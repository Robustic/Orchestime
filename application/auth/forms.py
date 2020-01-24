from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField


class NewaccountForm(FlaskForm):
    name = StringField("Name")
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False


class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False
