from flask_wtf import FlaskForm
from wtforms import StringField, TextField, validators
from wtforms_components import DateField


class EventForm(FlaskForm):
    name = StringField("Event name", [validators.DataRequired(message="Event name can't be empty"),
                                      validators.Length(min=2, max=140)])
    description = StringField("Event description", [validators.Length(max=996)])
    date_start = DateField('Start date', [validators.DataRequired(message="Start date can't be empty")])
    date_end = DateField('End date', [validators.DataRequired(message="End date can't be empty")])

    class Meta:
        csrf = False
