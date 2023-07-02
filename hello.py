from flask import Flask, render_template,flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = "my super secret key that no one is supposed to know"

db = SQLAlchemy(app)
app.app_context().push()

class Users(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), nullable=False, unique=True)
	name = db.Column(db.String(200), nullable=False)
	email = db.Column(db.String(120), nullable=False, unique=True)
	date_added = db.Column(db.DateTime, default=datetime.utcnow)
	with app.app_context():
		db.create_all()
	
def __repr__(self):
		return '<Name %r>' % self.name

class UserForm(FlaskForm):
	name = StringField("Name", validators=[DataRequired()])
	email = StringField("Email", validators=[DataRequired()])
	submit = SubmitField("Submit")
	
class NamerForm(FlaskForm):
	name= StringField("What's Your Name", validators=[DataRequired()])
	submit = SubmitField("Submit")
	

#def index():
#	return "<h1>Hello World!</h1>"

# FILTERS!!!
#safe
#capitalize
#lower
#upper
#title
#trim
#striptags
@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
	form = UserForm()
	
	return render_template("add_user.html", 
		form=form,)


@app.route('/')
def index():
	first_name = "AyushOnTwitter"
	stuff = "This is bold text"
	flash("welcome to our website")

	Website_features = ["Add name", "Add friends", "Tweets", "Edit" , "Upload"]
	return render_template("index.html", 
		first_name=first_name,
		stuff=stuff,
		Website_features = Website_features)

@app.route('/user/<name>')

def user(name):
	return render_template("user.html", user_name=name)

# Create Custom Error Pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500

@app.route('/name', methods=['GET', 'POST'])
def name():
	name = None
	form = NamerForm()
	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''
		flash("Form Submitted Successfully!")
		
	return render_template("name.html", 
		name = name,
		form = form)

