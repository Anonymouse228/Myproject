import time
import random
import json


def number_generation():
    number = '+375' + random.choice(('29', '33'))
    for i in range(7):
        number += str(random.randint(0, 9))
    return number


def call_data():
    call = {
        'FromNum': number_generation(),
        'ToNum': number_generation(),
        'Start': int(time.time()) - random.randint(20, 600),
        'Finish': int(time.time()),
        'CallType': random.choice(('LTE', 'GSM', 'CDMA'))
    }
    return call


def save(a):
    filename = 'Call' + str(a) + '.json'
    with open(filename, "w") as f:
        json.dump(call_data(), f)


a = 1
while True:
    time.sleep(random.randint(1, 5))
    save(a)
    a += 1
