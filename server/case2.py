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

# Notification config
notification_sent = False
notification_timeout = 5
names = ['james', 'john', 'robert', 'michael', 'mary', 'william', 'david', 'richard', 'charles', 'joseph', 'thomas', 'patricia', 'christopher', 'linda', 'barbara', 'daniel', 'paul', 'mark', 'elizabeth', 'donald', 'jennifer', 'george', 'maria', 'kenneth', 'susan', 'steven', 'edward', 'margaret', 'brian', 'ronald', 'dorothy', 'anthony', 'lisa', 'kevin', 'nancy', 'karen', 'betty', 'helen', 'jason', 'matthew', 'gary', 'timothy', 'sandra', 'jose', 'larry', 'jeffrey', 'frank', 'donna', 'carol', 'ruth', 'scott', 'eric', 'stephen', 'andrew', 'sharon', 'michelle', 'laura', 'sarah', 'kimberly', 'deborah', 'jessica', 'raymond', 'shirley', 'cynthia', 'angela', 'melissa', 'brenda', 'amy', 'jerry', 'gregory', 'anna', 'joshua', 'virginia', 'rebecca', 'kathleen', 'dennis', 'pamela', 'martha', 'debra', 'amanda', 'walter', 'stephanie', 'willie', 'patrick', 'terry', 'carolyn', 'peter', 'christine', 'marie', 'janet', 'frances', 'catherine', 'harold', 'henry', 'douglas', 'joyce', 'ann', 'diane', 'alice', 'jean']

# Send notification out
def send_notification(x, y):

    user_idx = min(99, int(x * y * 100 / 900 / 500))

    r = requests.post(SERVER + ":" + str(PORT) + "/notification", data = {"username": names[user_idx]})


while True:
    
    # Let's keep it slow
    time.sleep(.5)

    x = random.randint(person_x - 20, person_x + 20)
    y = random.randint(person_y - 20, person_y + 20)

    # Generate a vaue above 80 to trigger an alarm
    value = random.randint(80, 100)

    r = requests.post(SERVER + ":" + str(PORT) + "/" + COLLECTION, data = {"x":x, "y":y, "value":value})

    if not notification_sent:
        if notification_timeout > 0:
            notification_timeout -= 1
        else:
            send_notification(person_x, person_y)
            notification_sent = True    
