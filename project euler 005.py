##2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder
##what is the smallest positive number that is evenly dividible by all of the numbers from 1 to 20?

import math
"""
def number(y):
    result = 0
    for x in range(2520,y):
        divisor = 1
        if all(x % divisor == 0 for divisor in range(1, 20)):
            result = x
            return result
            
"""
         


##infinite rooppppppppppp
##print(number (10000000))       

"""
def number(y):
    
    result = 0
    
    for num in range(y, 1000000, -1):
        divisor = 1
        if all(num % divisor == 0 for divisor in range(1,20)):
            result = num
            return result 

print(number(10000000))   
"""


def euler005():
    prime_nums=[]
    divisor = 2
    for num in range(1,21):
        x = num
        while x % divisor == 0:
            x = round(x/divisor)
            prime_nums.append(divisor)
        divisor=3
        while divisor*divisor <= x:
            while x % divisor == 0:
                x = round(x/divisor)
                prime_nums.append(divisor)
            divisor += 2   
    return prime_nums        

def euler2(prime_nums):
    how_many={}
    pre_result=0
    result = 1
    for num in prime_nums:
        count = 0
        if num in how_many:
            how_many[num] += 1
        else:
            how_many[num] = 1    
    for num in how_many:
        result *= num ** how_many[num]

                
    return how_many, result            
    

print(euler005())
print((euler2(euler005())))





##これだと違うんだよねぇ
"""
def number():

    total=1
    for n in range(20,0,-1):
        total *= n
    return total   

print(number())
"""
