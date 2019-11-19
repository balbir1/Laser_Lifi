
#Python: Convert Image to String, Convert String to Image
#To store or transfer an image, we often need to convert an image to a string in such a way that the string represents the image. Like other programming languages (e.g. Java), we can also convert an image to a string representation in Python.
#Converting in Python is pretty straightforward, and the key part is using the "base64" module which provides standard data encoding an decoding.
#Convert Image to String
#Here is the code for converting an image to a string.

import base64
 
with open("lena.jpeg", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
    print (str)
	
f=open("strimg",'w+b')
f.write(str)
f.close()

with open ("strimg", "rb") as f1:
    data=f1.read()
    
fh = open("DedcodedImage.jpeg", "wb")
fh.write(base64.b64decode(data))

      


