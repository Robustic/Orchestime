from flask_wtf import FlaskForm
from wtforms import PasswordField, SelectField, StringField
from application.instruments.models import Instrument


class NewaccountForm(FlaskForm):
    name = StringField("Name")
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False


class UpdateaccountForm(FlaskForm):
    name = StringField("Name")
    instruments = Instrument.query.all()

    instrumentList = []
    instruments = Instrument.query.all()
    print("instruments: " + str(len(instruments)))
    for instrument in instruments:
        instrumentList.append((instrument.id, instrument.name))
    instrument_id = SelectField('Instrument', choices=instrumentList)

    class Meta:
        csrf = False


class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False
