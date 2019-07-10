"""
The flask application package.
"""

from flask import Flask, request, redirect, url_for
from os import environ
from applicationinsights.requests import WSGIApplication
from werkzeug.utils import secure_filename
#UPLOAD_FOLDER = "/app/python_webapp_flask/ImageCompare"
#UPLOAD_FOLDER = "/home/site/wwwroot"
app = Flask(__name__)
app.wsgi_app = WSGIApplication(environ.get('APPINSIGHTS_INSTRUMENTATIONKEY'), app.wsgi_app)
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#app.config['DEBUG'] = True 
import python_webapp_flask.views
from python_webapp_flask import app
#code below added by Rajiv
import base64
import os
from io import BytesIO
from skimage.measure import compare_ssim
from skimage.io import imsave
import cv2
import numpy
import requests
import Image
import matplotlib.pyplot as plt
from matplotlib import patches
import imutils




