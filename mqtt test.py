import paho.mqtt.publish as publish
import time


publish.single("testik", "payload", hostname="broker.hivemq.com")
time.sleep(5)


import paho.mqtt.subscribe as subscribe


msg = subscribe.simple("topic/sensorTemperature", hostname="broker.hivemq.com")
print("%s %s" % (msg.topic, msg.payload))
