print('Please enter the following information: ')
print()
first_name = input('First name: ')
last_name = input('Last name: ')
email = input('Email address: ')
phone = input('Phone number: ')
job = input('Job title: ')
id_number = input('ID number: ')
hair_color = input('Hair color: ')
eyes_color = input('Eyes color: ')
month = input('Starting month: ')
training = input('Training completed?: ')

print()  # blank line or print('\nThe ID Card is:')
print('The ID Card is:')
print('--------------------------')
print(f'{last_name.upper()}, {first_name.capitalize()}')
print(f'{job.title()}')
print(f'{id_number}')
print()
print(f'{email.lower()}')
print(f'{phone}')
print()
# number means spaces
print(f'Hair: {hair_color.capitalize():10} Eyes: {eyes_color.capitalize()}')
print(f'Month: {month.capitalize():9} Training: {training.capitalize()}')
print('--------------------------')
