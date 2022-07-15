from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField, EmailField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
#    username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
    email = EmailField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    numberphone = StringField('numero de telefono',validators=[DataRequired()])
    Genero=StringField('numero de telefono',validators=[DataRequired()])
    Nombre=StringField('Genero',validators=[DataRequired()])
    submit = SubmitField('Registrarse')

class LoginForm(FlaskForm):
    email = EmailField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember =BooleanField('Remember Me')
    submit = SubmitField('Iniciar Sesion')

class Olvide(FlaskForm):
    email = EmailField('Email',validators=[DataRequired(), Email()])
    submit = SubmitField('Iniciar Sesion')

class ContactoForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=2,max=30)])
    email = EmailField('Email',validators=[DataRequired(), Email()])
    number = StringField('Phone',validators=[DataRequired(),Length(min=10,max=20)])
    mensaj = StringField('Phone',validators=[DataRequired(),Length(min=15,max=100)])

#    password = PasswordField('Password',validators=[DataRequired()])
#    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Enviar')
