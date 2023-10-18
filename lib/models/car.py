from models.__init__ import CURSOR, CONN
from models.factory import Factory

class Car:

    all={}

    def __init__(self,model,year,weight,factory_id=None,id = None):
        self.id =id
        self.model = model
        self.year = year
        self.weight = weight
        self.factory_id = factory_id

    def __repr__(self):
        return (
            f"<Car {self.id}: {self.model}, {self.year}, {self.weight}, " + 
            f"Factory ID: {self.factory_id}>")

    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self,model):
        if type(model)==str and len(model)>1:
            self._model=model
        else:
            raise Exception("Model must be a non-empty string!")
        
    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self,year):
        if type(year) == int:
            self._year = year
        else:
            raise ValueError("Year must be an integer!")
        
    @property
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self,weight):
        if type(weight) == float:
            self._weight = weight
        else:
            raise ValueError("Weight must be a float!")
        
    @property
    def factory_id(self):
        return self._factory_id

    @factory_id.setter
    def factory_id(self, factory_id):
        if type(factory_id) is int and Factory.find_by_id(factory_id):
            self._factory_id = factory_id
        else:
            raise Exception("Factory_id must reference a factory in the database")
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS cars (
            id INTEGER PRIMARY KEY,
            model TEXT,
            year INT,
            weight FLOAT,
            factory_id INTEGER,
            FOREIGN KEY (factory_id) REFERENCES factories(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS cars;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
                INSERT INTO cars (model, year, weight, factory_id)
                VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.model, self.year, self.weight, self.factory_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE cars
            SET model = ?, year = ?, weight = ?, factory_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.model, self.year,
                             self.weight, self.factory_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM cars
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def create(cls, model, year, weight, factory_id):
        car = cls(model, year, weight, factory_id)
        car.save()
        return car

    @classmethod
    def instance_from_db(cls, row):
        car = cls.all.get(row[0])
        if car:
            car.model = row[1]
            car.year = row[2]
            car.weight = row[3]
            car.factory_id = row[4]
        else:
            car = cls(row[1], row[2], row[3], row[4])
            car.id = row[0]
            cls.all[car.id] = car
        return car

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM cars
        """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM cars
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_model(cls, model):
        sql = """
            SELECT *
            FROM cars
            WHERE model is ?
        """

        row = CURSOR.execute(sql, (model,)).fetchone()
        return cls.instance_from_db(row) if row else None