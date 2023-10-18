from models.__init__ import CURSOR,CONN

class Factory:

    all={}

    def __init__(self,name,country,id = None):
        self.id = id
        self.name = name
        self.country = country

    def __repr__(self):
        return f"<Factory {self.id}: {self.name}, {self.country}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if type(name)==str and len(name):
            self._name = name
        else:
            raise Exception("The name must be a string with more than 1 character!")

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self,country):
        if type(country)==str and len(country):
            self._country =country
        else:
            raise Exception("The country must be a string with more than 1 character!")

    
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of factory instances """
        sql = """
            CREATE TABLE IF NOT EXISTS factories (
            id INTEGER PRIMARY KEY,
            name TEXT,
            country TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        
        sql = """
            DROP TABLE IF EXISTS factories;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        
        sql = """
            INSERT INTO factories (name, country)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.country))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, country):
        
        factory = cls(name, country)
        factory.save()
        return factory

    def update(self):
        
        sql = """
            UPDATE factories
            SET name = ?, country = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.country, self.id))
        CONN.commit()

    def delete(self):
 
        sql = """
            DELETE FROM factories
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def instance_from_db(cls, row):
 
        factory = cls.all.get(row[0])
        if factory:
            factory.name = row[1]
            factory.country = row[2]
        else:
            factory = cls(row[1], row[2])
            factory.id = row[0]
            cls.all[factory.id] = factory
        return factory

    @classmethod
    def get_all(cls):
  
        sql = """
            SELECT *
            FROM factories
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM factories
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM factories
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def cars(self):
        from models.car import Car
        sql = """
            SELECT * FROM cars
            WHERE factory_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Car.instance_from_db(row) for row in rows
        ]
