from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db
from application.instruments.models import Instrument
from application.instruments.forms import InstrumentForm


@app.route("/instruments", methods=["GET"])
def instruments_index():
    return render_template("instruments/list.html", instruments=Instrument.query.all())


@app.route("/instruments/new/")
@login_required
def instruments_form():
    return render_template("instruments/new.html", form=InstrumentForm())


@app.route("/instruments/<instrument_id>/delete/", methods=["POST"])
@login_required
def instruments_delete(instrument_id):
    instru = Instrument.query.get(instrument_id)
    db.session().delete(instru)
    db.session().commit()
    return redirect(url_for("instruments_index"))


@app.route("/instruments/<instrument_id>/", methods=["POST"])
@login_required
def instruments_update_name(instrument_id):
    instru = Instrument.query.get(instrument_id)
    instru.name = request.form.get("name")
    db.session().commit()  
    return redirect(url_for("instruments_index"))


@app.route("/instruments/", methods=["POST"])
@login_required
def instruments_create():
    form = InstrumentForm(request.form)
    if not form.validate():
        return render_template("instruments/new.html", form=form)
    
    instr = Instrument(form.name.data)
    db.session().add(instr)
    db.session().commit()
    return redirect(url_for("instruments_index"))
