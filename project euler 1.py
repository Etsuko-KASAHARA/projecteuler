##if we list the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.abs
# # the sum of these multiples is 23.
# # Find the sum of all the multiples of 3 or 5 below 1000 




def sum_multiples (x):
    result = 0
    first_num = 0
    while first_num < x:
        
            if first_num % 3 == 0 or first_num % 5 == 0:
                
                result += first_num
            first_num += 1
            

    return (result)
    

print (sum_multiples(1000))    
