import json

file_obj=open('./sample.json','r')

json_object=  json.load(file_obj)


print(json_object['accounting'][0])
print(type(json_object['accounting']))