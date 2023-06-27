import paho.mqtt.publish as publish
import psutil
import time
import os
from pymodbus.client import ModbusSerialClient as ModbusClient


client = ModbusClient(method='rtu', port='/dev/ttyUSB0',
                       baudrate=19200, parity="N", stopbits=1,  timeout=2)

client.connect()


"""read = client.write_coil(address=0x330, value=False, slave=1)"""
read = client.read_holding_registers(address=4, count=1, slave=1)

print(read.registers)

mqtt_auth= { 'username': "mqtt", 'password': "1JAControls" }

def get_system_status():
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    return cpu_percent, memory_percent, disk_usage


while (True):

    status = os.system('systemctl is-active --quiet ROXI_sniff.service')
    
    if status == 0:
        publish.single("roxi_sniff", "active", hostname="54.73.206.157", auth=mqtt_auth)
        print("active")
    else:
        publish.single("roxi_sniff", "nonactive", hostname="54.73.206.157", auth=mqtt_auth)
        print("nonactive") 
        break


    cpu_percent, memory_percent, disk_usage = get_system_status()

    if get_system_status():
        status = 'Online'
    else:
        status = 'Offline'
        break


    read = client.read_holding_registers(address=4, count=1, slave=1)
    ccu = "CCU-baud" + read.registers
    print(ccu)
    print(f"CPU vytížení: {cpu_percent}%")
    print(f"Využití paměti: {memory_percent}%")
    print(f"Využití disku: {disk_usage}%")
    print(f"Status OPI: {status}")

    publish.single("ccu-baud", cpu_percent, hostname="54.73.206.157", auth=mqtt_auth)
    publish.single("cpu-percent1", cpu_percent, hostname="54.73.206.157", auth=mqtt_auth)
    publish.single("memory-percent1", memory_percent, hostname="54.73.206.157", auth=mqtt_auth)
    publish.single("disk-usage1", disk_usage, hostname="54.73.206.157", auth=mqtt_auth)
    publish.single("OPI-status", status, hostname="54.73.206.157", auth=mqtt_auth)
    time.sleep(10)