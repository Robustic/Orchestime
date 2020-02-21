from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db, get_css_framework, ITEMS_PER_PAGE
from application.room.models import Room
from application.place.models import Place
from application.place.forms import PlaceForm
from application.place.forms import PlaceUpdateForm
from flask_paginate import Pagination, get_page_parameter


@app.route("/place", methods=["GET"])
def place_index():
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)

    total = Place.query.count()
    places = Place.query.order_by(Place.name)\
        .slice((page - 1) * ITEMS_PER_PAGE, page * ITEMS_PER_PAGE)
    pagination = Pagination(page=page, total=total, search=search, record_name='places', per_page=ITEMS_PER_PAGE,
                            css_framework=get_css_framework(), format_total=True, format_number=True)

    return render_template("place/list.html", places=places, pagination=pagination)


@app.route("/place/new/")
@login_required
def place_form():
    return render_template("place/new.html", form=PlaceForm())


@app.route("/place/<place_id>/delete/", methods=["POST"])
@login_required
def place_delete(place_id):
    place = Place.query.get(place_id)
    roomswithdeletedplace = Room.query.filter(Room.place_id == place_id).all()
    for room in roomswithdeletedplace:
        room.place_id = None
    db.session().delete(place)
    db.session().commit()
    return redirect(url_for("place_index"))


@app.route("/place/<place_id>/", methods=["GET"])
def place_view(place_id):
    place = Place.query.get(place_id)
    return render_template("place/update.html", place=place, form=PlaceUpdateForm())


@app.route("/place/<place_id>/update/", methods=["POST"])
@login_required
def place_update(place_id):
    form = PlaceUpdateForm(request.form)
    place = Place.query.get(place_id)
    if form.name.data == "":
        form.name.data = place.name
    if not form.validate():
        return render_template("place/update.html", place=place, form=PlaceUpdateForm())

    place.name = form.name.data
    if form.address.data != "":
        place.address = form.address.data
    db.session().commit()
    return redirect(url_for("place_index"))


@app.route("/place/", methods=["POST"])
@login_required
def place_create():
    form = PlaceForm(request.form)
    if not form.validate():
        return render_template("place/new.html", form=form)

    place = Place(form.name.data, form.address.data)
    db.session().add(place)
    db.session().commit()
    return redirect(url_for("place_index"))
