
import serial 
s = serial.Serial("/dev/ttyUSB0",20000)
#s.write()
s.write(open("strimg","rb").read())
s.close()


