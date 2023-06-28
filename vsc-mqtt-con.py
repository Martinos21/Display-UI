""""import minimalmodbus

instrument = minimalmodbus.Instrument('/dev/tty.usbserial-TM43O4GP', 1)  # port name, slave address (in decimal)

## Read temperature (PV = ProcessValue) ##
temperature = instrument.read_register(4)  # Registernumber, number of decimals
print(temperature)

from pymodbus.client.serial import ModbusSerialClient

client = ModbusSerialClient(
    method='rtu',
    port='COM3',
    baudrate=19200,
    timeout=3,
    parity='N',
    stopbits=1,
    bytesize=8
)

if client.connect():  # Trying for connect to Modbus Server/Slave
    '''Reading from a holding register with the below content.'''
    res = client.read_holding_registers(address=5, count=1, unit=1)
    
    '''Reading from a discrete register with the below content.'''
    # res = client.read_discrete_inputs(address=1, count=1, unit=1)

    if not res.isError():
        print(res.registers)
    else:
        print(res)

else:
    print('Cannot connect to the Modbus Server/Slave')"""


import paho.mqtt.client as mqtt 

def on_connect(client, userdata, flags, rc):
    # display connection infos; irrelevant for now
    # print("Connected with result code " + str(rc))

    # this works as well
    # client.subscribe([("home/misc/vacuum/sally/stat/battery",1), ("home/oben/schlafzimmer/open/fenster/open",2)])
    client.subscribe("status")
    client.subscribe("random")

def on_message(client, userdata, msg):
    # don't display like `b'payload'` 
    msg.payload = msg.payload.decode("utf-8")
  
    print (msg.payload)
    if msg.topic == "status":
        print(msg.payload)
    if msg.topic == "random":
        print(msg.payload)
    




        # print("Fenster Schlafzimmer ==> " + str(msg.payload))

# def on_message(client2, userdata, msg):
    # does this work?
    # print("Fenster Schlafzimmer: " + str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", 1883, 60)
#Set userid and password

client.loop_forever()




















