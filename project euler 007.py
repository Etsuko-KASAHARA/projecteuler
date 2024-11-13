## by listing the first six prime numbers:2,3,5,7,11 and 13,
## we can see that the 6th prime number is 13
## what is the 10001st prime number?


def prime_number():
    result = []
    while len(result) <=6:
        for num in range(2,1000,1):
            i = 2
            while i*i < num:
                if num % i != 0:
                    result.append(num)
                    i += 1
    return max(result)

print(prime_number())                    