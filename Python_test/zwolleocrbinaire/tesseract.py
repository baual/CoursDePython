# Reading Text from the Image using Tesseract
# https://www.geeksforgeeks.org/reading-text-from-the-image-using-tesseract/
#Last Updated: 30-08-2020
#Pytesseract or Python-tesseract is an Optical Character Recognition(OCR) tool for python. 
# It will read and recognize the text in images, license plates, etc. Here, we will use the tesseract package to read the text from the given image.


#Mainly, 3 simple steps are involved here as shown below: -

#Loading an Image saved from the computer or download it using a browser and then loading the same. (Any Image with Text).
#Binarizing the Image(Converting Image to Binary).
#We will then Pass the Image through the OCR system.
#Implementation:
#The following python code represents the Localizing of the Text and correctly guessing the text written in the image.



# We import the necessary packages 
#import the needed packages 
import cv2 
import os,argparse 
import pytesseract 
from PIL import Image 

#We then Construct an Argument Parser 
ap=argparse.ArgumentParser() 
ap.add_argument("-i","--image", 
				required=True, 
				help="Path to the image folder") 
ap.add_argument("-p","--pre_processor", 
				default="thresh", 
				help="the preprocessor usage") 
args=vars(ap.parse_args()) 

#We then read the image with text 
images=cv2.imread(args["image"]) 

#convert to grayscale image 
gray=cv2.cvtColor(images, cv2.COLOR_BGR2GRAY) 

#checking whether thresh or blur 
if args["pre_processor"]=="thresh": 
	cv2.threshold(gray, 0,255,cv2.THRESH_BINARY| cv2.THRESH_OTSU)[1] 
if args["pre_processor"]=="blur": 
	cv2.medianBlur(gray, 3) 
	
#memory usage with image i.e. adding image to memory 
filename = "{}.jpg".format(os.getpid()) 
cv2.imwrite(filename, gray) 
text = pytesseract.image_to_string(Image.open(filename)) 
os.remove(filename) 
print(text) 

# show the output images 
cv2.imshow("Image Input", images) 
cv2.imshow("Output In Grayscale", gray) 
cv2.waitKey(0) 


#Execute the command below to view the Output.
#python  tesseract.py - -image Images/title.png
