from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/schedule")
def schedule():
    return render_template("schedule.html")

@app.route("/layout")
def layout():
    return render_template("layout.html")

app.run(debug=True)