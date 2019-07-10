"""
Routes and views for the flask application.
"""
from datetime import datetime
import os, base64, requests, sys
from flask import Flask, render_template, request, jsonify, json, send_file 
from python_webapp_flask import app
#from python_webapp_flask.image_compare import compare_images
from skimage.measure import compare_ssim
import imutils
import cv2
 

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/api/image_upload',methods=['GET','POST']) 
def get_images():
    if request.method =='GET':
        return render_template('imagediff.html')

    if request.method =='POST':
        try:
        #Receive the incoming data and split it into two image files
            imageData = json.loads(request.json)
            image1 = imageData['image1']
            image2 = imageData['image2']
        except Exception as ex:
            imageData = json.loads(request.data)
            image1 = imageData['image1']
            image2 = imageData['image2']
        
        try:
        #Read the image string and convert it into jpeg for the first image     
            ImageALocation = os.path.join('ImageA.jpg')
            with open(ImageALocation,"wb") as newFileA:
                newFileA.write(base64.b64decode(image1))
            newFileA.close()
                        

        #Read the image string and convert it into jpeg for the second image
            ImageBLocation = os.path.join('ImageB.jpg')       
            with open(ImageBLocation,"wb") as newFileB:
                newFileB.write(base64.b64decode(image2))
            newFileB.close()
            
        #Call the Image Compare function
            #result = compare_images(ImageALocation,ImageBLocation)
###########################################################################################################################
            imageA = cv2.imread(ImageALocation,-1)
            imageB = cv2.imread(ImageBLocation,-1)
            '''imageA = cv2.imread(ImageALocation,0)
            imageB = cv2.imread(ImageBLocation,0)'''
            grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
            grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY) 


# compute the Structural Similarity Index (SSIM) between the two
# images, ensuring that the difference image is returned
            (score, diff) = compare_ssim(grayA, grayB, full=True)
            diff = (diff * 255).astype("uint8")
            #print("SSIM: {}".format(score))
            strvar = format(score)
            if strvar == "1.0":
                result = strvar
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
                    ImageBLocation = os.path.join("Modified.jpg") 
                    cv2.imwrite(ImageBLocation, imageB)
                result = ImageBLocation
###############################################################################################################################


            if result == "1.0":
                return result
            else:
            

        #Open the result image and convert to base64 string for transmission
                with open(result,"rb") as resultFile:
                    data = base64.b64encode(resultFile.read())
                resultFile.close()

        
            #Package the image string in Json format and send back to caller
                jsonOut = str(data.decode())
                dump = json.dumps(jsonOut)
                load = json.loads(dump)
                return load
        except Exception as ex:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            jsonOut = {'ErrorMessage' : str(ex) + str(exc_type) + str(fname) + str(exc_tb.tb_lineno)}
            dump = json.dumps(jsonOut)
            load = json.loads(dump)
            return jsonify(load) 


if __name__ == '__main__':
   app.run(debug=True)
