from asyncio import events
from pyexpat import model
from random import *
from flask import Flask,render_template, request, send_from_directory,flash,redirect, url_for
import os
#from usuarios import usuario
#from forms import RegistrationForm,LoginForm,Olvide,ContactoForm
from datetime import datetime
#from diccionarios import Config
#from basededatos import basededatos
#from contacto import contactoA
#from usuarios import usuario
from werkzeug.security import check_password_hash,generate_password_hash
#from modeluser import Modeluser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app=Flask(__name__)
#app.config['SECRET_KEY']=Config['SECRET_KEY']

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



print(__name__)

if __name__ =='__main__':
    app.run(debug=True)