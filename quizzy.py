car = {
    'make': 'Honda', 
    'model': 'Accord', 
    'year': '1999', 
    'color': 'Green', 
    'passengers': ['Joe', 'Bob', 'Nancy'],
}

car['mileage'] = '696969'
# print(car)

# print('Only Keys:', list(car.keys()))

# for key in car:
#     print(key)

for value in car.values():
    print(value)

options = [
    {'label': 'Yes'},
    {'label': 'No'},
    {'label': 'Maybe'},
]