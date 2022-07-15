from basededatos import basededatos
from usuarios import usuario
from werkzeug.security import check_password_hash,generate_password_hash

class Modeluser():

    @classmethod
    def login(self,usur):
        try:
            print('hola')
            row=basededatos("SELECT * FROM users WHERE correo=(\'"+usur.user+"\')")
            row=row.fila()
            if row != None:
                usur=usuario(row[0],check_password_hash(row[1],usur.contra))
                return usur


        except Exception as ex:
            raise Exception(ex)