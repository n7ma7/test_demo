name = input('your name? ')
last = input('your last name? ')
welcome = (f'Hi {name} [{last}]')
print(welcome.upper())

birth_year = input('Year of birth ')
age = (2022 - int(birth_year))
print('your are ' + str(age) + ' years old')
print(type(age))

weight_kg = input("Weight (Kg) ")
weight_lbs = float(weight_kg)*2.20462
print('your converted weight in Lbs is ' + str(weight_lbs))

msg = f'{name} {last} with {age} years old and {weight_lbs} is a coder'
print(msg)
print(len(msg), 'characters')

