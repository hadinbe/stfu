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

table_x_idx = random.randint(0, 3)
table_y_idx = random.randint(0, 1)

person_x = 200 * (table_x_idx) + 150
person_y = 200 * (table_y_idx) + 150

# Notification config
notification_sent = False
notification_timeout = 5
names = ['james', 'robert', 'michael', 'mary', 'linda', 'barbara', 'alice', 'jean']

# Send notification out
def send_notification(x, y):

    user_idx = table_x_idx + 4 * table_y_idx *  #(table_x_idx + 1) * (table_y_idx + 1) - 1

    r = requests.post(SERVER + ":" + str(PORT) + "/notification", data = {"username": names[user_idx]})

    send_notification_to_spark(names[user_idx])


def send_notification_to_spark(username):
    MESSAGES_URL = "https://api.ciscospark.com/v1/messages"
    HEADER = {"Authorization":"Bearer MTcwNDUwMjUtMTY5NS00OGZlLTg3MWYtOTNkYmYyMjFhOGQ4MjZlNzBhZDAtZDQz"}

    # data = { 
    #   "roomId": "89a67ed0-d307-11e5-88f7-3b8564d072cc",
    #   "text": "Shut the f**k up!"
    #   }
    data = { 
        "toPersonEmail": "michael.kaserer@hotmail.com",
        "text": "Shut the f**k up, " + username + "!"
        }
    req = requests.post(MESSAGES_URL, data=data, headers=HEADER)


while True:
    
    # Let's keep it slow
    time.sleep(.5)

    x = random.randint(person_x - 75, person_x + 75)
    y = random.randint(person_y - 35, person_y + 35)

    # Generate a vaue above 80 to trigger an alarm
    value = random.randint(80, 100)

    r = requests.post(SERVER + ":" + str(PORT) + "/" + COLLECTION, data = {"x":x, "y":y, "value":value})

    if not notification_sent:
        if notification_timeout > 0:
            notification_timeout -= 1
        else:
            send_notification(person_x, person_y)
            notification_sent = True    
