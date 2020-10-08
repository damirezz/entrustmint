from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.validators import DataRequired

class AccountForm:
    account_num = StringField('Account Number' validators=[DataRequired(), Length(min=10, max=10, message='Account number is too short or too long'), Regexp('^[0-9]{3,}$',
                message='Invalid Phone Number')])