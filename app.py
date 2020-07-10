from flask import Flask, render_template, request, redirect, url_for, send_from_directory

from werkzeug import secure_filename
import numpy as np
import cv2
import animal
from PIL import Image
import os
'''
makes a variable called 'app' that is the
source of this web app so i can tie differnt web functions or routesto it
'''
app = Flask(__name__)
'''
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
    return redirect("https://www.terpconnect.umd.edu/~sanjays/Personal-Website%20Externals/Sanjay_Srikumar_Resume.pdf")

@app.route("/<string:name>")
def general(name):
    return ("<h1>This Page Does Not Exist</h1>")

@app.route("/about")
def about():
    return render_template("about_me.html")

@app.route("/Projects")
def projects():
    return render_template("Projects.html")
@app.route("/Contact")
def contact():
    return render_template("contact.html")

UPLOAD_FOLDER = '/Users/sanjay/Desktop/temp'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route('/Animal')
def upload_file():
   return render_template('upload.html')


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_files():
   if request.method == 'POST':
       # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        file = request.files['file']
        if file and allowed_file(file.filename):
            
            filename = secure_filename(file.filename) #string name of file
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            predictions = []
            files = []
            images = Image.open(file)
            images = np.array(images)
            shape = (128,128)
            images = cv2.resize(images,(shape[0],shape[1]))
            images = cv2.cvtColor(np.array(images), cv2.COLOR_BGR2RGB)
            filename = 'http://127.0.0.1:5000/uploads/' + filename
            predictions.append(animal.predict(images))
            files.append(filename)
            print()
            print()
            print()
            print()
            
            ret = {filename : predictions}
            print()
            print()
            print()
            print()
            print(list(zip(*ret)))
            return render_template('display_imgs.html', iterate = ret) 
            #return render_template('display_imgs.html', images = url_for('upload_file', filename=filename), predictions= predictions)
        return render_template('upload.html')


@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)