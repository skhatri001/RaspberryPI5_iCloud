from flask import Flask, render_template
import dropbox
import dropbox.files
import os



app = Flask(__name__)

def hello_world():
    return "<p>Hello world</p>"


@app.route("/")
@app.route("/index")
def show_index():
	full_filename = os.getcwd() + '/' +'IMG_0465.jpg'
	return render_template("index.html", user_image = full_filename)


