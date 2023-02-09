import json
from PIL import Image
import numpy as np

TRAIN_DATA_PATH = "bdd100k/labels/drivable/polygons/drivable_train.json"

with open(TRAIN_DATA_PATH,"r") as train_json:
    train_list = json.load(train_json)

print(len(train_list))

def get_x_y(target_train):
    train_y = target_train['labels'][0]['poly2d'][0]['vertices']

    img = Image.open('100k/train/' + target_train['name'])
    img_array = np.array(img)

    train_x = img_array

    print('x train data')
    print(train_y)

    print('y train data')
    print(train_x)

for target_train in train_list[:10]:
    get_x_y(target_train)