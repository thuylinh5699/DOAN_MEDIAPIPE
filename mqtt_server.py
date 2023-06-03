import paho.mqtt.client as mqtt #import the client1
import time
import base64
import tkinter as tk
from tkinter import filedialog as fd


class MQTT_OPTIONS:
    broker_address="broker.hivemq.com"
    connect = False
    client = None
    timkiem = False
    dudoan_sv = 0
    dudoan_cli = None
    cli_duaradudoan = False
    vaophong = False
    def __init__(self) -> None:
        self.name = 'MQTT OPTIONS'  


mqtt_option = MQTT_OPTIONS

############
def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))
    topic = message.topic
    if msg == "conguoichoi" and topic == "btl/mtl/game/server/response" :
        mqtt_option.timkiem = True
        print('Tìm kiếm thành công, mời bạn vào phòng')
    elif topic == "btl/mtl/game/server/dudoan":
        mqtt_option.dudoan_cli = int(msg)
    elif topic == "btl/mtl/game/server/vaophong":
        print('vào phòng')
        mqtt_option.vaophong = True
        gui_vaophong()
        


mqtt_option.client = mqtt.Client("ID01-MAY1")
mqtt_option.client.on_message = on_message



def connect_mqtt():
    try:
        if mqtt_option.connect == False:
            mqtt_option.client.connect(mqtt_option.broker_address) #connect to broker
            mqtt_option.connect = True
            print('Kết nối máy chủ thành công')
            mqtt_option.client.loop_start() #start the loop
            # print("Subscribing to topic","house/bulbs/bulb1")
            mqtt_option.client.subscribe("btl/mtl/game/server/#")
            

    except:
        mqtt_option.connect = False
        print('Kết nối máy chủ thất bại')

def disconnect_mqtt():
    try:
        if mqtt_option.connect == True:
            mqtt_option.client.loop_stop()
            mqtt_option.connect = False
            print('Ngắt kết nối máy chủ thành công')
    except:
        pass
    
def timkiemnguoichoi():
    
    while True:
        try:
            if mqtt_option.connect == True:
                print('Đang tìm kiếm ...')
                mqtt_option.client.publish("btl/mtl/game/client/request","timkiemnguoichoi")
                time.sleep(1)
            if mqtt_option.timkiem == True or mqtt_option.connect == False:
                break
                
        except:
            pass
    
    
def guidudoan_to_cli(msg):
    if mqtt_option.connect == True:
        print('Đã gửi dự đoán sang client ...')
        mqtt_option.client.publish("btl/mtl/game/client/dudoan",msg)


def start_time_game():
    mqtt_option.client.publish("btl/mtl/game/client/start","start")
    
def gui_vaophong():
    mqtt_option.client.publish("btl/mtl/game/client/vaophong","ok")

def reset_scores():
    mqtt_option.client.publish("btl/mtl/game/client/resetscore","ok")
    