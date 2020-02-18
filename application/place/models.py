from application import db
from application.models import Base


class Place(Base):

    name = db.Column(db.String(144), nullable=False)
    address = db.Column(db.String(144))

    room = db.relationship("Room", backref='Place', lazy=True)

    def __init__(self, name, address):
        self.name = name
        self.address = address
