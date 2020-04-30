import sys
import pickle
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
import streamlit as st 
from keras.layers.core import Dense, Activation
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras.applications.imagenet_utils import decode_predictions
from keras.applications.mobilenet_v2 import preprocess_input, MobileNetV2


@st.cache(persist=True) 
def predict(image1): 
    model = MobileNetV2(include_top=True, weights='imagenet')
    model._make_predict_function()
    #model = load_model('tl_fine_tuning_InceptionResNetV2_120_breeds.h5')
    image = load_img(image1, target_size=(224, 224))
    # convert the image pixels to a numpy array
    image = img_to_array(image)
    # reshape data for the model
    image = image.reshape((-1, image.shape[0], image.shape[1], 3)) / 255
    #img = cv2.imread(image1)
    #img = cv2.resize(img, (299, 299))
    #img = np.reshape(img, (-1, 299, 299, 3)) / 255
    #with open('classes_encoding_120', 'rb') as f:
    #    classes_labels = pickle.load(f)
    #label = classes_labels[model.predict_classes(image)[0]]
    predictions = model.predict(image)
    labels = decode_predictions(predictions)
    label = labels[0][0]
    label, probability = label[1], round(label[2]*100,2)
    return (label, probability)    