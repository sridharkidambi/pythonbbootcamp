import json
from collections import namedtuple
import namedtupled

file_obj=open('./sample.json','r')

json_object=  json.load(file_obj)


# print(json_object['accounting'][0])
# print(type(json_object['accounting']))

namedTupleConstructor = namedtuple('myNamedTuple', ' '.join(sorted(json_object.keys())))
nt= namedTupleConstructor(**json_object)
cat = namedtupled.map(json_object)
print(cat.accounting[0].lastName)