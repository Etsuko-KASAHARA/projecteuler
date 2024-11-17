## the following interactive sequence is defined for the set of positive integers:
##n→n/2(n is even)
##n→3n+1(n is odd)
##using the rule above and starting with 13, we generate the following sequesnce:
##13→40→20→10→5→16→8→4→2→１
##it can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
##Although it has not been proved yet(Collatz Problem), it is throught that all starting numbers finish at 1.abs
##which starting number, under one million, produced the longest chain?
##Note:once the chain starts the terms are allowed to go above one million

def euler14():
   
    
    long_result=[]
    for n in range(1, 1000000):
        result = [n]

        while n != 1:
        
            if n % 2 == 0:
                n //= 2
                result.append(n)
            
            else:
                n = 3*n + 1
                result.append(n)  

        if len(result) > len(long_result):
            long_result = result
    return long_result[0]    


print(euler14())              