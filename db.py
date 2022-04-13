import mysql.connector
from configparser import ConfigParser

config = ConfigParser()
config.read('auth.ini')

host  = config['auth']['host']
db    = config['auth']['db']
user  = config['auth']['user']
passw = config['auth']['passw']

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
            return True
        else:
            return False
    
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
        else:
            return None
        
    def getEspecificPerson(self, name : str):
        if self.con.is_connected():
            cursor = self.con.cursor()
            cursor.execute(f""" SELECT * FROM teste WHERE Name = "{name}" """)
            data = []
            for item in cursor:
                data.append({
                    "id"  : item[0],
                    "name": item[1],
                    "age" : item[2]
                })
            cursor.close()
            return data[0]
        return None
    
    def deleteEspecificItem(self, id : int):
        if self.con.is_connected:
            cursor = self.con.cursor()
            cursor.execute(f"DELETE FROM teste WHERE idTeste = {id}")
            self.con.commit()
            cursor.close()
            return True
    
        return False
    
    def updateEspecificItem(self, id : int, name : str, age : int):
        if self.con.is_connected:
            cursor = self.con.cursor()
            cursor.execute(f""" UPDATE teste 
                        SET Name = "{name}", Idade = {age} 
                        WHERE idTeste = {id}""")
            self.con.commit()
            cursor.close()
            return True
        return False
    
    def testClass(self):
        aux = self.getAllData()
        print(aux)
        
        self.insertItem(100, "TESTE",100)
        aux = self.getEspecificPerson("TESTE")
        print(aux)
        
        self.updateEspecificItem(100, "TESTE2",50)
        aux = self.getAllData()
        print(aux)
        
        self.deleteEspecificItem(100)
        aux = self.getAllData()
        print(aux)
    
DB = Query(host,db,user,passw)

if __name__ == "__main__":
    
    DB.testClass()
    
    
    