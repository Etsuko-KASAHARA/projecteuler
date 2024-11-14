## the sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
## find the sum of all the primes below 2 million

def prime_number():
    result = []
    result_sum = 0
    n = 2000000
    for num in range(2,n+1,1):
        is_prime = True
        for i in range(2, int(num ** 0.5)+1):
            if num %i == 0:
                is_prime = False
                break
        if is_prime:
            result.append(num)
            
    for i in result:
        result_sum += i            
    return max(result), result_sum  
        

print(prime_number())  