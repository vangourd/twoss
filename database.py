from abc import ABC, abstractmethod
import pyodbc

class Database(ABC):
    
    @abstractmethod
    def connect(self):
        pass


class MSSql(Database):

    def __init__(self,driver,server,database,uid,password):
        self.driver = driver
        self.server = server
        self.database = database
        self.uid = uid
        self.password = password
        self.cursor = None
        try:
            self.connect()
        except Exception as e:
            print(e)
            raise

    def connect(self) -> bool:
        try:
            conn = pyodbc.connect(
                driver=self.driver,
                server=self.server,
                database=self.database,
                uid=self.uid,
                password=self.password
            )
            self.cursor = conn
            return True
        except Exception as e:
            print(e)
            return False

    def execute(self, sql):
        try:
            query = self.cursor.execute(sql)
            return query
        except Exception as e:
            return (False, e)
        finally:
            query.close()