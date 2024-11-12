##2050 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder
##what is the smallest positive number that is evenly dividible by all of the numbers from 1 to 20?

def number(y):

    result_list = []
    for x in range(y):
        for divisor in range (1, 21):
            if x % divisor == 0:
                result  = x
                result_list.append(x)

    return result     



print(number (1000000))       