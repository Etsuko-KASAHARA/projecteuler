##2^15 = 32768 and the sum of its digits is 3 +2+7+6+8=26
##what is the sumof the digits of the number 12^1000

def euler16(n):
    pre_result = 2 ** n
    
    result=[int(x) for x in list(str(pre_result))]
    result_num=0
    for i in result:
        result_num += i

    
    return result_num


print(euler16(1000))    