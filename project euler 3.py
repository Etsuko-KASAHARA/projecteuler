##The prime factors of 13195 are 5, 7, 13 and 29
## What is the largest prime factor if the number 600851475143?

import math

def prime_factor (x):
    divisor= 2
    next_number = x
    result_list=[]
    while divisor <= x:
        if(next_number % divisor == 0):
            next_number = round(next_number / divisor)
            result_list.append(divisor)
            divisor = 2
            while divisor <= next_number:
                if(next_number % divisor == 0):
                        next_number = round(next_number / divisor)
                        result_list.append(divisor)
                divisor += 1        
        divisor+= 1
    return result_list        




def prime_factor2 (x):
    divisor= 2
    next_number = x
    result_list=[]
    while divisor <= x:
        if next_number % divisor == 0:
            next_number = round(next_number / divisor)
            result_list.append(divisor)
        
        divisor+= 1
    return result_list   


def prime_sum(prime_factors):
    result = 0
    for factor in prime_factors:
        result += factor
    return result    

print(prime_factor2(60)) 
print(prime_factor2(13195)) 
print(prime_sum(prime_factor2(13195)))

## too big number
##print(prime_factor2(600851475143))
##print(prime_sum(prime_factor2(600851475143)))  


