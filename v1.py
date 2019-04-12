from PIL import Image
from matplotlib import pyplot as plt
from pytesseract import *
image_file='C:/Users/Vivek/Documents/UiPath/untitled folder/Scan0013.jpg'
im=Image.open(image_file)
text = image_to_string(image_file)
print ("=====output=======\n")
print (text)