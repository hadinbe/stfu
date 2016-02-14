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
BETA = 5

while True:
    
    # Let's keep it slow
    time.sleep(.05)

    table_x_idx = random.randint(0, 3)
    table_y_idx = random.randint(0, 1)

    x = 200 * (table_x_idx) + 150 + random.randint(-125, 125)
    y = 200 * (table_y_idx) + 150 + random.randint(-75, 75)
    value = int(100 * random.betavariate(ALPHA, BETA))

    # Correct value to avoid random positives
    value = min(70, value)

    r = requests.post(SERVER + ":" + str(PORT) + "/" + COLLECTION, data = {"x":x, "y":y, "value":value})
