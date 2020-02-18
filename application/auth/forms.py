from flask_wtf import FlaskForm
from wtforms import PasswordField, SelectField, StringField, validators
from application.instrument.models import Instrument


class NewaccountForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2, max=140)])
    username = StringField("Username", [validators.Length(min=4, max=140)])
    password = PasswordField("Password", [validators.Length(min=10, max=140)])

    class Meta:
        csrf = False


class UpdateaccountForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2, max=140)])

    class Meta:
        csrf = False


class LoginForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=4, max=140)])
    password = PasswordField("Password", [validators.Length(min=10, max=140)])
  
    class Meta:
        csrf = False
