from flask import Flask, redirect, render_template, request, session
app = Flask(__name__)
app.secret_key = "swordfish"
@app.route("/")
def index():
    if not session.get("count"):
        session["count"] = 0
    session["count"] += 1
    return render_template("index.html", count=session["count"])
@app.route("/plus2", methods=["POST"])
def plus2():
    session["count"] += 1
    return redirect("/")
@app.route("/reset", methods=["POST"])
def reset():
    session["count"] = 0
    return redirect("/")
app.run(debug=True)