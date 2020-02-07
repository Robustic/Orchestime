from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db
from application.instrument.models import Instrument
from application.instrument.forms import InstrumentForm
from application.instrument.forms import InstrumentupdateForm


@app.route("/instrument", methods=["GET"])
def instruments_index():

    return render_template("instrument/list.html", instruments=Instrument.query.all())


@app.route("/instrument/new/")
@login_required
def instruments_form():
    return render_template("instrument/new.html", form=InstrumentForm())


@app.route("/instrument/<instrument_id>/delete/", methods=["POST"])
@login_required
def instruments_delete(instrument_id):
    instru = Instrument.query.get(instrument_id)
    db.session().delete(instru)
    db.session().commit()
    return redirect(url_for("instruments_index"))


@app.route("/instrument/<instrument_id>/", methods=["GET"])
def instrument_view(instrument_id):
    instru = Instrument.query.get(instrument_id)
    return render_template("instrument/update.html", instrument=instru, form=InstrumentupdateForm())


@app.route("/instrument/<instrument_id>/update/", methods=["POST"])
@login_required
def instrument_update(instrument_id):
    form = InstrumentupdateForm(request.form)
    instru = Instrument.query.get(instrument_id)
    if not form.validate():
        return render_template("instrument/update.html", instrument=instru, form=InstrumentupdateForm())

    instru.name = form.name.data
    db.session().commit()  
    return redirect(url_for("instruments_index"))


@app.route("/instrument/", methods=["POST"])
@login_required
def instruments_create():
    form = InstrumentForm(request.form)
    if not form.validate():
        return render_template("instrument/new.html", form=form)
    
    instr = Instrument(form.name.data)
    db.session().add(instr)
    db.session().commit()
    return redirect(url_for("instruments_index"))