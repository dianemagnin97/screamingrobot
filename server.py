from flask import *
from gopigo import *
state = ""

app = Flask(__name__)
@app.route("/js/<path:path>")
def js(path, state=state):
    return send_from_directory("js", path)

@app.route("/")
def homepage(state=state):
    return render_template("ui.html")

@app.route("/left")
def leftRoute(state=state):
    if state == "left":
        return
    state = "left"
    left_rot()
    return "Moving Left"

@app.route("/right")
def rightRoute(state=state):
    if state == "right":
        return
    state = "right"
    right_rot()
    return "Moving Right"

@app.route("/bwd")
def bwdRoute(state=state):
    if state == "bwd":
        return
    state = "bwd"
    bwd()
    return "Moving Back"

@app.route("/fwd")
def fwdRoute(state=state):
    if state == "fwd":
        return
    state = "fwd"
    fwd()
    return "Moving forward"

@app.route("/stop")
def stopRoute(state=state):
    state = "stop"
    stop()
    return "Stopping"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
