from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/skills")
def skills():
    return render_template("skills.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

