import os

from flask import Flask, session, render_template
from flask_socketio import SocketIO, join_room, leave_room, send

# A mock database to persist data
rooms = {}


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "social.db"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route("/about")
    def about():
        return render_template("about.html")

    socketio = SocketIO(app)

    # SocketIO event handlers
    @socketio.on("connect")
    def handle_connect():
        name = session.get("name")
        room = session.get("room")
        if name is None or room is None:
            return
        if room not in rooms:
            leave_room(room)
        join_room(room)
        send({"sender": "", "message": f"@{name} has entered the chat"}, to=room)
        rooms[room]["members"] += 1

    @socketio.on("message")
    def handle_message(payload):
        room = session.get("room")
        name = session.get("name")
        if room not in rooms:
            return
        message = {"sender": name, "message": payload["message"]}
        send(message, to=room)
        rooms[room]["messages"].append(message)

    @socketio.on("disconnect")
    def handle_disconnect():
        room = session.get("room")
        name = session.get("name")
        leave_room(room)
        if room in rooms:
            rooms[room]["members"] -= 1
            if rooms[room]["members"] <= 0:
                del rooms[room]
            send({"message": f"@{name} has left the chat", "sender": ""}, to=room)

    if __name__ == "__main__":
        socketio.run(app, debug=True)

    from . import db

    db.init_app(app)

    from . import auth

    app.register_blueprint(auth.bp)

    from . import blog

    app.register_blueprint(blog.bp)
    app.add_url_rule("/", endpoint="index")

    from . import space

    app.register_blueprint(space.bp)

    return app
