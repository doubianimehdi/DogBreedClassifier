import sys
import cv2
import pickle
import numpy as np
from keras.models import load_model

import tensorflow as tf
physical_devices = tf.config.experimental.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], True)

def main(image_path, height, width):
    model = load_model('tl_fine_tuning_InceptionResNetV2_120_breeds')

    img = cv2.imread(image_path)
    img = cv2.resize(img, (int(height), int(width)))
    img = np.reshape(img, (-1, int(height), int(width), 3)) / 255

    with open('classes_encoding_120', 'rb') as f:
        classes_labels = pickle.load(f)

    label = classes_labels[model.predict_classes(img)[0]]
    print(f"\n\nPredicted breed: {label}")

if len(sys.argv) > 1:
    main(sys.argv[1],sys.argv[2],sys.argv[3])