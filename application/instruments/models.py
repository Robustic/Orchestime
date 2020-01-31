from application import db


class Instrument(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)

    account = db.relationship("User", backref='Instrument', lazy=True)

    def __init__(self, name):
        self.name = name
        self.done = False
