import serial
import time
# pip install pyserial

ser = serial.Serial('COM4', 9600)

while True:
    if ser.readable():
        inp = input()
        ser.write(inp.encode('utf-8'))
        print(inp)

