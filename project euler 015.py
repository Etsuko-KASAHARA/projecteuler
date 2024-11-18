##starting in the top left corner of a 2 × 2 grid, and only being able to move to the right and
##down, there are exactly 6 routes the bottom right corner
##how much such rounts are there through 20 × 20 grid?
import math



##4!/2!*2!
##階上
num1=math.factorial(4)
num2=math.factorial(2)
print(round(num1/(num2*num2)))

def euler15(n):
    num1 = math.factorial(n*2)
    num2 = math.factorial(n)
    routes = (round(num1/(num2*num2)))
    return routes


print(euler15(20))    
    
    