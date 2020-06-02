from flask import Flask, render_template, request, redirect, url_for
'''
makes a variable called 'app' that is the 
source of this web app so i can tie differnt web functions or routesto it
'''
app = Flask(__name__)
'''
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key",
    MAIL_SERVER = "localhost",
    MAIL_PORT = 25,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'srikumar.sanjay@gmail.com',
    MAIL_PASSWORD = 'blaster1',
))

def send_email(to_email,from_email,mydict):
  result_dict = {}
  try:
      msg = Message("Message from your website",sender=from_email,recipients=[to_email])
      msg.body="Email from your website"
      msg.html= render_template("email.html",contact_email=mydict['contact_email'],message=mydict['message'])
      mail.send(msg)
      flash("Thanks for contacting me. I will get back to you soon!","success")
  except Exception as e:
      flash("Error sending email".format(str(e)),"error")

________________________________________________________________________________
NOTES:
routes '/' (which is essentially the landing page)
________________________________________________________________________________
Can pass additional arguments to render_template
EX: 
temp= "hi"
render_template("index.html", temp) 
IN HTML, I use {{temp}}
'''
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Resume")
def resume():
    return redirect("https://thinfi.com/nerq")

@app.route("/<string:name>")
def general(name):
    return ("<h1>This Page Does Not Exist</h1>")

@app.route("/about")
def about():
    return render_template("about_me.html")

@app.route("/Projects")
def projects():
    return render_template("projects.html")
@app.route("/Contact")
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)
