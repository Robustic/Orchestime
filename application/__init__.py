from flask import Flask
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///orchestime.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from application.instrument import models
from application.absence import models
from application.event import models
from application.auth import models
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_message = "Please login to use this functionality."
login_manager.login_view = "auth_login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


try:
    db.create_all()
except:
    pass
    print("***Error, database not created. ***")


from application.instrument.models import Instrument

if not Instrument.query.filter_by(name="Instrument not selected").first():
    instr = Instrument("Instrument not selected")
    db.session().add(instr)
    db.session().commit()

from application import views
from application.instrument import views
from application.absence import views
from application.event import views
from application.auth import views
