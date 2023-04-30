from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditor


app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)



class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods = ["GET", "POST"])
def contact():
    form = MyForm()
    return render_template("contact.html", form=form)

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/skills")
def skills():
    return render_template("skills.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

