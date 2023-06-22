
import minimalmodbus

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
    print('Cannot connect to the Modbus Server/Slave')

