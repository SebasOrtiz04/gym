import psycopg2
from diccionarios import conexionBase

class basededatos:
    """
    Aqui la conexión a base de datos
    
    """
    
    def __init__(self,sql):
        self.sql=sql
        mydb= psycopg2.connect(
            host=conexionBase['host'],
            user=conexionBase['user'],
            port=conexionBase['port'],
            password=conexionBase['password'],
            database=conexionBase['database'])
        # print('--------------------')
        # print (mydb)
        # print('--------------------')
        self.cursor = mydb.cursor()
        self.cursor.execute(self.sql)
        return print(f'comando {self.sql} ejecutado')

    def fila(self):
        return self.cursor.fetchone()

    def variasfilas(self):
        return self.cursor.fetchall()
    
    def concommit(self):
        self.cursor.execute('COMMIT;')

print(__name__)