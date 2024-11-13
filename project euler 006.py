##the sum of aquares of the first ten natural number is,
##1^2 + 2^2 + ... + 10^2 = 385
##the aquare of the sum of the first ten natural number is,
##(1 + 2 + ... + 10)^2 = 55^2 = 3025
##hence the difference between the sum of the square of the first ten natural numbers and
##the sequare of the sum is 3025-385= 2640
##find the difference between the sum of the squares of the first one hundred natural numbers the square of the sum

def square():
    result = 0
    for num in range(1,11,1):
        result += num**2
    return


print(square())        