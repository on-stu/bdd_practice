import json
import cv2 as cv
import numpy as np


class ImageLabeled():
    def __init__(self, basic_json_path, img_path):
        self.basic_json_path = basic_json_path
        self.img_path = img_path

        with open(basic_json_path,"r") as new_tran_json:
            self.train_list = json.load(new_tran_json)
        
    def get_raw_image(self, index):
        self.target_img = self.train_list[index]
        train_path = f"./100k/train/{self.target_img['name']}"
        img = cv.imread(train_path, cv.IMREAD_COLOR)
        return img

    def get_draw_images(self, img, target_img):
        target_labels = target_img['labels']
        for labels in target_labels:
            img = self.get_draw_image(img, labels)
        return img

    def get_draw_image(self, img, labels):
        for key, value in labels.items():
            if(key == 'box2d'):
                img = self.draw_rectangle_labels(img, (int(value['x1']), int(value['y1'])), (int(value['x2']), int(value['y2'])))
            elif(key == 'poly2d'):
                img = self.draw_ploy2d_labels(img,value)
        return img
        
    def draw_rectangle_labels(self, img, cor1, cor2):
        img = cv.rectangle(img, cor1, cor2, (0, 255, 0), 3)
        return img


    def draw_ploy2d_labels(self, img, value):
        for vertice in value[0]['vertices']:
            pts = np.array(vertice, np.int32)
            pts = pts.reshape((-1, 1, 2))
            img = cv.polylines(img, [pts], value[0]['closed'], (0, 255, 0), thickness=3)
        return img

    def show_img(self, img):
        cv.imshow("img",img)
        cv.waitKey(0)
        cv.destroyAllWindows()

    def run(self, index):
        img = self.get_raw_image(index)
        img = self.get_draw_images(img, self.train_list[index])
        self.show_img(img)

    
def main():
    test_labeled_data = ImageLabeled("./labels/new_train.json", "./100k/train/")
    while True:
        index = input("몇번째??: ")
        if(index == 'quit'):
            break
        index = int(index)
        test_labeled_data.run(index)

main()


    

