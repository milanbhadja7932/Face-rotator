# Face-rotator

# INTRODUCTION

Face rotator is generally uses for rotate the thousand of images and also create csv file for the images.

# CONTENT

[1. GENERATE DATSET](https://github.com/milanbhadja7932/Face-rotator/blob/master/README.md#1-generate-dataset)<br />
[2. TRAINING](https://github.com/milanbhadja7932/Face-rotator/blob/master/README.md#2-training)<br />
[3. TESTING](https://github.com/milanbhadja7932/Face-rotator/blob/master/README.md#3-testing)<br />
[4. OUTPUT](https://github.com/milanbhadja7932/Face-rotator/blob/master/README.md#4-output)<br />

### 1. GENERATE DATASET 
      There are library dependancies to run the dataset.py file. You have to install Keras, Matplotlib, Panda, Numpy, and OS. 
      
### 2. TRAINING
      After that create a model for the data and after some fine tuning. There is a final model was generated. You have to run model.py file for this step.
      Now, model was ready so you have to train dataset with train.py file. The model is trained with 60 epcoh, model save in h5 file, which can be used for the further proccess.
      
### 3. TESTING
      At the end, the test was done by predicting the test images. 
      It generate csv file of prediction using the prediction to correct the rotation of the images. 
### 4. OUTPUT
      There is a zip file generated which contain output images and a csv file for predict the rotation.
      
