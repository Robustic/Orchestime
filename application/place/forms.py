from flask_wtf import FlaskForm
from wtforms import StringField, validators


class PlaceForm(FlaskForm):
    name = StringField("Place name", [validators.DataRequired(message="Place name can't be empty"),
                                      validators.Length(min=2, max=140)])
    address = StringField("Address", [validators.Length(max=140)])

    class Meta:
        csrf = False


class PlaceUpdateForm(FlaskForm):
    name = StringField("New place name", [validators.DataRequired(message="Place name can't be empty"),
                                          validators.Length(min=2, max=140)])
    address = StringField("New address", [validators.Length(max=140)])

    class Meta:
        csrf = False
