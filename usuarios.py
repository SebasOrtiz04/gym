from flask import request,flash, redirect, url_for,render_template
from werkzeug.security import check_password_hash,generate_password_hash
# from forms import RegistrationForm,LoginForm
#from diccionarios import AWSCognito
import os
import boto3
from basededatos import basededatos

#Cliente=basededatos("SELECT * FROM clientes WHERE \"ID\"=1")
#Cliente=Cliente.fila()

#username = AWSCognito['username']
#confirm_code = AWSCognito['confirm_code']


# client = boto3.client('cognito-idp', region_name=os.getenv('COGNITO_REGION_NAME'))
# response = client.resend_confirmation_code(
#     ClientId=os.getenv('COGNITO_USER_CLIENT_ID'),
#     Username=username,
# )
# print(response)
#reenvio de mensaje para confirmar registro

class usuario():
    """Aquí todo los procesos par los usuarios, registro, logueo, 
    olvide mi contraseña y futuras funciones que se requieran para 
    los usuarios."""
    numeroUsuarios = 0
    def __init__(self, user,contra,**kargs):
        self.user = user
        self.contra=contra
        self.kargs=kargs
        self.conectado = False
        
    @classmethod
    def check_password(self,hashed_password,contra):
        return check_password_hash(hashed_password,contra)

    # @property # este decorador se usa para acceder indirectamente a la variable 
    # def conectar(self):
    #     print('Lamando metodo get conectado')
    #     return self.conectado

    # @conectar.setter
    # def conectar(self,conectarValor):
    #     """Aqui espera un valor Booleano"""
    #     print('Lamando metodo set conectar')
    #     self.conectado=conectarValor

   # def registrarse(self):
        
        # client = boto3.client('cognito-idp', region_name=os.getenv('COGNITO_REGION_NAME'))
        # response = client.confirm_sign_up(
        # ClientId=os.getenv('COGNITO_USER_CLIENT_ID'),
        # Username=username,
        # ConfirmationCode=confirm_code
        # )
        # print(response)
        # return render_template('register.html',title='Register',form=self.form,Cliente=Cliente)


    #def conectar(self):
        

        #     miContra =LoginForm().password.data
#     if miContra==self.contras:
#         print("Se conecto exitosamente")
#         self.conectado = True
#     else:
#         self.intentos-=1
#         if self.intentos>0:
#             print("Contraseña incorrecta,intenelo devuelta ..")
#             print("Intentos restantes",self.intentos)
#             self.conectar()
#         else:
#             print("No se pudo iniciar sesion")
#             print("Adios")
    # client = boto3.client('cognito-idp', region_name=os.getenv('COGNITO_REGION_NAME'))
    # response = client.sign_up(
    # ClientId=os.getenv('COGNITO_USER_CLIENT_ID'),
    # Username=self.user,
    # Password=self.contra
    # )
    # print(response)

    def desconectarse(self):
        if self.conectado:
            print("Se cerró su sesion con exito!!")
            self.conectado = False
        else:
            print("Error, no inicio sesion")

    def __str__(self):
        if self.conectado:
            connect="conectado"
        else:
            connect="desconectado"
        return print(f"Mi correo es \"{self.user}\" y estoy {connect}")
print(__name__)
if __name__ == '__main__':
    print('holi ')
