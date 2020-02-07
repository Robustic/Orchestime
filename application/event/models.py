from application import db
from application.models import Base

from sqlalchemy.sql import text


absence_event = db.Table('absence_event',
                         db.Column('absence_id', db.Integer, db.ForeignKey('absence.id'), nullable=False),
                         db.Column('event_id', db.Integer, db.ForeignKey('event.id'), nullable=False),
                         db.PrimaryKeyConstraint('absence_id', 'event_id'))


class Event(Base):
    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(1000))
    date_start = db.Column(db.DateTime, nullable=False)
    date_end = db.Column(db.DateTime, nullable=False)

    absence_events = db.relationship('Absence', secondary=absence_event, backref='event')

    def __init__(self, name, description, date_start, date_end):
        self.name = name
        self.description = description
        self.date_start = date_start
        self.date_end = date_end

    @staticmethod
    def find_events_between_timepoints(start, end):
        stmt = text("SELECT * FROM Event"
                    " WHERE (Event.date_end >= :x)"
                    " AND (Event.date_start <= :y)")
        stmt = stmt.bindparams(x=start, y=end)
        return db.engine.execute(stmt)

    @staticmethod
    def find_absent_users_for_event(event_id):
        stmt = text("SELECT account.name as account_name,"
                    " Absence.name as absence_name,"
                    " Absence.description as absence_description,"
                    " Absence.date_start as absence_date_start,"
                    " Absence.date_end as absence_date_end"
                    " FROM Event"
                    " LEFT JOIN absence_event ON Event.id = absence_event.event_id"
                    " LEFT JOIN Absence ON Absence.id = absence_event.absence_id"
                    " LEFT JOIN account ON account.id = Absence.account_id"
                    " WHERE (Event.id = :x)")
        stmt = stmt.bindparams(x=event_id)
        return db.engine.execute(stmt)
