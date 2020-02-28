from flask_wtf import FlaskForm
from wtforms import StringField, validators


class InstrumentForm(FlaskForm):
    name = StringField("Instrument name", [validators.DataRequired(message="Instrument name can't be empty"),
                                           validators.Length(min=2, max=140)])
    
    class Meta:
        csrf = False


class InstrumentupdateForm(FlaskForm):
    name = StringField("Updated name", [validators.DataRequired(message="Instrument name can't be empty"),
                                        validators.Length(min=2, max=140)])

    class Meta:
        csrf = False
