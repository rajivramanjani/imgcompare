# import the necessary packages
import os
from skimage.measure import compare_ssim
import imutils
import cv2
from python_webapp_flask import app

def compare_images(imageOne,imageTwo):
# load the two input images
    print(imageOne)
    
    imageA = cv2.imread(imageOne,-1)
    imageB = cv2.imread(imageTwo,-1)
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY) 


# compute the Structural Similarity Index (SSIM) between the two
# images, ensuring that the difference image is returned
    (score, diff) = compare_ssim(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    #print("SSIM: {}".format(score))
    floatvar = float(format(score))
    if floatvar == 1.0:
        return floatvar
    else:

# threshold the difference image, followed by finding contours to
# obtain the regions of the two input images that differ
        thresh = cv2.threshold(diff, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]

# loop over the contours
# compute the bounding box of the contour and then draw the
# bounding box on both input images to represent where the two
# images differ
        for c in cnts:
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)
    # show the output images
        #ImageCLocation = os.path.join("Diff.jpg")  
        #ImageDLocation = os.path.join("Thresh.jpg") 
            ImageBLocation = os.path.join("Modified.jpg") 
        #cv2.imwrite(ImageCLocation, diff)
        #cv2.imwrite(ImageDLocation, thresh)
            cv2.imwrite(ImageBLocation, imageB)
        return ImageBLocation