fruits = ['apple', 'banana', 'orange', 'strawberry']
vegetables = ['lettuce', 'cucumber', 'carrots']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)
salad = 3 * vegetables
print(salad)

""" 
len(): Returns the length of a list.
min(): Returns the minimum value in a list.
max(): Returns the maximum value in a list.
sorted(): Sorts a list in ascending order.
enumerate(): Returns a list of tuples, where each tuple contains the index and value of each item in the list.
map(): Applies a function to each item in a list and returns a list of the results.
"""
print(len(fruits))
print(min(fruits))
enumerated_list = enumerate(fruits)

for index, value in enumerated_list:
    print(index, value)

lengths_list = list(map(len, fruits))
print(lengths_list)

#other built in functions : 
#https://docs.python.org/2/library/functions.html

"""
Here are some of the most commonly used list built-in methods:

append(): Adds an item to the end of a list.
extend(): Adds all items from a second list to the end of the first list.
pop(): Removes and returns the item at the given index from a list. If no index is passed, the last item in the list is removed.
index(): Returns the index of the first occurrence of the given value in a list. If the value is not found, the method returns -1.
remove(): Removes the first occurrence of the given value from a list. If the value is not found, the method does nothing.
sort(): Sorts the list in ascending order.
reverse(): Reverses the order of the list.
"""