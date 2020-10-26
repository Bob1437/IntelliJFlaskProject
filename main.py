
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/page 1')
def home():

    return render_template("page 1.html")


@app.route("/Ideas")
def Ideas():
    return render_template("Ideas.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/other")
def other():
    return render_template("other.html")


if __name__ == "__main__":

    app.run(debug=True, port='3000', host='0.0.0.0')