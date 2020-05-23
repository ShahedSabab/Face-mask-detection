# Mask Detection
Many measurements have been taken to tackle the COVID-19 pandemic. Among which wearing mask is one way to prevent spreading the virus. The aim of this work is to detect if a person is wearing a mask or not. With this objective, a machine learning model is developed which leverages transfer learning to detect mask. The training data for this model is collected from multiple sources. <br>

For collecting human faces with mask, a subset (i.e.,1000 images) of the MAFA dataset (can be found in http://www.escience.cn/people/geshiming/mafa.html) is used. For collecting human faces without mask, a subset of (1000 images) the UTKFace dataset (can be found in https://susanqq.github.io/UTKFace/) is used.

• Keras is used to develop the model. <br>
• Resnet-50 is used to train the model. <br>
• Data augmentation (horizontal and vertical shift, flip) is performed as a preprocessing step. <br>
• 99% accuracy is achieved while testing with hold-out images. <br>

# How to run:
To use the saved model check "maskDetectionModel.h5" file. For code and performance, check the maskDetection.ipynb file.
