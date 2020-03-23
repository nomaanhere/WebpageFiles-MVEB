import os
from time import sleep
from flask import Flask, render_template, request, Response, jsonify

app = Flask(__name__)

# Global variables definition and initialization
global panServoAngle
global tiltServoAngle
panServoAngle = 90
tiltServoAngle = 90

panPin = 27
tiltPin = 17

@app.route('/')
def index():
    """Video streaming home page."""
 
    templateData = {
      'panServoAngle'	: panServoAngle,
      'tiltServoAngle'	: tiltServoAngle
	}
    return render_template('index.html', **templateData)


@app.route('/<servo>/<angle>')
def move(servo, angle):
	global panServoAngle
	global tiltServoAngle
	if servo == 'pan':
		if angle == '+':
			panServoAngle = panServoAngle + 10
		else:
			panServoAngle = panServoAngle - 10
		os.system("python3 angleservoctrl.py " + str(panPin) + " " + str(panServoAngle))
	if servo == 'tilt':
		if angle == '+':
			tiltServoAngle = tiltServoAngle + 10
		else:
			tiltServoAngle = tiltServoAngle - 10
		os.system("python3 angleservoctrl.py " + str(tiltPin) + " " + str(tiltServoAngle))
	
	templateData = {
      'panServoAngle'	: panServoAngle,
      'tiltServoAngle'	: tiltServoAngle
	}
	return render_template('index.html', **templateData)
    
    
@app.route("/<direction>")
def webdrive(direction):
    os.system("python3 Motor_test.py " + str(direction) + " " + str(0.32))
    templateData = {
      'panServoAngle'	: panServoAngle,
      'tiltServoAngle'	: tiltServoAngle
	}
    return render_template('index.html', **templateData)	

	

if __name__ == '__main__':
    app.run(host='127.0.0.1', port =5000, debug=True, threaded=True)
