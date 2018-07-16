Let Me See
This project is aimed to help those who can not see. 

Objectives of app: 1)Object detection 2)Text detection 3)Text-To-Speech

1.prototype.py -> This is the script which calls the tenserflow model('ssd_mobilenet_v1_coco_11_06_2017') which has been trained for 100 class of objects. This model was trained using around 335k images. It then calls the camera of the device and for this OpenCV has been used.

2. ocr.py -> This part of the program takes input an image and tries to find a text in it then displays the text. This uses the pytesseract module of python.

3. speak.py -> This part of the program speaks out the text or class of the object passed to it as an input. For this, we have used 'wincl' module of python

video of the working prototype:https://www.youtube.com/watch?v=pmIAZmZlvVU       

