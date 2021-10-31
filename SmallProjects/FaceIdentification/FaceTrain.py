import cv2 as cv
import os
from PIL import Image
import numpy as np
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
faces_dir = os.path.join(BASE_DIR, 'Faces')

recognizer = cv.face.LBPHFaceRecognizer_create()

current_id = 0
label_ids = {}
y_lebels = []
x_train = []

for root, dirs, files in os.walk(faces_dir):
    for file in files:
        if file.endswith("png") or file.endswith('jpg'):
            path = os.path.join(root, file)
            label = os.path.basename(root).replace(' ', '-')
            if label not in label_ids:
                label_ids[label] = current_id
                current_id += 1

            id_ = label_ids[label]

            pil_image = Image.open(path)
            final_image = pil_image.resize((550,550), Image.ANTIALIAS)
            image_array = np.array(final_image, 'uint8')
            x_train.append(image_array)
            y_lebels.append(id_)

with open('labels.pickle', 'wb') as f:   # writing bytes = wb
    pickle.dump(label_ids, f)

recognizer.train(x_train, np.array(y_lebels))
recognizer.save('trainner.yml')