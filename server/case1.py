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

# Beta distribution parameters
ALPHA = 2
BETA = 10

while True:
    
    # Let's keep it slow
    time.sleep(.05)

    x = random.randint(0, COLS - 1)
    y = random.randint(0, ROWS - 1)
    value = int(100 * random.betavariate(ALPHA, BETA))

    # Correct value to avoid random positives
    value = min(70, value)

    r = requests.post(SERVER + ":" + str(PORT) + "/" + COLLECTION, data = {"x":x, "y":y, "value":value})
