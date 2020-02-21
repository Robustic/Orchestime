from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db, get_css_framework, ITEMS_PER_PAGE
from application.room.models import Room
from application.room.forms import RoomForm
from application.room.forms import RoomUpdateForm
from application.place.models import Place
from application.event.models import Event
from flask_paginate import Pagination, get_page_parameter


@app.route("/room", methods=["GET"])
def room_index():
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)

    total = Room.query.count()
    rooms = Room.query.join(Place, isouter=True).order_by(Place.name, Room.name)\
        .slice((page - 1) * ITEMS_PER_PAGE, page * ITEMS_PER_PAGE)
    pagination = Pagination(page=page, total=total, search=search, record_name='rooms', per_page=ITEMS_PER_PAGE,
                            css_framework=get_css_framework(), format_total=True, format_number=True)

    return render_template("room/list.html", rooms=rooms, pagination=pagination)


@app.route("/room/new/")
@login_required
def room_form():
    return render_template("room/new.html", form=RoomForm(), places=Place.query.order_by(Place.name).all())


@app.route("/room/<room_id>/delete/", methods=["POST"])
@login_required
def room_delete(room_id):
    room = Room.query.get(room_id)
    eventswithdeletedroom = Event.query.filter(Event.room_id == room_id).all()
    for event in eventswithdeletedroom:
        event.room_id = None
    db.session().delete(room)
    db.session().commit()
    return redirect(url_for("room_index"))


@app.route("/room/<room_id>/", methods=["GET"])
def room_view(room_id):
    room = Room.query.get(room_id)
    return render_template("room/update.html", room=room, form=RoomUpdateForm(),
                           places=Place.query.order_by(Place.name).all(),
                           oldplace=Place.query.get(room.place_id))


@app.route("/room/<room_id>/update/", methods=["POST"])
@login_required
def room_update(room_id):
    place_id = request.form.get('place_id')
    form = RoomUpdateForm(request.form)
    room = Room.query.get(room_id)
    if form.name.data == "":
        form.name.data = room.name
    if not form.validate():
        return render_template("room/update.html", room=room, form=RoomUpdateForm(),
                               places=Place.query.order_by(Place.name).all(),
                               oldplace=Place.query.get(room.place_id))

    room.name = form.name.data
    if place_id:
        room.place_id = place_id
    db.session().commit()
    return redirect(url_for("room_index"))


@app.route("/room/", methods=["POST"])
@login_required
def room_create():
    place_id = request.form.get('place_id')
    form = RoomForm(request.form)
    if not form.validate():
        return render_template("room/new.html", form=RoomForm(), places=Place.query.order_by(Place.name).all())

    room = Room(form.name.data)
    if place_id:
        room.place_id = place_id
    db.session().add(room)
    db.session().commit()
    return redirect(url_for("room_index"))
