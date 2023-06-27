import paho.mqtt.subscribe as subscribe
import time

mqtt_auth= { 'username': "mqtt", 'password': "1JAControls" }


while (True):
    msg = subscribe.simple("testik", hostname="broker.hivemq.com")
    print("%s %s" % (msg.topic, msg.payload))
    break

msg = msg.payload