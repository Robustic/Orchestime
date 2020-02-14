from flask import redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user, current_user

from application import app, db, bcrypt, login_manager
from application.instrument.models import Instrument
from application.auth.models import User
from application.auth.forms import LoginForm, NewaccountForm, UpdateaccountForm


@app.route("/auth/new")
def auth_form():
    return render_template("auth/newaccountform.html", form=NewaccountForm())


@app.route("/auth", methods=["POST"])
def auth_create():
    form = NewaccountForm(request.form)
    if not form.validate():
        return render_template("auth/newaccountform.html", form=form)

    account = User(form.name.data, form.username.data, bcrypt.generate_password_hash(form.password.data).decode('utf-8'))
    db.session().add(account)
    db.session().commit()
    return redirect(url_for("auth_form"))


@app.route("/auth/<auth_id>/", methods=["GET"])
@login_required
def auth_view(auth_id):
    if int(auth_id) != current_user.id:
        return login_manager.unauthorized()
    account = User.query.get(auth_id)
    return render_template("auth/update.html", account=account,
                           instrument=Instrument.query.get(account.instrument_id), form=UpdateaccountForm())


@app.route("/auth/<auth_id>/update/", methods=["POST"])
@login_required
def auth_update(auth_id):
    if int(auth_id) != current_user.id:
        return login_manager.unauthorized()
    form = UpdateaccountForm(request.form)
    account = User.query.get(auth_id)
    form.instrument_id.data = int(form.instrument_id.data[0])
    if not form.validate():
        return render_template("auth/update.html", instrument=account, form=UpdateaccountForm())
    if len(form.name.data) > 1:
        account.name = form.name.data
    if form.instrument_id.data != 1:
        account.instrument_id = form.instrument_id.data
    db.session().commit()
    return redirect(url_for("index"))


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
    return redirect(url_for("index"))


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))  
