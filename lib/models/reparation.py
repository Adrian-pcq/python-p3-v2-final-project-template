from models.__init__ import CURSOR,CONN

class Reparation:

    all={}

    def __init__(self,cause,model,year,weight,factory_id,id=None):
        self.id = id
        self.cause= cause
        self.model = model
        self.year = year
        self.weight = weight
        self.factory_id = factory_id
        

    def __repr__(self):
        return (
            f"<Car {self.id}: {self.model}, {self.year}, {self.weight}, " + 
            f"Factory ID: {self.factory_id}, Reparation: {self.cause}>")

    @property
    def cause(self):
        return self._cause
    
    @cause.setter
    def cause(self,cause):
        if type(cause)==str and len(cause)>0:
            self._cause = cause
        else:
            raise Exception("Cause must be a non-empty string!")
        

    @classmethod
    def create_table(cls):
        sql="""
            CREATE TABLE IF NOT EXISTS reparations (
            id INTEGER PRIMARY KEY,
            cause TEXT,
            model TEXT,
            year INT,
            weight FLOAT,
            factory_id INT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS reparations;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
                INSERT INTO reparations (cause, model, year, weight, factory_id)
                VALUES (?, ?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.cause, self.model, self.year, self.weight, self.factory_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def delete(self):
        sql = """
            DELETE FROM reparations
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def create(cls,cause, model, year, weight, factory_id):
        car = cls(cause, model, year, weight, factory_id)
        car.save()
        return car

    @classmethod
    def instance_from_db(cls, row):
        car = cls.all.get(row[0])
        if car:
            car.cause = row[1]
            car.model = row[2]
            car.year = row[3]
            car.weight = row[4]
            car.factory_id = row[5]
        else:
            car = cls(row[1], row[2], row[3], row[4], row[5])
            car.id = row[0]
            cls.all[car.id] = car
        return car

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM reparations
        """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM reparations
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_model(cls, model):
        sql = """
            SELECT *
            FROM reparations
            WHERE model is ?
        """

        row = CURSOR.execute(sql, (model,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_cause(cls, cause):
        sql = """
            SELECT *
            FROM reparations
            WHERE cause is ?
        """

        row = CURSOR.execute(sql, (cause,)).fetchone()
        return cls.instance_from_db(row) if row else None