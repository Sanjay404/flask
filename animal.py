import numpy as np
import pandas as pd
from sklearn.utils.multiclass import unique_labels
import matplotlib as plt
import matplotlib.image as mpimg
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from keras import Sequential
from keras.applications import VGG19, VGG16, ResNet50
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import SGD,Adam
from keras.callbacks import ReduceLROnPlateau
from keras.layers import Flatten, Dense, BatchNormalization, Activation,Dropout
from keras.utils import to_categorical
import tensorflow as tf
import cv2

class_names = ['cat', 'lynx', 'wolf', 'coyote', 'cheetah', 'jaguar', 'chimpanzee', 'orangutan', 'hamster', 'guinea pig']
shape = (128,128)
base_model_VGG19 = VGG19(include_top=False, weights='imagenet', input_shape=(shape[0],shape[1],3), classes= len(class_names))

class VGG19:
        @staticmethod
        def build():
            model = Sequential()
            model.add(base_model_VGG19)
            model.add(Flatten()) 
            model.add(Dense(1024,activation=('relu'),input_dim=512))
            model.add(Dense(512,activation=('relu'))) 
            model.add(Dense(256,activation=('relu'))) 
            #model_vgg19.add(Dropout(.3))
            model.add(Dense(128,activation=('relu')))
            #model_vgg19.add(Dropout(.2))
            model.add(Dense(10,activation=('softmax')))
            return model
VGG19_model = VGG19.build()
VGG19_model.load_weights('/Users/sanjay/Desktop/CODE/Python/Animal-Classification/VGG19A_Animal_Classifier.h5')

def predict(image):
    x = np.expand_dims(image, axis=0)
    image = np.vstack([x])
    classes = VGG19_model.predict(image, batch_size=1)
    index_max = np.argmax(classes)
    return (class_names[index_max] + f': {100*classes[0][index_max]}%')
    '''
    for img in images:
        x = np.expand_dims(img, axis=0)
        images = np.vstack([x])
        classes = VGG19_model.predict(images, batch_size=1)
        index_max = np.argmax(classes)
        print(class_names[index_max] + f'at {classes[index_max]}%')
        dic.append(images, class_names[index_max] + f'at {classes[index_max]}%')
    '''
