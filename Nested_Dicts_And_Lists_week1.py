x = [ [5,2,3], [10,8,9] ]
x[1][0] = 15
print(x)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print(z)

#------------------------------------------------------------------------------------------------------------------------------

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(students):
    for student in range(len(students)):
        print(students[student])

iterateDictionary(students)

#------------------------------------------------------------------------------------------------------------------------------

def iterateDictionary2(key_name, some_list):
    for student in range(len(some_list)):
        print(some_list[student][key_name])

iterateDictionary2('first_name', students)

#------------------------------------------------------------------------------------------------------------------------------

dojo = {
    'Locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'Instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(any_dict):
    for x in any_dict:
        length1 = len(any_dict[x])
        print(length1, x)
        for i in any_dict[x]:
            print(i)
# x is dict key names (loc and instr)
# i is everything inside those lists

printInfo(dojo)
