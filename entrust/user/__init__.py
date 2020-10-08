from datetime import datetime
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

app.secret_key = '2a44c7f6b5a25bd255d1488e75830f43'
app.config["SQLALCHEMY_DATABASE_URI"] ='mysql+pymysql://root:@localhost:3306/damirez'
db = SQLAlchemy(app)





from entrust.idle.routes import idle
from entrust.user.routes import user
from entrust.Account.routes import Account

app.register_blueprint(idle)
app.register_blueprint(user)
app.register_blueprint(Account)

from entrust import routes