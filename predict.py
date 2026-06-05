import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

import tensorflow as tf
import cv2
import numpy as np

IMG_SIZE = 224  # use same size as training

model = tf.keras.models.load_model("mask_detector.h5")

# Change this to any test image path
image_path = "test.jpg"

img = cv2.imread(image_path)
img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
img = img / 255.0
img = np.reshape(img, (1, IMG_SIZE, IMG_SIZE, 3))

prediction = model.predict(img)

if prediction[0][0] > 0.5:
    print("Prediction: No Mask")
else:
    print("Prediction: Mask")
