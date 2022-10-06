import json

base_path = "./labels/"

with open(base_path + "train.json","r") as train_json:
    train_list = json.load(train_json)


data = []

for i, train in enumerate(train_list):
    data.append(train)
    if i == 9:
        break

with open(base_path + "new_train.json" , "w") as train2:
    json.dump(data, train2)




