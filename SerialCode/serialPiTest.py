import serial

# Example Usage
'''
import serialPi
serialPi.initSerial()
serialPi.write("Go")
serialPi.write("Stop")
'''

def initSerial():
	global s1
	s1 = serial.Serial('COM6', 115200)
	s1.flushInput()

#comp_list = [b"Flash Complete\r\n", b"Hello Pi, this is arduino UNO...\r\n"]

def write(self, code)
    s1.write(str.encode(code))

