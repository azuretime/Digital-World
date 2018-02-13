import RPi.GPIO as GPIO
from time import sleep
from firebase import firebase

url = "https://my-awesome-project-2fdd3.firebaseio.com//" # URL to Firebase database
token = "P6WgJAORwZYOtqNNz7PFtOB40fbhfSmCN3x0wj7z" # unique token used for authentication

# Create a firebase object by specifying the URL of the database and its secret token.
# The firebase object has functions put and get, that allows user to put data onto 
# the database and also retrieve data from the database.
firebase = firebase.FirebaseApplication(url, token)

# Use the BCM GPIO numbers as the numbering scheme
GPIO.setmode(GPIO.BCM)

# Use GPIO12, 16, 20 and 21 for the buttons.
buttons = {'ok': 12, 'rotate_ccw': 16, 'forward': 20, 'rotate_cw': 21}

# Set GPIO numbers in the list: [12, 16, 20, 21] as input with pull-down resistor.
GPIO.setup(buttons.values(), GPIO.IN, GPIO.PUD_DOWN)

# Keep a list of the expected movements that the eBot should perform sequentially.
movement_list = []

done = False

while not done:
    # Check each button to determine whether any of them has been pressed. If
    # the OK button is pressed, the program exits the while loop and writes the
    # movement_list to the Firebase database. If any of the directional buttons
    # are pressed, the commands should be stored in the movement_list.

    # Write your code here
     if GPIO.input(buttons['ok']) == GPIO.HIGH:
        done = True
        
     elif GPIO.input(buttons['rotate_ccw']) == GPIO.HIGH:
        movement_list.append('rotate_ccw')
        sleep(1)
     elif GPIO.input(buttons['forward']) == GPIO.HIGH:
        movement_list.append('forward')
        sleep(1)
     elif GPIO.input(buttons['rotate_cw']) == GPIO.HIGH:
        movement_list.append('rotate_cw')
        sleep(1)
     pass
firebase.put('/', 'movement_list',movement_list)


# Write to database once the OK button is pressed

