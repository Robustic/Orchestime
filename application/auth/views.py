from flask import redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user, current_user

from application import app, db, bcrypt, login_manager
from application.instrument.models import Instrument
from application.auth.models import User
from application.auth.forms import LoginForm, NewaccountForm, UpdateaccountForm
from application.event.models import Event, absence_event
from application.absence.models import Absence


@app.route("/auth/new")
def auth_form():
    return render_template("auth/newaccountform.html", form=NewaccountForm())


@app.route("/auth", methods=["POST"])
def auth_create():
    form = NewaccountForm(request.form)
    if not form.validate():
        return render_template("auth/newaccountform.html", form=form)

    account = User(form.name.data, form.username.data,
                   bcrypt.generate_password_hash(form.password.data).decode('utf-8'))
    db.session().add(account)
    db.session().commit()
    message = "You have now registered. You can log in."
    return render_template("index.html", message=message)


@app.route("/auth/<auth_id>/absences", methods=["GET"])
@login_required
def auth_view_my_absences(auth_id):
    if int(auth_id) != current_user.id:
        return login_manager.unauthorized()
    accountnow = User.query.get(auth_id)
    absenceforevents = User.query.join(Absence).join(absence_event).join(Event)\
        .filter(Absence.account_id == accountnow.id).all()
    participation = 100
    if Event.query.count() > 0 and len(absenceforevents) > 0:
        participation_percent_list = []
        for participation_percent in User.participation_percent_for_events(accountnow.id):
            participation_percent_list.append(participation_percent)
        participation = participation_percent_list[0].count_events

    return render_template("auth/viewmyabsences.html", account=accountnow,
                           participation=participation,
                           absences=Event.find_all_absents_for_user(accountnow.id))


@app.route("/auth/<auth_id>/", methods=["GET"])
@login_required
def auth_view(auth_id):
    if int(auth_id) != current_user.id:
        return login_manager.unauthorized()
    account = User.query.get(auth_id)
    return render_template("auth/update.html", account=account,
                           instruments=Instrument.query.order_by(Instrument.name).all(),
                           oldinstrument=Instrument.query.get(account.instrument_id), form=UpdateaccountForm())


@app.route("/auth/<auth_id>/update/", methods=["POST"])
@login_required
def auth_update(auth_id):
    instrument_id = request.form.get('instrument_id')
    if int(auth_id) != current_user.id:
        return login_manager.unauthorized()
    form = UpdateaccountForm(request.form)
    account = User.query.get(auth_id)
    if len(form.name.data) == 0:
        form.name.data = account.name
    if not form.validate():
        return render_template("auth/update.html", account=account,
                               instruments=Instrument.query.order_by(Instrument.name).all(),
                               oldinstrument=Instrument.query.get(account.instrument_id), form=UpdateaccountForm())
    account.name = form.name.data
    if instrument_id:
        account.instrument_id = instrument_id
    db.session().commit()
    message = "Your information have been saved"
    return render_template("index.html", message=message)


@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm())
    form = LoginForm(request.form)
    userfromdb = User.query.filter_by(username=form.username.data).first()
    if not userfromdb:
        return render_template("auth/loginform.html", form=form, error="No such username or password")

    if not bcrypt.check_password_hash(userfromdb.password, form.password.data):
        return render_template("auth/loginform.html", form=form, error="No such username or password")

    login_user(userfromdb)
    message = "You have logged in"
    return render_template("index.html", message=message)


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    message = "You have logged out"
    return render_template("index.html", message=message)
