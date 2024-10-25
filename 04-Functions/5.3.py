import mymodule
first_name = mymodule.input_string('Enter name: ')
last_name = mymodule.input_string('Enter your last name : ')
age = mymodule.input_integer("Enter your age: ")
salary = mymodule.input_integer('Enter your salary: ')
is_salary_hidden = mymodule.input_boolean('Hide salary? (y/n)')

# Prints employee's record
print('DATA RECORD')
print('===========')
print('Name:', {first_name})
print('Surname:',{last_name})
print('Age:',{age})
if is_salary_hidden =='n':
    print('Salary',{salary})