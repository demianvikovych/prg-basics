###
# Calculates the sum of the digits in a number
#
def sum_digits(number):

    number_str=str(number)
    sum= 0
    for i in  number_str:
        sum += int(i)
    
        
    return sum
    
    

    
    


any_number = abs(int(input('Enter integer number: ')))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')