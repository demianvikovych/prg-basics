###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
number1 = float(input("enter the number: "))
number2 = float(input("enter the second number: "))
operator = input('enter the operator: ')
result = 0
if operator == '+':
    result +=(number1 + number2)
elif operator == '-':
    result +=(number1 - number2)
elif operator == '*':
    result +=(number1 * number2)
elif operator == '/':
    result +=(number1 / number2)
print(result)