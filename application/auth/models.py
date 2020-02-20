from application import db
from application.models import Base

from sqlalchemy.sql import text


class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    instrument_id = db.Column(db.Integer, db.ForeignKey('instrument.id'))
    absence = db.relationship("Absence", backref='account', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    @staticmethod
    def participation_percent_for_events(account_id):
        stmt = text("SELECT account.id AS account_id,"
                    " 100 - COUNT(DISTINCT Event.id) * 100 / (SELECT COUNT(*) FROM Event) as count_events"
                    " FROM account"
                    " LEFT JOIN Absence ON account.id = Absence.account_id"
                    " LEFT JOIN absence_event ON Absence.id = absence_event.absence_id"
                    " LEFT JOIN Event ON Event.id = absence_event.event_id"
                    " WHERE (account_id = :x)")
        stmt = stmt.bindparams(x=account_id)
        return db.engine.execute(stmt)
