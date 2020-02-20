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

    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
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
    def find_events():
        stmt = text("SELECT Event.name AS event_name,"
                    " Event.description AS event_description,"
                    " Event.date_start AS event_date_start,"
                    " Event.date_end AS event_date_end,"
                    " Event.id AS event_id,"
                    " Room.name AS room_name,"
                    " Place.name AS place_name,"                    
                    " COUNT(DISTINCT Account.id) as count_names"
                    " FROM Event"
                    " LEFT JOIN absence_event ON Event.id = absence_event.event_id"
                    " LEFT JOIN Absence ON Absence.id = absence_event.absence_id"
                    " LEFT JOIN account ON account.id = Absence.account_id"
                    " LEFT JOIN Room ON Room.id = Event.room_id"
                    " LEFT JOIN Place ON Place.id = Room.place_id"
                    " GROUP BY Event.id, Room.name, Place.name"
                    " ORDER BY event_name")
        return db.engine.execute(stmt)

    @staticmethod
    def find_absent_users_for_event(event_id):
        stmt = text("SELECT account.name AS account_name,"
                    " Absence.name AS absence_name,"
                    " Absence.description AS absence_description,"
                    " Absence.date_start AS absence_date_start,"
                    " Absence.date_end AS absence_date_end"
                    " FROM Event"
                    " LEFT JOIN absence_event ON Event.id = absence_event.event_id"
                    " LEFT JOIN Absence ON Absence.id = absence_event.absence_id"
                    " LEFT JOIN account ON account.id = Absence.account_id"
                    " WHERE (Event.id = :x)"
                    " ORDER BY account_name, absence_date_start, absence_date_end")
        stmt = stmt.bindparams(x=event_id)
        return db.engine.execute(stmt)

    @staticmethod
    def find_all_absents_for_user(user_id):
        stmt = text("SELECT Event.name AS event_name,"
                    " Event.date_start AS event_date_start,"
                    " Event.date_end AS event_date_end,"
                    " Absence.name AS absence_name,"
                    " Absence.description AS absence_description,"
                    " Absence.date_start AS absence_date_start,"
                    " Absence.date_end AS absence_date_end"
                    " FROM Absence"
                    " LEFT JOIN absence_event ON Absence.id = absence_event.absence_id"
                    " LEFT JOIN Event ON Event.id = absence_event.event_id"                    
                    " LEFT JOIN account ON account.id = Absence.account_id"
                    " WHERE (account.id = :x)"
                    " ORDER BY event_name, event_date_start, event_date_end, absence_date_start, absence_date_end")
        stmt = stmt.bindparams(x=user_id)
        return db.engine.execute(stmt)
