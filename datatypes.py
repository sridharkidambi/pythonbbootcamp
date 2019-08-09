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
print('dictionaries')
my_dic={'key1': 'value1','key2': 'value2','key1': 'value1','key3': {'value2':'sample piece'}}
# my_dic.items.
print(my_dic)
print(my_dic['key3']['value2'])
print(my_dic['key3']['value2'].upper())
# Dictionaries are mappings and do not retain order! If you do want the capabilities of a dictionary but you would like ordering as well, check out the ordereddict object lecture later on in the course!

#  Tuples are similar to List means they are immutable
# Advantages of immutable objects:

# An immutable object remains in exactly one state, the state in which it was created. Therefore, immutable object is thread-safe so there is no synchronization issue. They cannot be corrupted by multiple threads accessing them concurrently. This is far and away the easiest approach to achieving thread safety.
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
    

