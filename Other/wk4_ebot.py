from eBot import eBot
from time import sleep
from firebase import firebase

url = "https://my-awesome-project-2fdd3.firebaseio.com/"  # URL to Firebase database
token = "P6WgJAORwZYOtqNNz7PFtOB40fbhfSmCN3x0wj7z"  # unique token used for authentication

# Create a firebase object by specifying the URL of the database and its secret token.
# The firebase object has functions put and get, that allows user to put data onto 
# the database and also retrieve data from the database.
firebase = firebase.FirebaseApplication(url, token)

ebot = eBot.eBot() # create an eBot object
ebot.connect() # connect to the eBot via Bluetooth

# Use a variable to determine whether there is any valid movement commands in
# the Firebase database.
no_commands = True

while no_commands == True:
    # Check the value of movement_list in the database at an interval of 0.5
    # seconds. Continue checking as long as the movement_list is not in the
    # database (ie. it is None). If movement_list is a valid list, the program
    # exits the while loop and controls the eBot to perform the movements
    # specified in the movement_list in sequential order. Each movement in the
    # list lasts exactly 1 second.
    
    # Get movement list from Firebase
    movement_list = firebase.get('/movement_list')
    for i in range(len(movement_list)):
        movement_list[i] = str(movement_list[i])
        if movement_list[i] != '0':
            no_commands = False
        else:
            no_commands = True
    sleep(0.5)

# Write the code to control the eBot here

def forward(speed, duration):
    ebot.wheels(speed, speed)
    sleep(duration)
    pass

def rotate_cw(speed, duration):
    ebot.wheels(1*speed, -1*speed)
    sleep(duration)
    pass

def rotate_ccw(speed, duration):
    ebot.wheels(-1*speed, 1*speed)
    sleep(duration)
    pass

for i in range(len(movement_list)):
    if movement_list[i] == 'forward':
        forward(1, 1)
    elif movement_list[i] == 'rotate_cw':
        rotate_cw(1, 1)
    elif movement_list[i] == 'rotate_ccw':
        rotate_ccw(1, 1)
    
print movement_list
movement_list = ['0']
firebase.put('/', 'movement_list', movement_list)
ebot.disconnect() # disconnect the Bluetooth communication
