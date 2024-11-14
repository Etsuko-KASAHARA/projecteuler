##a pythoagorean triplet is a set of three natural numbers, a < b < c, for which,
##a^2 + b^2 = c^2
##for wxample, 3^2 + 4^2 = 9 + 16 = 5^2
## there exists exactly one pthagorean triplet for which a + b + c = 1000
##fing the product abc

def euler9():
    result=[]
    a_square=1
    b_square=1
    c_square=1
    for a in range(1, 1000,1):
        a_square = a ** 2 
        for b in range(a+1,1000-a,1):
            b_square = b ** 2
            c = 1000 - a - b
            c_square = c ** 2
            if a_square + b_square == c_square:
                result.append(a)
                result.append(b)
                result.append(c)
            
            """
            for c in range(b+1, 1000-b,1):
                c_square = c ** 2
                if a_square + b_square == c_square and a + b + c == 1000:
                    result.append(a)
                    result.append(b)
                    result.append(c)
            """  
        result_num = 1          
        for i in result:
            result_num *= i           
    return result, result_num                
        

print(euler9())