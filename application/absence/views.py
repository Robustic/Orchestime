from flask import redirect, render_template, request, url_for
from flask_login import current_user, login_required

from application import app, db, get_css_framework, ITEMS_PER_PAGE
from application.auth.models import User
from application.event.models import Event
from application.event.models import absence_event
from application.absence.models import Absence
from application.absence.forms import AbsenceForm
from flask_paginate import Pagination, get_page_parameter


@app.route("/absence", methods=["GET"])
def absences_index():
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)

    total = Absence.query.count()
    absences = Absence.query.join(User, isouter=True).order_by(User.name, Absence.date_start, Absence.date_end) \
        .slice((page - 1) * ITEMS_PER_PAGE, page * ITEMS_PER_PAGE)
    pagination = Pagination(page=page, total=total, search=search, record_name='absences', per_page=ITEMS_PER_PAGE,
                            css_framework=get_css_framework(), format_total=True, format_number=True)

    return render_template("absence/list.html", absences=absences, pagination=pagination)


@app.route("/absence/new/")
@login_required
def absences_form():
    return render_template("absence/new.html", form=AbsenceForm())


@app.route("/absence/", methods=["POST"])
@login_required
def absences_create():
    form = AbsenceForm(request.form)
    if form.date_start.data is None:
        return render_template("absence/new.html", form=form, message="Start date should not be empty.")
    if form.date_end.data is None:
        return render_template("absence/new.html", form=form, message="End date should not be empty.")
    if form.date_start.data > form.date_end.data:
        return render_template("absence/new.html", form=form, message="Start date should be before end date.")
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

    message = "New absence created!"
    return render_template("absence/new.html", form=form, message=message)
