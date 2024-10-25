import math
def area(a,b,c):
    p=(a+b+c)/2
    result = math.sqrt((p*(p-a)*(p-b)*(p-c)))
    return result
print(area(4,5,3))