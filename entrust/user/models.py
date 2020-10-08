from datetime import datetime
rom flask_login import UserMixin
from datetime import datetime
from entrust import db 



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname= db.Column(db.String(60))
    lastname = db.Column(db.String(60))
    email = db.Column(db.String(60), unique=True)
    phonenumber = db.Column(db.Text, unique=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    password = db.Column(db.Text)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    


     def __str__(self):
        return f"User {self.username}"


    class AccountDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    BankAccountName = db.Column(db.String(80), nullable = False)
    BankAccountNumber = db.Column(db.String(10), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False)
    SelectPackage = db.Column(db.String(40))
    activationcode = db.Column(db.Text, unique=True)
    
        def __str__(self):
             return self.bank_name

    