from pyexpat import model
from random import *
from flask import Flask,render_template, request, send_from_directory,flash,redirect, url_for
import os
from usuarios import usuario
from forms import RegistrationForm,LoginForm,Olvide,ContactoForm
from datetime import datetime
from diccionarios import Config,correoEnvio
from basededatos import basededatos
#from contacto import contactoA
from werkzeug.security import check_password_hash,generate_password_hash
from modeluser import Modeluser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Cliente=basededatos("SELECT * FROM clientes WHERE \"ID\"=1")
# Cliente=Cliente.fila()

try:
    conectado='desconectado'
    print(conectado)
except:
    conectado='conectado'  
    print('No hay un usuario conectado')
    print(conectado)
else:
    print('hola otra vez')
    print(conectado)
finally:
    print('Se trato de conseguir el usuario')
    print(conectado)

app=Flask(__name__)
app.config['SECRET_KEY']=Config['SECRET_KEY']

#------------------------------------index
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        model.save()
        # Failure to return a redirect or render_template
    else:
        return render_template('index.html')

@app.route('/nosotros')
def nosotros():    
    return render_template('nosotros.html')

@app.route('/producto')
def producto():    
    return render_template('producto.html')

@app.route('/tienda')
def tienda():    
    return render_template('tienda.html')

@app.route('/register',methods=["POST","GET"])
def register():
    form = RegistrationForm()
    user=form.email.data
    contra=form.password.data
    confirmacion=form.confirm_password.data
    phone=form.numberphone.data
    Nombre=form.Nombre.data
    Genero=form.Genero.data

    if request.method =="POST":
#------------------------------Esto crea al usuario 
        if contra == confirmacion:
            print('-'*10)
            contrahash=str((generate_password_hash(contra)))
            print(contrahash)
            print('-'*10)
            #------------------------------Inserta en la base de datos
            usu=basededatos("SELECT * FROM users WHERE correo=(\'"+user+"\')")
            usu = usu.fila()
            print("VALIDANDO SI EXISTE"+user+"EN LA BASE DE DATOS")
            if usu is None :
                variable = basededatos("INSERT INTO users VALUES(\'"+user+"\',\'"+contrahash+"\',\'"+phone+"\',\'"+Genero+"\',\'"+Nombre+"\',True)")
                variable.concommit()
                if form.validate_on_submit():
                    flash(f'Cuenta Creada para {form.email.data}!', 'success')
                    print(f'Cuenta Creada para {form.email.data}!', 'success')
                    print(f'Cuenta conectada de {form.email.data}!', 'success')
                    flash(f'Cuenta conectada de {form.email.data}!', 'success')
            else:
                flash('Este correo ya tiene una cuenta con nosotros.')
                print('Este correo ya tiene una cuenta con nosotros.')
            return redirect(url_for('index'))
        else:
            flash('La contraseña no coincide con la confirmación de contraseña','error')
            print('La contraseña no coincide con la confirmación de contraseña')
        print('Registrandose')
    return render_template('register.html',title='Register',form=form,conectado=conectado)


@app.route('/login',methods=["POST","GET"])
def login():
    conectado='desconectado'
    form = LoginForm()
    if request.method =="POST":
        user=form.email.data
        contra=form.password.data
            #------------------------------Esto toma el texto del html
        #valoresv=[user,contra]
        print("\""+user+"\"")
#------------------------------Esto crea al usuario 
        #user1=usuario(user,contra)
#------------------------------Esto inicia la sesion
        #print(user1)
        usu = basededatos("SELECT * FROM users WHERE correo=(\'"+user+"\')")
        usu = usu.fila()
        if usu is None :
            if form.validate_on_submit():
                flash(f'No cuentas con una cuenta aun... Puedes crear una ahora', 'success')
                return redirect(url_for('register'))
        elif check_password_hash(usu[1],contra):#usu[1] es la contraseña hasheada
            usur=usuario(user,contra)
            logged_user=Modeluser.login(usur)
            if logged_user != None:
                if logged_user.contra:
                    conectado='conectado'
                    print(conectado)
                    flash('estatus conectado')
                    print('estatus conectado')
                    return redirect(url_for('index',conectado=conectado))
                else:
                    flash('Contraseña no valida')
                    return redirect(url_for('login'))
            else:
                flash('Usuario no encontrado')
            print("VALIDANDO SI EXISTE "+user+" EN LA BASE DE DATOS")
            print("usuario existente en la base de datos "+usu[0])
            variable=basededatos("UPDATE users SET status=True WHERE correo=\'"+usu[0]+"\';")
            variable.concommit()
            flash(f'Cuenta conectada de {usu[0]}!', 'success')
            print(f'Cuenta conectada de {usu[0]}!', 'success')
            return redirect(url_for('index'))

        else:
            flash(f'Contraseña incorrecta', 'error')

    return render_template('login.html',title='Login',form=form,conectado=conectado)

@app.route('/olvide',methods=["POST","GET"])
def olvide():
    form = Olvide()
    if request.method =="POST":

            user=form.email.data
            usu = basededatos("SELECT * FROM users WHERE correo=(\'"+user+"\')")
            usu = usu.fila()
            #----------------------------------------------cosas random para hacer contraseña nueva
            palabras=['Pastadedientes','Gelantibacterial','Avengers','Dccomics','Palabra','Comillas','Comasimple','Teclado']
            simbolos=['@','#','!','%','&','?','¿','¡']
            indice=randrange(len(palabras))
            palabra=palabras[indice]
            simbolo=simbolos[indice]
            contra=str(indice)+palabra+simbolo
            contranueva=str((generate_password_hash(contra)))
            
            #----------------------------------------------cosas random para hacer contraseña nueva

            variable = basededatos("UPDATE users SET passwd=\'"+contranueva+"\' WHERE correo = \'"+user+"\'")
            variable.concommit()
            print("VALIDANDO SI EXISTE "+user+" EN LA BASE DE DATOS")        
            if usu is None:
                if form.validate_on_submit():
                    flash(f'No cuentas con una cuenta aun... Puedes crear una ahora', 'success')
                    return redirect(url_for('register'))
            else:
                if form.validate_on_submit():
                    server = smtplib.SMTP('smtp.gmail.com',587)
                    server.starttls()
                    mail_content = "Tu nueva contraseña es: "+contra
                    sender_address = correoEnvio['elQueEnvia']
                    sender_pass = 'qsdwxssgqpjcaikn'
                    server.login(sender_address,sender_pass)
                    receiver_address = usu[0]
                    print('Aquí se esta enviando un correo según')
                    message = MIMEMultipart()
                    message['From'] = sender_address
                    message['To'] = receiver_address
                    message['Subject'] = 'Olvidaste tu contraseña'   
                    message.attach(MIMEText(mail_content, 'plain'))
                    text = message.as_string()
                    server.sendmail(sender_address,receiver_address,text)
                    server.quit()
                    flash(f'Coreo enviado a {user}!', 'success')
                    print(f'Coreo enviado a {user}!')
                    print('Se envío correo con la contraseña')
                    flash('Se envío correo con la contraseña','success')
                    
    return render_template('olvide.html',title='Olvide mi contraseña',form=form,conectado=conectado)

print(__name__)

if __name__ =='__main__':
    app.run(debug=True)