import cv2 as cv
import numpy as np
import json

with open("./labels/new_train.json","r") as new_train_json:
    train_list = json.load(new_train_json)

class LabeledImage:
    def __init__(self, index):
        self.index = index
    target_img = train_list[index]
    train_path = f"./100k/train/{target_img['name']}"
    img_read = cv.imread(train_path, cv.IMREAD_COLOR)

    target_labels = target_img['labels']
    for labels in target_labels:
        for key, value in labels.items():
            if(key == 'box2d'):
                img_read = cv.rectangle(img_read, (int(value['x1']), int(value['y1'])), (int(value['x2']), int(value['y2'])), (0,255,0), 3)
            elif(key == 'poly2d'):
                for vertice in value[0]['vertices']:
                    pts = np.array(vertice, np.int32)
                    pts = pts.reshape((-1, 1, 2))
                    img_read = cv.polylines(img_read, [pts], value[0]['closed'], (0, 255, 0), thickness=3)
            
            
    cv.imshow("img",img_read)
    cv.waitKey(0)



while True:
    index = input("몇번째??: ")
    if(index == 'quit'):
        break
    index = int(index)
    get_image(index)


