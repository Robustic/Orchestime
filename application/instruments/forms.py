from flask_wtf import FlaskForm
from wtforms import StringField, validators


class InstrumentForm(FlaskForm):
    name = StringField("Instrument name", [validators.Length(min=2)])
    
    class Meta:
        csrf = False


class InstrumentupdateForm(FlaskForm):
    name = StringField("Updated name", [validators.Length(min=2)])

    class Meta:
        csrf = False
