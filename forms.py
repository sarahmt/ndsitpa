from flask_wtf import Form
from wtforms import TextField, SubmitField, TextAreaField, validators
from wtforms.validators import InputRequired

class ContactForm(Form):
	name = TextField("Name", validators=[InputRequired('Please enter your name.')])
	email = TextField("E-mail", validators=[InputRequired('Please enter your email.'),validators.Email('Please enter a valid email address.')])
	phone = TextField("Phone", validators=[InputRequired('Please enter your phone.')])
	message = TextAreaField("Message")
	submit = SubmitField("Send")
