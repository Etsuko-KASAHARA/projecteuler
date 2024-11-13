##the sum of aquares of the first ten natural number is,
##1^2 + 2^2 + ... + 10^2 = 385
##the aquare of the sum of the first ten natural number is,
##(1 + 2 + ... + 10)^2 = 55^2 = 3025
##hence the difference between the sum of the square of the first ten natural numbers and
##the sequare of the sum is 3025-385= 2640
##find the difference between the sum of the squares of the first one hundred natural numbers the square of the sum

def square():
    square_first = 0
    square_later=0
    for num in range(1,101,1):
        square_first += num ** 2
        square_later += num

    square_later **= 2
    result = square_later - square_first
    return result



print(square())        