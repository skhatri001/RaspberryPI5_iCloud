from flask import Flask,Response,render_template
from selenium.webdriver.common.keys import Keys
import dropbox
import dropbox.files
import os
import time
import webbrowser
from threading import Timer
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
app = Flask(__name__)

def get_all_images():
	images = [img for img in os.listdir() if img.endswith(".jpg")]
	return images

def gen():
	i = 0
	
	while True:
		images = get_all_images()
		if not images:
			time.sleep(5)
			continue # Skip iteration if no images found
		image_name = images[i]
		im = open(image_name, 'rb').read()
		yield (b'--frame\r\n'
			b'Content-Type: image/jpeg\r\n\r\n' + im + b'\r\n')
		time.sleep(5)
		i = (i+1) % 2
		


#def hello_world():
#    return "<p>Hello world</p>"


@app.route("/")
def index():
	return "<html><head></head><body style='background-color:black;text-align:center';overflow:hidden;><h1>Photo Album</h1><img src='/slideshow' style='width: 720; height: 432; object-fit: cover;'/>" \
		"</body></html"
@app.route("/slideshow")
#def show_index():
#	full_filename = os.getcwd() + '/' +'IMG_0465.jpg'
#	return render_template("index.html", user_image = full_filename)
def slideshow():
	return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')

def open_browser():
	chrome_options = Options()
	chrome_options.add_experimental_option("detach",True)
	chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
#	chrome_options.add_argument("--no-sandbox")
#	chrome_options.add_argument("--disable-dev-shm-usage")
#	chrome_options.add_argument("--remote-debugging-port=9222")

	driver = webdriver.Chrome(options=chrome_options)
	#webbrowser.open_new("http://127.0.0.1:5000")
	driver.get("http://127.0.0.1:5000")
	#driver.find_element_by_xpath('/html/body').send_keys(Keys.F11)
	driver.fullscreen_window()
	os.system('xbanish')
	time.sleep(5)
	#port = 5000
	#url = "http://127.0.0.1:{0}".format(port)
	#chrome_path = '/usr/bin/chromium-browser --start-fullscreen '+url
	#os.system(chrome_path)
if __name__ == '__main__':
	# Open Chromium in full-screen mode

	#os.system('chromium-browser http://127.0.0.1:5000 --start-fullscreen')
	#os.system(chrome_path)
	#open_browser()
	#time.sleep(1)
	#print(os.getcwd())
	Timer(1,open_browser).start()
	#os.system('chromium-browser --start-maximized')
	#time.sleep(5)
	#os.system('sleep 5')
	#os.system('xdotool key F11')
	#webbrowser.get('chromium').open_new('http://localhost:5000 --start-fullscreen')
	app.run(debug=True)

