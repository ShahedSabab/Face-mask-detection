# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 01:47:55 2020

@author: sabab
"""

# Importing the libraries
from PIL import Image
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from keras.preprocessing import image

#load the pretrained model
model = load_model('maskDetectionModel.h5')

# Loading the cascades to detect human faces
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def face_extractor(img):
    # Function detects faces and returns the cropped face
    # If no face detected, it returns the input image
    scale_factor = 1.05
    min_neighbour = 6
    faces = face_cascade.detectMultiScale(img, scale_factor, min_neighbour, minSize=(100, 100),
                                 flags=cv2.CASCADE_SCALE_IMAGE)
    
    if faces is ():
        return None
    # Crop all faces found
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        cropped_face = img[y:y+h, x:x+w]

    return cropped_face

# Doing some Face Recognition with the webcam
video_capture = cv2.VideoCapture(0)
while True:
    _, frame = video_capture.read()  
    face=face_extractor(frame)
    if type(face) is np.ndarray:
        
        #resize the image to match the pretrained model input
        face = cv2.resize(face, (224, 224))
        im = Image.fromarray(face, 'RGB')
        img_array = np.array(im)
        img_array = np.expand_dims(img_array, axis=0)
        
        # Use the model to predict
        pred = model.predict(img_array)
        print(pred[:,1])
        
        #Check the threshold
        if(pred[:,1] > 0.001):
            name='no mask found'
        else:
            name='mask found'
        cv2.putText(frame,name, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
    else:
        cv2.putText(frame,"No face found", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()

       

