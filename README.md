# Mask Detection
Many measurements have been taken to tackle the COVID-19 pandemic. Among which wearing mask is one way to prevent spreading the virus. The aim of this work is to detect if a preson is wearing a mask or not. With this objective, a machine laerning model is developed which leverages transfer learning to detect mask. The traing data is collected from multiple sources. For collecting human faces with mask, a subset (i.e.,1000 images) of MAFA dataset (can be found in http://www.escience.cn/people/geshiming/mafa.html) is used. For collecting human faces without mask, is used.

• Keras is used to develop the model
• Resnet-50 is used to train the mdoel.
• Data augmentation (horizontal and vertical shift, flip) is performed as a preprocessing step.
• 99% accuracy is achived while testing with hold-out images.
