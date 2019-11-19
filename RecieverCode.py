import base64
import serial

ser=serial.Serial("/dev/ttyAMA0",9600)
f=open("lena.txt",'w+b')

try:
    with open("lena.txt",'w+b') as f:
        while True:
            data=ser.read()
            f.write(data)
            print(data)
                    
except KeyboardInterrupt:
    f.close()
    
    with open("lena.txt", "rb") as f1:
        dataImg=f1.read()
    f2=open("lenaRx.jpeg", "wb")
    f2.write(base64.b64decode(dataImg))
    ser.close()
    print ('program exited')
    

