FROM ubuntu:16.04
LABEL maintainer="Azure App Service Container Images <appsvc-images@microsoft.com>"
# ####     INSTALL ESSENTIAL LIBRARIES          ##########
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y python-dev
RUN apt-get install -y pkg-config
# ####     UPGRADE TO THE LATEST VERSION OF PIP USING THE get-pip.py COMMAND #####
RUN apt-get install -y wget
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py
# ####     INSTALL THE SCIKIT IMAGE PACKAGE #########
RUN pip install -U scikit-image
# ####     LINE ADDED TO INSTALL SKIMAGE PACKAGE  ######
RUN apt-get install -y python-skimage
# ####    LINES ADDED TO INSTALL THE OPENCV PACKAGE    ##########
RUN pip install opencv-python==3.4.3.18
# ####   STANDARD LINES TO EXECUTE THE REQUIREMENTS FILE  #######
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
EXPOSE 5000
CMD ["runserver.py"]