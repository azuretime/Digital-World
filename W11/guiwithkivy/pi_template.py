from RPi import GPIO
from firebase import firebase

url = "https://my-awesome-project-2fdd3.firebaseio.com//" 
token = "P6WgJAORwZYOtqNNz7PFtOB40fbhfSmCN3x0wj7z"

firebase=firebase.FirebaseApplication(url,token)

GPIO.setmode(GPIO.BCM)
ledcolor={'yellow':20, 'red':21}

GPIO.setup(ledcolor.values(), GPIO.OUT)

def setLED(ledno, status):
	# you can use this to set the LED on or off
	pass

while True:
	# get firebase data and call setLED
    pass
