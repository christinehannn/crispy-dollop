student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

# adding key value pairs one at a time to the dictionary/ replacing
# student['phone'] = '555-5555'
# student['name'] = 'Jane'

# updating multiple key value pairs simultaneously
student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})
# new_student = {
#     **student,
#     'name': 'Jane',
#     'age': 26,
#     'phone': '555-5555',
# }


# two ways to access keys
# bracket notation
# print(student['name'])

# get method
# print(student.get('phone'))

# get method second argument/ default value
# print(student.get('phone', 'Not Found'))

# delete key
# del student['age']
# age = student.pop('age')

# for key, value in student.items():
#     print(key, value)

# List keys
print('Only Keys:', list(student.keys()))

# List values
print('Only Values:', student.values())
