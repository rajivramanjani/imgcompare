| Language | Framework | Platform | Author |
| -------- | -------- |--------|--------|
| Python | Flask | Azure Web App, Virtual Machine| |


# Python Flask web application

# Image Compare

  
  

![Our Application Logo](https://profiletestingserstorage.blob.core.windows.net/profiletesting/ImageA.JPG)

# Team

Jonathan Stonesifer and Rajiv Ramanjani worked together to develop this solution

# Problem

When we do automation testing : there is one part of it which involves doing a UI screen compare before the build and after the build.  The existing approach to do that compare is to do it manually.  

  

# Solution

Our solution uses a Python OpenCV computer vision solution that does an image compare automatically and spots the difference between the two screens. 

# Why it's cool

a. Using our solution would eliminate the manual comparison of images altogether and introduce an automated, quicker and more efficient way of comparing images and UI screens.
b. It can spot minute differences that might otherwise miss the eye of a normal person
c. The solution is delivered as an API service over the internet. 
d. Our solution does not require extensive processing capabilities or any additional expensive software or hardware.  Since the solution actually is made to reside on the internet as an API service - all processing happens on the internet - thus saving the user a lot of local processing needs
  

# Technologies and architecture used

� **Python OpenCV** is the core package used to highlight the differences between the images

**o Azure Notebooks** was used for essential code development of the Python code

**o Visual Studio** were used to build the code locally and later deploy it

  
  

**� Azure Cloud services** was used for hosting the solution

**o Python Flask WebApp** was created on Azure Cloud and hosted on an Ubuntu 16.04 Host
**o Azure DevOps** was used for Continuous Integration and Continuous Deployment of the Python-Flask application


  

**� Azure blob service** was used to upload images store them to create this readme file

  
# What your code was written in

a. **Python** was the main code base

b. **Flask** was the web framework on which the Python code was developed



# Open source or proprietary software used

Azure cloud services were extensively leveraged besides Visual Studio IDE

# What your code is designed for

Our code is designed to achieve the following:

a. In take two captured images and send it to the API service

b. Within the API service the image compare code executes and it highlights the differences between the two images

c. The API services returns a third image which highlights the differences and the spots in which the differences reside.

# Where would your code reside
Our main code would reside behind an API service.  However besides the core functionality - we would have a wrapper code that would have to be integrated into a testing framework. 

a. The testing framework has to take care of capturing the two images of the same screen (pre-build and post-build) and call the API service through the wrapper script.
b. The wrapper script would then call the API and return a third image with the differences in the image.  

# Underlying Flow

The underlying flow of the entire application is depicted here:

![enter image description here](https://profiletestingserstorage.blob.core.windows.net/profiletesting/Architecture3.JPG)

  


  



