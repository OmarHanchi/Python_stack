#For Loops through Strings
for x in 'Hello':
    print(x)
# output: 'H', 'e', 'l', 'l', 'o'
print("."*50)

#For Loops through Lists
my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
# output: 0 abc, 1 123, 2 xyz
    
# OR 
    
for v in my_list:
    print(v)
# output: abc, 123, xyz
print("."*50)

#For Loops through Tuples
dog = (1,2,4,6,9)
for data in dog:
    print(data)
print("."*50)
#For Loops through Dictionaries
"""Dictionaries are also iterable. When we iterate through a dictionary, the iterator is each of the keys of the dictionary."""
my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(k)
print("."*50)
# output: name, language
"""That means if we want the values of our dictionary, we might do something like this:"""
my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(my_dict[k])
# output: Noelle, Python
print("."*50)

capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# another way to iterate through the keys
for key in capitals.keys():
    print(key)
# output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
print("."*50)
#to iterate through the values
for val in capitals.values():
    print(val)
# output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
print("."*50)
#to iterate through both keys and values
for key, val in capitals.items():
    print(key, " = ", val)
# output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc




