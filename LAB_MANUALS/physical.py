import time
import serial.tools.list_ports

print("Sensors and Actuators")
# ls /dev/tty*
# def getPort():
#     ports = serial.tools.list_ports.comports()
#     commPort = None
#     for port in ports:
#         if "USB Serial Device" in port.description:
#             commPort = port.device
#     return commPort

# port = getPort()
# if port:
#     print(f"Found serial port: {port}")
# else:
#     print("Serial port not found.")
    
try:
    ser = serial.Serial(port="/dev/ttyUSB0", baudrate=9600)
except:
    print("Can not open the port")
    
# 0006000000FF
relay1_ON  = [0, 6, 0, 0, 0, 255, 200, 91]
# 000600000000
relay1_OFF = [0, 6, 0, 0, 0, 0, 136, 27]


# 0F06000000FFC8A4 -> 0F06000000FF -> A4C8 -> C8: 200, A4: 164
relay2_ON  = [15, 6, 0, 0, 0, 255, 200, 164]
# 0F060000000088E4 -> 0F0600000000 -> E488 -> 88: 136, E4: 228
relay2_OFF = [15, 6, 0, 0, 0, 0, 136, 228]

def setDevice1(state):
    if state == True:
        ser.write(relay1_ON)
    else:
        ser.write(relay1_OFF)
    time.sleep(1)
    print(serial_read_data(ser))
        
def setDevice2(state):
    if state == True:
        ser.write(relay2_ON)
    else:
        ser.write(relay2_OFF)
    time.sleep(1)
    print(serial_read_data(ser))
        
def serial_read_data(ser):
    bytesToRead = ser.inWaiting()
    if bytesToRead > 0:
        out = ser.read(bytesToRead)
        data_array = [b for b in out]
        print(data_array)
        if len(data_array) >= 7:
            array_size = len(data_array)
            value = data_array[array_size - 4] * 256 + data_array[array_size - 3]
            return value
        else:
            return -1
    return 0
        
# while True:
#     setDevice1(True)
#     setDevice2(True)
#     time.sleep(2)
#     setDevice1(False)
#     setDevice2(False)
#     time.sleep(2)

# [1, 3, 2, 10, 48, 190, 240]
# 10 * 256 + 48 -> Temerature = 2608 -> 26.08 °C
soil_temperature = [1,3,0,6,0,1,100,11]
def readTemperature():
    serial_read_data(ser)
    ser.write(soil_temperature)
    time.sleep(1)
    return serial_read_data(ser)

soil_moisture = [1,3,0,7,0,1,53,203]
def readMoisture():
    serial_read_data(ser)
    ser.write(soil_moisture)
    time.sleep(1)
    return serial_read_data(ser)
