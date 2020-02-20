from flask_wtf import FlaskForm
from wtforms import StringField, TextField, validators
from wtforms_components import DateField


class EventForm(FlaskForm):
    name = StringField("Event name", [validators.Length(min=2, max=140)])
    description = StringField("Event description", [validators.Length(max=996)])
    date_start = DateField('Start date')
    date_end = DateField('End date')

    class Meta:
        csrf = False
