from application import db
from application.models import Base


class Instrument(Base):

    name = db.Column(db.String(144), nullable=False)

    account = db.relationship("User", backref='Instrument', lazy=True)

    def __init__(self, name):
        self.name = name
