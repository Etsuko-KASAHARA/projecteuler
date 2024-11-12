## A palindromic number reads the same both ways
## The largest palindrome made from the product of
##2-digit numbers is 9009 = 91 ×99
##Find the largest palindrome made from the product of two 3-digit numbers



def palindrome_number (a):
    a = []
    for num1 in range(999, 99, -1):
        for num2 in range(999, 99, -1):
            result = str(num1 * num2)
            if result == result[::-1]:
                a.append(int(result))
    return max(a) 


aa = []
print(palindrome_number (aa))     

##b = 1234
##print((str(b))[::-1])
##print((str(b))[::-2])
##print((str(b))[0:3:2])
