import paho.mqtt.publish as publish
import psutil
import time


def get_system_status():
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    return cpu_percent, memory_percent, disk_usage


while (True):

    cpu_percent, memory_percent, disk_usage = get_system_status()

    if get_system_status():
        status = 'Online'
    else:
        status = 'Offline'

    print(f"CPU vytížení: {cpu_percent}%")
    print(f"Využití paměti: {memory_percent}%")
    print(f"Využití disku: {disk_usage}%")
    print(f"Status OPI: {status}")

    publish.single("cpu-percent1", cpu_percent, hostname="broker.hivemq.com")
    publish.single("memory-percent1", memory_percent, hostname="broker.hivemq.com")
    publish.single("disk-usage1", disk_usage, hostname="broker.hivemq.com")
    publish.single("OPI-status", status, hostname="broker.hivemq.com")
    time.sleep(10)