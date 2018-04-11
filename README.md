This project is aimed to help those who can not see. 


What is the project about?
The people who are blind, face day to day problem in several situations and always need some help and this makes them dependent on others. We are trying to reduce this dependency using current technology with the help of Machine Learning.

What are we doing?

1st part ->    We are using machine learning to make models with the help of neural network and these models are used to detect the objects in the live stream which is being fed by the help of a camera. 

2nd part-> As the model needs intense training there are chances of errors while detection. To reduce these errors and enhance the accuracy of the models, We next try to find any text in the live feed. There are chances that we might get a hint of the object in the image by looking through the texts around it.

3rd part -> Whatever is the object or text detected in the live feed is passed to the machine and the machine speaks out the object detected or the text found in the image to the user.

The repository consists of 3 python(.py) files:

1.  prototype.py
2.  ocr.py
3.  speak.py

1.prototype.py -> This is the script which calls the tenserflow model('ssd_mobilenet_v1_coco_11_06_2017') which has been trained for 100 class of objects. Note that, to this model was trained using around 335k images. It then calls the camera of the device and for this OpenCV has been used. The frame by frame image is passed to the model and the model tries to detect the class of an object and makes a box around the detected object along with the name of the class on it.

2. ocr.py -> This part of the program takes input an image and tries to find a text in it. If found, it displays the text. This uses the pytesseract module of python.

3. speak.py -> This part of the program speaks out the text or class of the object passed to it as an input. For this, we have used 'wincl' module of python

***** As the project is still going on, here we are providing a video of the working prototype of it https://www.youtube.com/watch?v=pmIAZmZlvVU       

***** Currently, We are trying to implement Natural Language Processing to enhance the work of the program while extracting text from the image.
Also, we are working to implement this on hardware devices using raspberry pi.

 Any kind of suggestions or flaws are most welcome 