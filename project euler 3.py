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
    result = 0
    while divisor <= x:
        if next_number % divisor == 0:
            next_number = round(next_number / divisor)
            result = divisor
        
        divisor+= 1
    return result  





print(prime_factor2(60)) 
print(prime_factor2(13195))

## too big number
##print(prime_factor2(600851475143)) 

def prime_factor3(x):
    next_number = x
    divisor = 2
    result=0
    
    while next_number % divisor == 0:
        next_number = round(next_number / divisor)
        result = devisor

    divisor = 3    

    while divisor * divisor <= next_number:
        while next_number % divisor == 0:
            next_number = round(next_number / divisor)
            result = divisor
        divisor += 2

    if next_number > 2:
        result = next_number

    return result


print(prime_factor3(13195))
print(prime_factor3(600851475143))



