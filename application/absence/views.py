from flask import redirect, render_template, request, url_for
from flask_login import current_user, login_required

from application import app, db
from application.auth.models import User
from application.event.models import Event
from application.event.models import absence_event
from application.absence.models import Absence
from application.absence.forms import AbsenceForm


@app.route("/absence", methods=["GET"])
def absences_index():
    return render_template("absence/list.html", absences=Absence.query.join(User).all())


@app.route("/absence/new/")
@login_required
def absences_form():
    return render_template("absence/new.html", form=AbsenceForm())


@app.route("/absence/", methods=["POST"])
@login_required
def absences_create():
    form = AbsenceForm(request.form)
    if not form.validate():
        return render_template("absence/new.html", form=form)

    newabsence = Absence(form.name.data, form.description.data,
                         form.date_start.data, form.date_end.data, current_user.id)
    db.session().add(newabsence)
    db.session().commit()

    events_during_absence = Event.find_events_between_timepoints(newabsence.date_start, newabsence.date_end)

    for event in events_during_absence:
        statement = absence_event.insert().values(absence_id=newabsence.id, event_id=event.id)
        db.session.execute(statement)
    db.session().commit()

    return redirect(url_for("absences_index"))
