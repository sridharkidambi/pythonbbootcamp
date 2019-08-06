max_num = float("-inf") 
print(' hello \n World')
print(len(' hello \n World'))
print(2**4 )

sk=2
print(sk)
print(type(sk))
sk=['me','da']
sk.append('rascal')
sk.append('rascal1')
print(sk)
sk.pop(3)
print(sk)
print(sk[0])
print(type(sk))
mystring="Sridhar Kidambi "
print(f"my name is  {mystring}") #new way for formatting
print(("sridhar kidambi {c} {d}").format(c="is" ,d="great"))

print(mystring.upper())
print(mystring.lower())
print(mystring.split())
print(mystring.split("i"))
print(mystring*2)
print(mystring[::])
print(mystring[::2])
print(mystring[2::])
print(mystring[2:6:2])
print(mystring[2:])
print(mystring[:3])
print(mystring[2:10])
# float formatting
k=100/177
print(k)
print("the result was {k1:1.4f}".format(k1=k))  
# the ablve line 1  resembles width

mycheckstring=['a','z','d','b']
print(mycheckstring)
mycheckstring.sort()
castedString=mycheckstring.sort()
type(mycheckstring)
print('hi')
print(mycheckstring)
print(type(castedString))
mycheckstring.reverse()
print(mycheckstring)
mynum=[1,1,[1,2]]
print(mynum[2][1])
# dictionary is unordered collection
# hashmap gives unordered for ordered use treemap or sortedmap or linkedhashmap
#  HashMap is very much similar to Hashtable only difference is Hashtable has all method synchronized 
#  for thread safety while HashMap has non-synchronized methods for better performance.

my_dic={'key1': 'value1','key2': 'value2','key1': 'value1','key3': {'value2':'sample piece'}}
# my_dic.items.
print(my_dic['key3']['value2'])