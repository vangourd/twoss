import datetime

class WorkOrder():
    
    def __init__(self,db):
        self.db = db
    
    def newest(self,qty):
        query = \
        """SELECT TOP {}
                id,
                dtcreated,
                workdescription,
                ownerid
            FROM
                WoxTickets
            ORDER BY
                dtcreated DESC;""".format(qty)
        result = self.db.cursor.execute(query)
        wo = []
        for row in result:
            wo.append({
                'id': row[0],
                'dtcreated': row[1],
                'workdescription': row[2],
                'ownerid': row[3]
            })
        return wo

    

class Person():
    pass

class Location():
    pass

class Company():
    pass