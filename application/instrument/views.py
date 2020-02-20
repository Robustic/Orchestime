from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db, get_css_framework, ITEMS_PER_PAGE
from application.instrument.models import Instrument
from application.instrument.forms import InstrumentForm
from application.instrument.forms import InstrumentupdateForm
from application.auth.models import User
from flask_paginate import Pagination, get_page_parameter


@app.route("/instrument", methods=["GET"])
def instruments_index():
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)

    total = Instrument.query.count()
    instruments = Instrument.query.order_by(Instrument.name)\
        .slice((page - 1) * ITEMS_PER_PAGE, page * ITEMS_PER_PAGE)
    pagination = Pagination(page=page, total=total, search=search, record_name='instruments', per_page=ITEMS_PER_PAGE,
                            css_framework=get_css_framework(), format_total=True, format_number=True)

    return render_template("instrument/list.html", instruments=instruments, pagination=pagination)


@app.route("/instrument/new/")
@login_required
def instruments_form():
    return render_template("instrument/new.html", form=InstrumentForm())


@app.route("/instrument/<instrument_id>/delete/", methods=["POST"])
@login_required
def instruments_delete(instrument_id):
    instrument = Instrument.query.get(instrument_id)
    userswithdeletedinstrument = User.query.filter(User.instrument_id == instrument_id).all()
    for user in userswithdeletedinstrument:
        user.instrument_id = None
    db.session().delete(instrument)
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

    if form.name.data != "":
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
