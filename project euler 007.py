## by listing the first six prime numbers:2,3,5,7,11 and 13,
## we can see that the 6th prime number is 13
## what is the 10001st prime number?


def prime_number():
    result = []
    
    for num in range(2,10000000,1):
        is_prime = True
        for i in range(2, int(num ** 0.5)+1):
            if num %i == 0:
                is_prime = False
                break
        if is_prime:
            result.append(num)
            if len(result) == 10001:
                    break
    return max(result)  
        

print(prime_number())                    

