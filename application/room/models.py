from application import db
from application.models import Base


class Room(Base):

    name = db.Column(db.String(144), nullable=False)

    place_id = db.Column(db.Integer, db.ForeignKey('place.id'))
    event = db.relationship("Event", backref='Room', lazy=True)

    def __init__(self, name):
        self.name = name
