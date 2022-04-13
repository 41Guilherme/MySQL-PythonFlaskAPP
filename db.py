import mysql.connector
from configparser import ConfigParser

config = ConfigParser()
config.read('auth.ini')

host = config['auth']['host']
db   = config['auth']['db']
user = config['auth']['user']
passw= config['auth']['passw']

class Query():
    
    def __init__(self, host, db, user, passw):
        self.con = mysql.connector.connect(host=host,
                                           database=db,
                                           user=user,
                                           password=passw)
        
    def insertItem(self, id : int, name : str, idade :int):
        if self.con.is_connected:
            cursor = self.con.cursor()
            cursor.execute(f"INSERT INTO teste(idTeste, Name, Idade) VALUES({id},'{name}',{idade})")
            self.con.commit()
            cursor.close()
    
    def getAllData(self):
        if self.con.is_connected():
            cursor = self.con.cursor()
            cursor.execute("SELECT * FROM teste")
            data = []
            for item in cursor:
                data.append({
                    "id"  : item[0],
                    "name": item[1],
                    "age" : item[2]
                })
                
            cursor.close()
            return data
        
    def getEspecificPerson(self, name : str):
        data = self.getAllData()
        for item in data:
            if name in item:
                return item 
        return None
    
    def deleteEspecificItem(self, id : int):
        cursor = self.con.cursor()
        cursor.execute(f"DELETE FROM teste WHERE idTeste = {id}")
        self.con.commit()
        cursor.close()
    
        return None
    
DB = Query(host,db,user,passw)