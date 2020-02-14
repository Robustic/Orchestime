from flask_wtf import FlaskForm
from wtforms import DateField, StringField, TextField, validators


class AbsenceForm(FlaskForm):
    name = StringField("Absence name", [validators.Length(min=2, max=140)])
    description = StringField("Absence description", [validators.Length(max=996)])
    date_start = DateField('Start date YYYY-MM-DD', format='%Y-%m-%d')
    date_end = DateField('End date YYYY-MM-DD', format='%Y-%m-%d')

    class Meta:
        csrf = False
