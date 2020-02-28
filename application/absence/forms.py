from flask_wtf import FlaskForm
from wtforms import StringField, TextField, validators
from wtforms_components import DateField


class AbsenceForm(FlaskForm):
    name = StringField("Absence name", [validators.DataRequired(message="Absence name can't be empty"),
                                        validators.Length(min=2, max=140)])
    description = StringField("Absence description", [validators.Length(max=996)])
    date_start = DateField('Start date YYYY-MM-DD', [validators.DataRequired(message="Start date can't be empty")])
    date_end = DateField('End date YYYY-MM-DD', [validators.DataRequired(message="Start date can't be empty")])

    class Meta:
        csrf = False
