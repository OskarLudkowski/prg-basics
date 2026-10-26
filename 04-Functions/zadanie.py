import keyboard

first_name = keyboard.input_string('Enter name: ')
age = keyboard.input_integer('Enter age: ')
salary = keyboard.input_real('Enter salary: ')
hide_salary = keyboard.input_boolean('Hide salary? (y/n): ')

print('DATA RECORD')
print('Name:', first_name)
print('Age:', age)

if not hide_salary:
    print('Salary:', salary)