from flask_wtf import FlaskForm
from wtforms import DateField, StringField, TextField, validators


class EventForm(FlaskForm):
    name = StringField("Event name", [validators.Length(min=2)])
    description = TextField("Event description")
    date_start = DateField('Start date YYYY-MM-DD', format='%Y-%m-%d')
    date_end = DateField('End date YYYY-MM-DD', format='%Y-%m-%d')

    class Meta:
        csrf = False
