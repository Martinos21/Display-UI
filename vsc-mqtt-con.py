import minimalmodbus

instrument = minimalmodbus.Instrument('/dev/tty.usbserial-TM43O4GP', 1)  # port name, slave address (in decimal)

## Read temperature (PV = ProcessValue) ##
temperature = instrument.read_register(4)  # Registernumber, number of decimals
print(temperature)