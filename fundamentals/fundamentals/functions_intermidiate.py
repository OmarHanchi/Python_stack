#1/Update Values in Dictionaries and Lists
x = [ [5,2,3], [15,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Bryant'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Andres', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 30} ]
#2/Iterate Through a List of Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students) :
    for student in students:
        print('first_name - {} , last_name - {}'.format(student['first_name'], student['last_name']))
iterateDictionary(students)
#3/Get Values From a List of Dictionaries
def iterateDictionary2(key_name, students) : 
    for student in students:
        print (student [key_name])
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)
#4/Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for key,value in some_dict.items() :
        print (f"{key} : {len(value)}")
        for item in value :
            print(item)
printInfo(dojo)
