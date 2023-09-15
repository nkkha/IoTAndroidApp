import sys
from Adafruit_IO import MQTTClient
import time
import random
# from simple_ai import *
# from uart import *
from physical import *

AIO_FEED_IDS = ["nutnhan1","nutnhan2"]
AIO_USERNAME = "nkkha"
AIO_KEY = "aio_jRkU73Nm9px7stkImEiFt92udZtw"

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDS:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + " , feed id: " + feed_id)
    if feed_id == "nutnhan1":
        # if payload == "0":
        #     writeData(1)
        # else:
        #     writeData(2)
        setDevice1(payload == "1")
    elif feed_id == "nutnhan2":
        # if payload == "0":
        #     writeData(3)
        # else:
        #     writeData(4)
        setDevice2(payload == "1")
            
            
client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

counter = 10
counter_ai = 5
sensor_type = 0
previous_result = ""

while True:
    # counter -= 1
    # if counter <= 0:
    #     counter = 10
    #     #TODO
    #     print("Random data is publishing...")
    #     if sensor_type == 0:
    #         print("Temperature...")
    #         temp = random.randint(10, 20)
    #         client.publish("cambien1", temp)
    #         sensor_type = 1
    #     elif sensor_type == 1:
    #         print("Humidity...")
    #         humi = random.randint(50, 70)
    #         client.publish("cambien3", humi)
    #         sensor_type = 2
    #     elif sensor_type == 2:
    #         print("Light...")
    #         light = random.randint(100, 500)
    #         client.publish("cambien2", light)
    #         sensor_type = 0

    # counter_ai -= 1
    # if counter_ai <= 0:
    #     counter_ai = 5
    #     ai_result, image = image_detector()
    #     if previous_result != ai_result:
    #         previous_result = ai_result
    #         print("AI Output: ")
    #         client.publish("ai", ai_result)
    #         client.publish("image", image)

    # readSerial(client)
    
    temp = readTemperature()
    mois = readMoisture()
    print("Nhiet do: " + str(temp / 100) + "°C")
    print("Do am: " + str(mois) + "%")
    client.publish("cambien1", temp / 100)
    client.publish("cambien3", mois)

    time.sleep(1)
    pass