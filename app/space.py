from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from app.auth import login_required
from app.db import get_db

import random
from string import ascii_letters

bp = Blueprint("space", __name__, url_prefix="/spaces")


@bp.route("/")
def index():
    db = get_db()
    spaces = db.execute(
        "SELECT s.id, name, description, created, admin_id"
        " FROM spaces s JOIN users u ON s.admin_id = u.id"
        " ORDER BY created DESC"
    ).fetchall()
    spaces = [
        {
            "id": space["id"],
            "name": space["name"],
            "description": space["description"],
            "created": space["created"],
            "admin_id": space["admin_id"],
            "admin_name": db.execute(
                "SELECT username FROM users WHERE id = ?", (space["admin_id"],)
            ).fetchone()["username"],
            "members": get_space_member_ids(space["id"]),
        }
        for space in spaces
    ]
    return render_template("space/index.html", spaces=spaces)


def get_space_member_ids(space_id):
    db = get_db()
    members_cur = db.execute(
        "SELECT user_id FROM space_members WHERE space_id = ?", (space_id,)
    ).fetchall()
    member_ids = [member["user_id"] for member in members_cur]
    return member_ids


def get_space_members(space_id):
    db = get_db()
    return db.execute(
        "SELECT sm.joined, sm.user_id, u.id, u.username FROM space_members sm JOIN users u ON sm.user_id = u.id WHERE space_id = ? ORDER BY joined DESC",
        (space_id,),
    ).fetchall()


@bp.route("/create", methods=("GET", "POST"))
@login_required
def create():
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        error = None

        if not name:
            error = "Name is required."

        if not description:
            error = "Name is required."

        if error is not None:
            flash(error)
        else:
            code = generate_space_code(6)
            db = get_db()
            space_cur = db.execute(
                "INSERT INTO spaces (code, name, description, admin_id)"
                " VALUES (?, ?, ?, ?)",
                (code, name, description, g.user["id"]),
            )
            db.execute(
                "INSERT INTO space_members (space_id, user_id) VALUES (?, ?)",
                (space_cur.lastrowid, g.user["id"]),
            )
            db.commit()
            return redirect(url_for("space.index"))

    return render_template("space/create.html")


@bp.route("/<int:id>")
@login_required
def show(id):
    db = get_db()
    space = db.execute(
        "SELECT s.id, s.code, name, description, created, admin_id, username as admin_name"
        " FROM spaces s JOIN users u ON s.admin_id = u.id"
        " WHERE s.id = ?",
        (id,),
    ).fetchone()

    if space is None:
        abort(404, f"Space id {id} doesn't exist.")

    members = get_space_members(id)
    is_member = g.user["id"] in [member["user_id"] for member in members]
    if not is_member:
        abort(403, f"You are not a member of this space.")

    return render_template(
        "space/show.html", space=space, members=members, is_member=is_member
    )


@bp.route("/<int:id>/join", methods=["POST"])
@login_required
def join(id):
    db = get_db()
    db.execute(
        "INSERT INTO space_members (space_id, user_id)" " VALUES (?, ?)",
        (id, g.user["id"]),
    )
    db.commit()
    return redirect(url_for("space.show", id=id))


@bp.route("/<int:id>/leave", methods=["POST"])
@login_required
def leave(id):
    db = get_db()
    db.execute(
        "DELETE FROM space_members WHERE space_id = ? AND user_id = ?",
        (id, g.user["id"]),
    )
    db.commit()
    return redirect(url_for("space.index"))


@bp.route("/<int:id>/members/<int:user_id>/remove", methods=["DELETE"])
@login_required
def remove_member(id, user_id):
    db = get_db()
    db.execute(
        "DELETE FROM space_members WHERE space_id = ? AND user_id = ?",
        (id, user_id),
    )
    db.commit()
    return redirect(url_for("space.show", id=id))


# Generate a random space code
def generate_space_code(length: int) -> str:
    while True:
        code_chars = [random.choice(ascii_letters) for _ in range(length)]
        code = "".join(code_chars)
        existing_codes = "SELECT code FROM spaces"
        if code not in existing_codes:
            return code
