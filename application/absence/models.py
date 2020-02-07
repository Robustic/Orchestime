from application import db
from application.models import Base


class Absence(Base):

    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.Text(10000))
    date_start = db.Column(db.DateTime, nullable=False)
    date_end = db.Column(db.DateTime, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name, description, date_start, date_end, account_id):
        self.name = name
        self.description = description
        self.date_start = date_start
        self.date_end = date_end
        self.account_id = account_id
