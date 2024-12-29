from flask import Flask,Response,render_template
import dropbox
import dropbox.files
import os
import time



app = Flask(__name__)

def get_all_images():
	images = [img for img in os.listdir() if img.endswith(".jpg")]
	return images

def gen():
	i = 0
	
	while True:
		images = get_all_images()
		image_name = images[i]
		im = open(image_name, 'rb').read()
		yield (b'--frame\r\n'
			b'Content-Type: image/jpeg\r\n\r\n' + im + b'\r\n')
		i+=1
		if i>=len(images):
			i=0
		time.sleep(5)


def hello_world():
    return "<p>Hello world</p>"


@app.route("/")
def index():
	return "<html><head></head><body style='background-color:black;text-align:center'><h1>Photo Album</h1><img src='/slideshow' style='width: 192; height: 256; object-fit: cover;'/>" \
		"</body></html>"
@app.route("/slideshow")
#def show_index():
#	full_filename = os.getcwd() + '/' +'IMG_0465.jpg'
#	return render_template("index.html", user_image = full_filename)
def slideshow():
	return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
	app.run(host = '0.0.0.0',debug = True)


