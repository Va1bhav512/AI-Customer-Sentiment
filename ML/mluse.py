from keras.models import model_from_json
from keras.preprocessing.image import load_img
from keras.utils import get_custom_objects
import tensorflow as tf

# Register custom activations if needed
def swish_activation(x):
    return x * tf.nn.sigmoid(x)

get_custom_objects().update({'swish_activation': swish_activation})


import numpy as np
import cv2

json_file = open('emotiondetector.json', 'r')

loaded_model_json = json_file.read()

json_file.close()

model = model_from_json(loaded_model_json)
model.load_weights('emotionaldetector.h5')

hear_file = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(hear_file)

def extract_features(image):
    feature = np.array(image)
    feature = feature.reshape(1, 1, 48, 48)
    return feature/255

webcam = cv2.VideoCapture(0)
labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

while True:
    i, im = webcam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    try:
        for(x, y, w, h) in faces:
            face = gray[y:y+h, x:x+w]
            face = cv2.resize(face, (48, 48))
            face = extract_features(face)
            prediction = model.predict(face)
            emotion = labels[np.argmax(prediction)]
            cv2.rectangle(im, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(im, emotion, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Emotion Detector', im)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    except cv2.error:
        pass