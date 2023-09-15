import serial.tools.list_ports

def list_serial_ports():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        print(f"Serial Port: {port.device}, Description: {port.description}")

list_serial_ports()
