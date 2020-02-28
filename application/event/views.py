from flask import redirect, render_template, request, url_for
from flask_login import current_user, login_required

from application import app, db, get_css_framework, ITEMS_PER_PAGE
from application.auth.models import User
from application.event.models import Event
from application.event.models import absence_event
from application.event.forms import EventForm
from application.absence.models import Absence
from application.room.models import Room
from application.place.models import Place
from flask_paginate import Pagination, get_page_parameter


@app.route("/event", methods=["GET"])
def events_index():
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)

    total = Event.query.count()
    events = Event.find_events((page - 1) * ITEMS_PER_PAGE, ITEMS_PER_PAGE)
    pagination = Pagination(page=page, total=total, search=search, record_name='events', per_page=ITEMS_PER_PAGE,
                            css_framework=get_css_framework(), format_total=True, format_number=True)

    return render_template("event/list.html", events=events, pagination=pagination)


@app.route("/event/<event_id>/", methods=["GET"])
def event_view(event_id):
    event = Event.query.join(Room, isouter=True).join(Place, isouter=True).filter(Event.id == event_id).first()

    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)

    total = Event.query.join(absence_event).filter(Event.id == event_id).count()
    notavailables = Event.find_absent_users_for_event(event_id, (page - 1) * ITEMS_PER_PAGE, ITEMS_PER_PAGE)
    pagination = Pagination(page=page, total=total, search=search, record_name='absents', per_page=ITEMS_PER_PAGE,
                            css_framework=get_css_framework(), format_total=True, format_number=True)

    return render_template("event/view.html", event=event, notavailables=notavailables, pagination=pagination)


@app.route("/event/new/")
@login_required
def events_form():
    return render_template("event/new.html", form=EventForm(), rooms=Room.query.order_by(Room.name).all())


@app.route("/event/", methods=["POST"])
@login_required
def events_create():
    room_id = request.form.get('room_id')
    form = EventForm(request.form)
    if form.date_start.data is None:
        return render_template("absence/new.html", form=form, message="Start date should not be empty.",
                               rooms=Room.query.order_by(Room.name).all())
    if form.date_end.data is None:
        return render_template("absence/new.html", form=form, message="End date should not be empty.",
                               rooms=Room.query.order_by(Room.name).all())
    if form.date_start.data > form.date_end.data:
        return render_template("event/new.html", form=form, message="Start date should be before end date.",
                               rooms=Room.query.order_by(Room.name).all())
    if not form.validate():
        return render_template("event/new.html", form=form, rooms=Room.query.order_by(Room.name).all())

    newevent = Event(form.name.data, form.description.data,
                     form.date_start.data, form.date_end.data)
    if room_id:
        newevent.room_id = room_id
    db.session().add(newevent)
    db.session().commit()

    absences_during_event = Absence.find_absences_between_timepoints(newevent.date_start, newevent.date_end)

    for absence in absences_during_event:
        statement = absence_event.insert().values(absence_id=absence.id, event_id=newevent.id)
        db.session.execute(statement)
    db.session().commit()

    message = "New event created!"
    return render_template("event/new.html", form=EventForm(), rooms=Room.query.order_by(Room.name).all(),
                           message=message)
