import random
import requests
import time

# Server config
SERVER = "http://127.0.0.1"
PORT = 5000
COLLECTION = "noise"

# Map dimension
COLS = 900
ROWS = 500

person_x = random.randint(0, COLS - 1)
person_y = random.randint(0, ROWS - 1)

while True:
    
    # Let's keep it slow
    time.sleep(.5)

    x = random.randint(person_x - 20, person_x + 20)
    y = random.randint(person_y - 20, person_y + 20)

    # Generate a vaue above 80 to trigger an alarm
    value = random.randint(80, 100)

    r = requests.post(SERVER + ":" + str(PORT) + "/" + COLLECTION, data = {"x":x, "y":y, "value":value})
