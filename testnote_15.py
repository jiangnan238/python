import json
#导入json模块

file_path = 'loves.json'
favorite_number = input("please enter your favorite number: ")
try:
    with open(file_path,'r+') as probject_2:#加载信息
        loves = json.load(probject_2)
except FileNotFoundError:
    with open(file_path,'w+') as probject_1:#存储信息
        json.dump(favorite_number,probject_1)
else:
    print("i know your favorite number is "+loves)