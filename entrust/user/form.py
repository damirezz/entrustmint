from flask_wtf import FlaskForm
from wtforms.fields import StringField, BooleanField, PasswordField,SubmitField,IntegerField,SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp
from qanda.models import User



class RegistrationForm(FlaskForm):
  firstname= StringField("FirstName", validators=[DataRequired(), Regexp('^[A-Za-z]{3,}$',
  message='First name can only contain letters')])
  lastname= StringField("LastName", validators=[DataRequired(),Regexp('^[A-Za-z]{3,}$', 
  message='First name can only contain letters')])
  email = StringField("Email", validators=[DataRequired(),
  Email(message='Invalid email address')])
  phonenumber=StringField('Phone', validators=[DataRequired(), Length(min=10, message='Phone Number is too short'), 
  Regexp('^[0-9]{3,}$',message='Invalid Phone Number')])
  password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm_password', 
  message="Password Must Match"
    )])
  confirm_password = PasswordField("Confirm Password", validators=[DataRequired()])
  terms=BooleanField("i agree to the terms and condition")
  


  def validate_email(self, email):
        email = User.query.filter_by(email = email.data).first()
        if email:
            raise ValueError('This Email Has Been Used')
    
    def validate_phone(self, phonenumber):
        phonenumber = User.query.filter_by(phonenumber = phone.data).first()
        if phonenumber:
            raise ValueError('This Phone Number Has Been Used Registered by Another User') 

class LoginForm(FlaskForm):
  email=StringField("Email",validators=[DataRequired(), Email(message='Invalid email address')])
  password=PasswordField("password",validators=[DataRequired()])
  remember=BooleanField("Remember Me")
  

 class UpdateAccountInfo(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired(), Regexp('^[A-Za-z]{3,}$',
                message='First name can only contain letters')])
    lastname = StringField('Last Name', validators=[DataRequired(), Regexp('^[A-Za-z]{3,}$',
                message='Last name can only contain letters')])
    phonenumber = StringField('Phone', validators=[DataRequired(), Length(min=10, message='Phone Number is too short'), Regexp('^[0-9]{3,}$',
                message='Invalid Phone Number')])  
   
   
   
   