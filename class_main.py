import json
import cv2
import numpy as np


class LabeledImage():
    pass

class LabledImages():
    def __init__(self, base_img_path, label_json_path):
        self.base_img_path = base_img_path
        self.label_json_path = label_json_path

        self.train_list = []
        self.labeled_images = []

        with open(self.label_json_path,"r") as new_train_json:
            self.train_list = json.load(new_train_json)

    def get_raw_image(self, index):
        target_img = self.train_list[index]
        train_path = f"./100k/train/{target_img['name']}"
        img = cv2.imread(train_path, cv2.IMREAD_COLOR)
        return img

    def draw_labels(self, img, target_labels):
        for labels in target_labels:
            img = self.draw_label(img, labels)
        return img

    def draw_label(self, img, labels):
        for key, value in labels.items():
            if(key == 'box2d'):
                self.draw_rectangle_label(img, (int(value['x1']), int(value['y1'])), (int(value['x2']), int(value['y2'])))
            elif(key == 'poly2d'):
                for vertice in value[0]['vertices']:
                    pts = np.array(vertice, np.int32)
                    pts = pts.reshape((-1, 1, 2))
                    img = cv2.polylines(img, [pts], value[0]['closed'], (0, 255, 0), thickness=3)
        return img

    def draw_rectangle_label(self, img, cor1, cor2):
        img = cv2.rectangle(img, cor1, cor2, (0,255,0), 3)
        return img

    def show_img(self, img):
        cv2.imshow("img",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def run(self, index):
        img = self.get_raw_image(index)
        img = self.draw_labels(img, self.train_list[index])
        self.show_img(img)

def main():
    test_label_images = LabledImages("./100k/train/", "./labels/new_train.json")
    val_label_images = LabledImages("./100k/val/", "./labels/val.json")
    while True:
        index = input("몇번째??: ")
        if(index == 'quit'):
            break
        index = int(index)
        test_label_images.run(index)

main()