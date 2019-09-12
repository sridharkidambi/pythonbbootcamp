from myclass.sampleclass import sampleclass

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

# reverse a string
name_my='cinema'
print('reverse string is:')
print(name_my[::-1])
# float formatting
k=100/177
print(k)
print("the result was {k1:1.4f}".format(k1=k))  
# the ablve line 1  resembles width

mycheckstring=['a','z','d','b']
print ('sorted')

print(sorted(mycheckstring))
print(mycheckstring)
mycheckstring.sort()
print(mycheckstring)
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
print('dictionaries')
my_dic={'key1': 'value1','key2': 'value2','key1': 'value1','key3': {'value2':'sample piece'}}
# my_dic.items.
print(my_dic)
print(my_dic['key3']['value2'])
print(my_dic['key3']['value2'].upper())
# Dictionaries are mappings and do not retain order! If you do want the capabilities of a dictionary but you would like ordering as well, 
# check out the ordereddict object lecture later on in the course!

#  Tuples are similar to List means they are immutable
# Advantages of immutable objects:

# An immutable object remains in exactly one state, the state in which it was created. Therefore, immutable object is thread-safe so there is no 
# synchronization issue. They cannot be corrupted by multiple threads accessing them concurrently. This is far and away the easiest approach to achieving 
# thread safety.
# Immutable classes are easier to design, implement, and use than mutable classes.
# Immutable objects are good Map keys and Set elements, since these typically do not change once created.
# Immutability makes it easier to write, use and reason about the code (class invariant is established once and then unchanged).
# Immutability makes it easier to parallelize program as there are no conflicts among objects.
# The internal state of program will be consistent even if you have exceptions.
# References to immutable objects can be cached as they are not going to change. (i.e. in Hashing it provide fast operations).
# Disadvantages of immutable objects:

# Creating an immutable class seems at first to provide an elegant solution. However, whenever you do need a modified object 
# of that new type you must suffer the overhead of a new object creation, as well as potentially causing more frequent garbage collections. 
# The only real disadvantage of immutable classes is that they require a separate object for each distinct value.

# Defensive copy:
# the get method should return the new object value or else the caller can change the value.

tple_value=(1,2,"sk",[1,2,3])
print(tple_value[3][1])
print(tple_value.count("sk"))
print(tple_value.index("sk"))

print('******************SET****************** ')
myset= set()
myset.add(1)
myset.add(2)
myset.add(2)
print(myset)
myset1= list('Parallel')
print(myset1)
print(1==1)
print(set([1,1,2,3]))
myfile=open("myfile.txt")
print(myfile.read())
myfile.seek(0)
print(myfile.read())
myfile.seek(0)
print(myfile.readlines())
with open('myfile.txt',mode='a' ) as  my_file_txt:
    my_file_txt.write("askdlasndln")
print(100**.5)
print(3 !=3)

#  logical operators
print(1<2>3)
print(1<2<3)
print(not(1<2 and 2<3))

#  control statements:

# if elif else
print("*********** IF ELIF ELSE in PYTHON *****************")
if not(1<2 and 2<3) == True :
    print("IF is working")
elif not(1<2 and 2<3) == 1 :
    print("ELIF is working")
else:
    print("default print for ELSE")

# for loop in python
print("*********** FOR LOOP in PYTHON *****************")
for item in my_dic:
    print(my_dic[item])
for item in 'hello world':
    print(item)
for item in tple_value:
    print(item)

# TUPLE unpacking
print ('*********TUPLE unpacking****************')
my_tple_list=[(1,2),(3,4),(5,6),(7,8),(9,10)]

for (a,b) in my_tple_list:
    print(a)
    print(b)
i=0
print ('*********WHILE LOOp****************')
while i<=100:
#    comment
    print(i)
    # continue break
    pass    
    i=i+1
else:
    print("out of while loop")
print("*********** RANGE in PYTHON *****************")
for item in range(0,10,5):
    print(item)
emum_string="Sridhar kidambi"

for index,item in enumerate(emum_string):
    print(index)
    print(item)
    print('\n')
print("*********** ZIP PYTHON *****************")
my_tple_list2=[(1,2),(3,4),(5,6),(7,8),(9,10),(1,2),(3,4),(5,6),(7,8),(9,10)]

for item in zip(my_tple_list,my_tple_list2):
    print(item)
print("*********** IN  PYTHON *****************")
print('sk' in ['sk',2 ,3])
print("*********** MAX/MIN  PYTHON *****************")
print(min(my_tple_list))
print("*********** RANDOM LIBRARY PYTHON *****************")
print(my_tple_list)
from random import shuffle
print(shuffle(my_tple_list))
print(my_tple_list)
from random import randint
myny=randint(0,100)
print(myny)
inresul=input('enter a number here:')
print(inresul)
print(type(inresul))
print(float(inresul))
#  LIST comprehension

print("*********** LIST comprehension PYTHON *****************")
new_lst= [item for item in emum_string  if item=='a' ]
print(new_lst)

print("*********** NESTED FOR LOOP PYTHON *****************")
nesterd_list_items=[]

for i in [1,2,3,4,5]:
    for j in [100,200,300,400,500]:
        nesterd_list_items.append(i*j)
print(nesterd_list_items)
value = 124
print(value, 'is', 'even' if value % 2 == 0 else 'odd')

for i in range(1,101,1) :
    if  i%3==0 and i%5!=0  :
        print('FIZZ3')
    elif ( i%5==0 and i%3!=0 ) :
        print('FIZZ5')
    elif ( i%3==0 and i%5==0 ) :
        print('FIZZALL35')
    else :
        print(i)

    # help function:

    # help(my_dic)

def sridharkidambifunc(name):
    return ('hello-->'+ name)

myresult= sridharkidambifunc('sridharKidambi')
print(myresult) 

print('***********MULTI PARAM ARGUEMENTS-tuple format************')
def funcmeMultiparams(*args): #return tuples means immutable
    return sum(args)

resutmmulti = funcmeMultiparams(10,20,30,40,50) 

print(resutmmulti)

print('***********MULTI PARAM ARGUEMENTS-tuple format************')
def funcmeMultiparamsdic(**kwargs): #return dictionary means immutable
    print(kwargs)
    return 'firstName is: ' + kwargs['firsname']

resutmmultikw = funcmeMultiparamsdic(firsname='sk' , lastname='ks') 

print(resutmmultikw.capitalize())
print(resutmmultikw[::-1])

print ('*****'.join(['a','b','c','d']))

print(sum([1,2,4,5]))
print('***********LAMBDA FUNCTIONS MAP AND FILTERS ************')
def squareme(num):
    return num**2
def squareme1(num):
    return num%2 ==0


nums=[1,2,3,4,5]

for item in map(squareme,nums):
    print(item)
print('filter methods->')
for item in filter(squareme1,nums):
    print( item)

print( list(map(squareme,nums)))

print('lambda functions:')
print(list(map(lambda num: num**2,nums)))
print('L E G B local enclosing global  and built-in')

ab=10

def myfunc3():
    global ab
    print(f'number global is:{ab}')
    ab=500
    print(f'number global is:{ab}')
    print( ab )
def callmethod():
    obj=sampleclass("Sridhar Kidambi")
    print(len(obj))
    print(obj)

myfunc3()

import string

print (set (string.ascii_lowercase))
print (set ('The quick brown fox  jumps over the lazy dog'.lower())>= set (string.ascii_lowercase))

#  PACKAGES AND MODULES

# PyPI - repository for the python libraries.linek npm for nodejs

import json

print(json.dumps({'9': 5, '6': 7}, sort_keys=True, indent=4))

callmethod()

k=(1,2)
a,b =k
print(a)
print(b)
print(k)