from flask import redirect, render_template, request, url_for
from flask_login import login_user, logout_user

from application import app, db, bcrypt
from application.auth.models import User
from application.auth.forms import LoginForm
from application.auth.forms import NewaccountForm


@app.route("/auth/new")
def auth_form():
    return render_template("auth/newaccountform.html", form=NewaccountForm())


@app.route("/auth", methods=["POST"])
def auth_create():
    form = NewaccountForm(request.form)
    if not form.validate():
        return render_template("auth/newaccountform.html", form=form)

    account = User(form.name.data, form.username.data, bcrypt.generate_password_hash(form.password.data))
    db.session().add(account)
    db.session().commit()
    return redirect(url_for("auth_form"))


@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

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
