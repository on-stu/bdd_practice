import json
import cv2
import numpy as np

with open("./labels/val.json","r") as val_json:
    val_list = json.load(val_json)

def get_labeled_image(index):
    target_img = val_list[index]

    img_path = f"./100k/val/{target_img['name']}"
    print(target_img)
    img_read = cv2.imread(img_path, cv2.IMREAD_COLOR)   

    target_labels = target_img['labels']
    for label in target_labels:
        for key, value in label.items():
            if(key == 'box2d'):
                img_read = cv2.rectangle(img_read, (int(value['x1']), int(value['y1'])), (int(value['x2']), int(value['y2'])), (0,255,0), 3)
                
                
            elif(key == 'poly2d'):
                positions = []
                for vertice in value[0]['vertices']:
                    new_position = [int(a) for a in vertice]
                    positions.append(new_position)
                print(positions)
                positions =  np.array( positions, np.int32)
                positions = positions.reshape((-1, 1, 2))
                img_read = cv2.polylines(img_read, [positions], value[0]['closed'], (0,255,0), 3)

    cv2.imshow('img', img_read)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

while True:
    index = input('몇번째 사진 이용할 껴? : ')
    if(index == 'quit'):
        break
    index = int(index)
    get_labeled_image(index)
