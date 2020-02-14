from flask import redirect, render_template, request, url_for
from flask_login import current_user, login_required

from application import app, db
from application.auth.models import User
from application.event.models import Event
from application.event.models import absence_event
from application.event.forms import EventForm
from application.absence.models import Absence


@app.route("/event", methods=["GET"])
def events_index():
    events = Event.find_events()
    return render_template("event/list.html", events=events)


@app.route("/event/<event_id>/", methods=["GET"])
def event_view(event_id):
    event = Event.query.get(event_id)
    notavailables = Event.find_absent_users_for_event(event_id)
    return render_template("event/view.html", event=event, notavailables=notavailables)


@app.route("/event/new/")
@login_required
def events_form():
    return render_template("event/new.html", form=EventForm())


@app.route("/event/", methods=["POST"])
@login_required
def events_create():
    form = EventForm(request.form)
    if not form.validate():
        return render_template("event/new.html", form=form)

    newevent = Event(form.name.data, form.description.data,
                     form.date_start.data, form.date_end.data)
    db.session().add(newevent)
    db.session().commit()

    absences_during_event = Absence.find_absences_between_timepoints(newevent.date_start, newevent.date_end)

    for absence in absences_during_event:
        statement = absence_event.insert().values(absence_id=absence.id, event_id=newevent.id)
        db.session.execute(statement)
    db.session().commit()

    return redirect(url_for("events_index"))
