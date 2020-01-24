from application import app, db
from flask import redirect, render_template, request, url_for
from application.instruments.models import Instrument

@app.route("/instruments", methods=["GET"])
def instruments_index():
    return render_template("instruments/list.html", instruments = Instrument.query.all())

@app.route("/instruments/new/")
def instruments_form():
    return render_template("instruments/new.html")

@app.route("/instruments/<instrument_id>/delete/", methods=["POST"])
def instruments_delete(instrument_id):
    instru = Instrument.query.get(instrument_id)
    db.session().delete(instru)
    db.session().commit()
    return redirect(url_for("instruments_index"))
    
@app.route("/instruments/<instrument_id>/", methods=["POST"])
def instruments_update_name(instrument_id):
    instru = Instrument.query.get(instrument_id)
    instru.name = request.form.get("name")
    db.session().commit()  
    return redirect(url_for("instruments_index"))

@app.route("/instruments/", methods=["POST"])
def instruments_create():
    instr = Instrument(request.form.get("name"))
    db.session().add(instr)
    db.session().commit()
    return redirect(url_for("instruments_index"))
