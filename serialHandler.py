import serial
import re
import numpy
stringSanitizer=re
serialConn=serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
    )

while True:
    incomingSerialData=serialConn.readline()
    if incomingSerialData:
        incomingSanitizedData=stringSanitizer.findall(r"[-+]?(?:\d*\.\d+|\d+)",incomingSerialData.decode("utf-8"))
        incomingSanitizedData=numpy.asarray(incomingSanitizedData,dtype=float)
        temp=incomingSanitizedData[1]
        hum=incomingSanitizedData[0]
        print('t:'+str(temp))
        print('h:'+str(hum))