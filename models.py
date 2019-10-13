import datetime

class WorkOrder():
    
    def __init__(self,db):
        self.db = db
    
    def newest(self,qty):
        query = \
        """SELECT TOP {}
                id,
                workdescription,
                ownerid
            FROM
                WoxTickets
            ORDER BY
                dtcreated DESC;""".format(qty)
        result = self.db.cursor.execute(query)
        wo = []
        for row in result:
            wo.append(row)
        return wo

    

class Person():
    pass

class Location():
    pass

class Company():
    pass