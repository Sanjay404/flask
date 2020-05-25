from flask import Flask, render_template
'''
makes a variable called 'app' that is the 
source of this web app so i can tie differnt web functions or routesto it
'''
app = Flask(__name__)  
'''
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

@app.route("/<string:name>") 
def general(name):
    return (f"<h1>hi {name}</h1>")

if __name__ == '__main__':
    app.run(debug=True)