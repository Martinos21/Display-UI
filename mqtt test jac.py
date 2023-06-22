import paho.mqtt.publish as publish
import time

mqtt_auth= { 'username': "mqtt", 'password': "1JAControls" }


while (True):
    publish.single("test", "test1", hostname="54.73.206.157", auth=mqtt_auth)
    print("published")
    time.sleep(10)