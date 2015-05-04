from flask import Flask, render_template, request, flash, session, redirect, url_for
from datetime import datetime
from forms import ContactForm
from flask.ext.mail import Message, Mail

mail = Mail()


#from flaskapp import app as application

app = Flask(__name__, static_url_path='')

app.secret_key = 'ndapp development key'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'contact@neurodining.com'
app.config["MAIL_PASSWORD"] = 'NeuroDining'

mail.init_app(app)

#error message
@app.errorhandler(404)
def page_not_found(error):
    return "Sorry, this page was not found."

@app.route("/test")
def test():
    return "<strong>It's Alive!</strong>"

@app.route("/news")
def news():
    return render_template("news.html")

#service page
@app.route("/service")
def home():
	return render_template("service.html")


#contact page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            msg = Message("Request Membership", sender='contact@neurodining.com', recipients=['contact@neurodining.com'])
            msg.html = """
            From: %s <br>
            <br>
            Email: %s <br>
            <br>
            Phone: %s <br>
            <br>
            Message: %s
            """% (form.name.data, form.email.data, form.phone.data, form.message.data)
            mail.send(msg)
            return render_template('contact.html', success=True)
    elif request.method == 'GET':
        return render_template('contact.html', form=form)




#community page
@app.route("/community")
def community():
    return render_template("community.html")

#privacy policy page
@app.route("/privacypolicy")
def privacy():
    return render_template("privacy.html")


#about page
@app.route("/about")
def about():
    return render_template("about.html")


#home page
@app.route("/")
def homegrid():
    return render_template("homegrid.html")

#trying to improve home page
@app.route("/2")
def homegrid2():
    return render_template("homegrid2.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

#attempt at sign in page
@app.route("/signin")
def signin():
    return render_template("signin.html")


# learning to add js
@app.route("/js")
def java():
    return render_template("js_test.html")










if __name__ == "__main__":
	app.run()
