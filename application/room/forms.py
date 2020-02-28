from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField
from application.place.models import Place


class RoomForm(FlaskForm):
    name = StringField("Room name", [validators.DataRequired(message="Room name can't be empty"),
                                     validators.Length(min=2, max=140)])

    class Meta:
        csrf = False


class RoomUpdateForm(FlaskForm):
    name = StringField("New room name", [validators.DataRequired(message="Room name can't be empty"),
                                         validators.Length(min=2, max=140)])

    class Meta:
        csrf = False
