# Scrip description: This script let you get data from hardwware layer (temperatura 1 = DHT11 / 22, humedad = DHT11, Temperatura2 = LM35)

import serial
import time

arduino_port = 'COMX'
baud_rate = 9600

ser = serial.Serial(
    arduino_port,
    baud_rate,
    timeout=1
)

time.sleep(2)

while True:
    data = ser.readline().decode('utf-8').rstrip()
    print(data)