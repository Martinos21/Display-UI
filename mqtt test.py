import paho.mqtt.publish as publish
# import time


publish.single("topic/sensorTemperature", "payload", hostname="broker.hivemq.com")


import paho.mqtt.subscribe as subscribe


msg = subscribe.simple("topic/sensorTemperature", hostname="broker.hivemq.com")
print("%s %s" % (msg.topic, msg.payload))
