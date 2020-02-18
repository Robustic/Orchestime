from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField
from application.place.models import Place


class RoomForm(FlaskForm):
    name = StringField("Room name", [validators.Length(min=2, max=140)])

    class Meta:
        csrf = False


class RoomUpdateForm(FlaskForm):
    name = StringField("New room name", [validators.Length(min=2, max=140)])

    class Meta:
        csrf = False
