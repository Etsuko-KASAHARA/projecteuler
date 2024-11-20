##if the numbers 1 to 5 are written our in words: one, two, three, four, five, then there are 
##3+3+5+4+4=19 letters used in total
##if all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
##how many letters would be used?
##note: do not count spaces or hyphens. for example, 342(three hundred and fourty-two)
##contains 23 letters and 115(one hundred and fifteen) contains 20 letters. 
##the use of "and" when writing out numbers is in compliance with british usage


"""
num_letter ={
    0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen", 20:"twenty", 30:"thiry", 40:"fourty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety", 100:"onehundred", 200:"twohundred", 300:"threehundred", 400:"fourhundred", 500:"fivehundred", 600:"sixhundred", 700:"sevenhundred", 800:"eighthundred", 900:"ninehundred", 1000:"onethausand"

}
"""

num_letter = {
    0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 
    6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 
    12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 
    16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 
    20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 
    70: "seventy", 80: "eighty", 90: "ninety", 100: "onehundred", 
    200: "twohundred", 300: "threehundred", 400: "fourhundred", 
    500: "fivehundred", 600: "sixhundred", 700: "sevenhundred", 
    800: "eighthundred", 900: "ninehundred", 1000: "onethousand"
}

print(len(num_letter))

def euler17():
    result=[]
    sum_letter = 0
    kari = 0
    j = 0
    for i in range(1,1001):
         
       if i <= 20:
            kari = (len(num_letter[i]))
            sum_letter += kari
       elif 20< i < 30:
            kari = (len(num_letter[20])) + (len(num_letter[i - 20]))
            sum_letter += kari
       elif i == 30:
            kari = (len(num_letter[30]))
            sum_letter += kari
       elif 30 < i < 40:
            kari =  (len(num_letter[30])) + (len(num_letter[i-30]))
            sum_letter += kari
       elif i == 40:
            kari = (len(num_letter[40]))   
            sum_letter += kari 
       elif 40 < i < 50:
            kari =  (len(num_letter[40])) + (len(num_letter[i-40]))
            sum_letter += kari   
       elif i == 50:
            kari = (len(num_letter[50]))
            sum_letter += kari 
       elif 50 < i < 60:    
            kari =  (len(num_letter[50])) + (len(num_letter[i-50]))                   
            sum_letter += kari 
       elif i == 60:
            kari = (len(num_letter[60]))
            sum_letter += kari 
       elif 60 < i < 70:
            kari =  (len(num_letter[60])) + (len(num_letter[i-60]))                   
            sum_letter += kari
       elif i == 70:
            kari = (len(num_letter[70]))
            sum_letter += kari            
       elif 70 < i < 80:
            kari =  (len(num_letter[70])) + (len(num_letter[i-70]))                   
            sum_letter += kari
       elif i == 80:
            kari = (len(num_letter[80]))
            sum_letter += kari  
       elif 80 < i < 90:
            kari =  (len(num_letter[80])) + (len(num_letter[i-80]))                   
            sum_letter += kari
       elif i == 90:
            kari = (len(num_letter[90]))
            sum_letter += kari 
       elif 90 < i < 100:
            kari =  (len(num_letter[90])) + (len(num_letter[i-90]))                   
            sum_letter += kari
       elif i == 100:
            kari = (len(num_letter[100]))
            sum_letter += kari
       elif 100 < i < 200:
            kari =(len(num_letter[100])) + 3
            sum_letter += kari
            j = i - 100
            if j <= 20:
                kari = (len(num_letter[j]))
                sum_letter += kari
            elif 20< j < 30:
                kari = (len(num_letter[20])) + (len(num_letter[j-20]))
                sum_letter += kari
            elif j == 30:
                kari = (len(num_letter[30]))
                sum_letter += kari
            elif 30 < j < 40:
                kari =  (len(num_letter[30])) + (len(num_letter[j-30]))
                sum_letter += kari
            elif j == 40:
                kari = (len(num_letter[40]))   
                sum_letter += kari 
            elif 40 < j < 50:
                kari =  (len(num_letter[40])) + (len(num_letter[j-40]))
                sum_letter += kari   
            elif j == 50:
                kari = (len(num_letter[50]))
                sum_letter += kari 
            elif 50 < j < 60:    
                kari =  (len(num_letter[50])) + (len(num_letter[j-50]))                   
                sum_letter += kari 
            elif j == 60:
                kari = (len(num_letter[60]))
                sum_letter += kari 
            elif 60 < j < 70:
                kari =  (len(num_letter[60])) + (len(num_letter[j-60]))                   
                sum_letter += kari
            elif j == 70:
                kari = (len(num_letter[70]))
                sum_letter += kari            
            elif 70 < j < 80:
                kari =  (len(num_letter[70])) + (len(num_letter[j-70]))                   
                sum_letter += kari
            elif j == 80:
                kari = (len(num_letter[80]))
                sum_letter += kari  
            elif 80 < j < 90:
                kari =  (len(num_letter[80])) + (len(num_letter[j-80]))                   
                sum_letter += kari
            elif j == 90:
                kari = (len(num_letter[90]))
                sum_letter += kari 
            elif 90 < j < 100:
                kari =  (len(num_letter[90])) + (len(num_letter[j-90]))                   
                sum_letter += kari
       elif i == 200:
               kari = (len(num_letter[200]))
               sum_letter += kari
       elif 200 < i < 300:        
               kari =(len(num_letter[200])) + 3
               sum_letter += kari
               j = i - 200
               if j <= 20:
                    kari = (len(num_letter[j]))
                    sum_letter += kari
               elif 20< j < 30:
                    kari = (len(num_letter[20])) + (len(num_letter[j-20]))
                    sum_letter += kari
               elif j == 30:
                    kari = (len(num_letter[30]))
                    sum_letter += kari
               elif 30 < j < 40:
                    kari =  (len(num_letter[30])) + (len(num_letter[j-30]))
                    sum_letter += kari
               elif j == 40:
                    kari = (len(num_letter[40]))   
                    sum_letter += kari 
               elif 40 < j < 50:
                    kari =  (len(num_letter[40])) + (len(num_letter[j-40]))
                    sum_letter += kari   
               elif j == 50:
                    kari = (len(num_letter[50]))
                    sum_letter += kari 
               elif 50 < j < 60:    
                    kari =  (len(num_letter[50])) + (len(num_letter[j-50]))                   
                    sum_letter += kari 
               elif j == 60:
                    kari = (len(num_letter[60]))
                    sum_letter += kari 
               elif 60 < j < 70:
                    kari =  (len(num_letter[60])) + (len(num_letter[j-60]))                   
                    sum_letter += kari
               elif j == 70:
                    kari = (len(num_letter[70]))
                    sum_letter += kari            
               elif 70 < j < 80:
                    kari =  (len(num_letter[70])) + (len(num_letter[j-70]))                   
                    sum_letter += kari
               elif j == 80:
                    kari = (len(num_letter[80]))
                    sum_letter += kari  
               elif 80 < j < 90:
                    kari =  (len(num_letter[80])) + (len(num_letter[j-80]))                   
                    sum_letter += kari
               elif j == 90:
                    kari = (len(num_letter[90]))
                    sum_letter += kari 
               elif 90 < j < 100:
                    kari =  (len(num_letter[90])) + (len(num_letter[j-90]))                   
                    sum_letter += kari
       elif i == 300:
               kari = (len(num_letter[300]))
               sum_letter += kari
       elif 300 < i < 400:        
               kari = (len(num_letter[300])) + 3
               sum_letter += kari
               j = i - 300
               if j <= 20:
                    kari = (len(num_letter[j]))
                    sum_letter += kari
               elif 20< j < 30:
                    kari = (len(num_letter[20])) + (len(num_letter[j-20]))
                    sum_letter += kari
               elif j == 30:
                    kari = (len(num_letter[30]))
                    sum_letter += kari
               elif 30 < j < 40:
                    kari =  (len(num_letter[30])) + (len(num_letter[j-30]))
                    sum_letter += kari
               elif j == 40:
                    kari = (len(num_letter[40]))   
                    sum_letter += kari 
               elif 40 < j < 50:
                    kari =  (len(num_letter[40])) + (len(num_letter[j-40]))
                    sum_letter += kari   
               elif j == 50:
                    kari = (len(num_letter[50]))
                    sum_letter += kari 
               elif 50 < j < 60:    
                    kari =  (len(num_letter[50])) + (len(num_letter[j-50]))                   
                    sum_letter += kari 
               elif j == 60:
                    kari = (len(num_letter[60]))
                    sum_letter += kari 
               elif 60 < j < 70:
                    kari =  (len(num_letter[60])) + (len(num_letter[j-60]))                   
                    sum_letter += kari
               elif j == 70:
                    kari = (len(num_letter[70]))
                    sum_letter += kari            
               elif 70 < j < 80:
                    kari =  (len(num_letter[70])) + (len(num_letter[j-70]))                   
                    sum_letter += kari
               elif j == 80:
                    kari = (len(num_letter[80]))
                    sum_letter += kari  
               elif 80 < j < 90:
                    kari =  (len(num_letter[80])) + (len(num_letter[j-80]))                   
                    sum_letter += kari
               elif j == 90:
                    kari = (len(num_letter[90]))
                    sum_letter += kari 
               elif 90 < j < 100:
                    kari =  (len(num_letter[90])) + (len(num_letter[j-90]))                   
                    sum_letter += kari       
       elif i == 400:
               kari = (len(num_letter[400]))
               sum_letter += kari
       elif 400 < i < 500:
               kari = (len(num_letter[400])) + 3
               sum_letter += kari
               j = i - 400
               if j <= 20:
                    kari = (len(num_letter[j]))
                    sum_letter += kari
               elif 20< j < 30:
                    kari = (len(num_letter[20])) + (len(num_letter[j-20]))
                    sum_letter += kari
               elif j == 30:
                    kari = (len(num_letter[30]))
                    sum_letter += kari
               elif 30 < j < 40:
                    kari =  (len(num_letter[30])) + (len(num_letter[j-30]))
                    sum_letter += kari
               elif j == 40:
                    kari = (len(num_letter[40]))   
                    sum_letter += kari 
               elif 40 < j < 50:
                    kari =  (len(num_letter[40])) + (len(num_letter[j-40]))
                    sum_letter += kari   
               elif j == 50:
                    kari = (len(num_letter[50]))
                    sum_letter += kari 
               elif 50 < j < 60:    
                    kari =  (len(num_letter[50])) + (len(num_letter[j-50]))                   
                    sum_letter += kari 
               elif j == 60:
                    kari = (len(num_letter[60]))
                    sum_letter += kari 
               elif 60 < j < 70:
                    kari =  (len(num_letter[60])) + (len(num_letter[j-60]))                   
                    sum_letter += kari
               elif j == 70:
                    kari = (len(num_letter[70]))
                    sum_letter += kari            
               elif 70 < j < 80:
                    kari =  (len(num_letter[70])) + (len(num_letter[j-70]))                   
                    sum_letter += kari
               elif j == 80:
                    kari = (len(num_letter[80]))
                    sum_letter += kari  
               elif 80 < j < 90:
                    kari =  (len(num_letter[80])) + (len(num_letter[j-80]))                   
                    sum_letter += kari
               elif j == 90:
                    kari = (len(num_letter[90]))
                    sum_letter += kari 
               elif 90 < j < 100:
                    kari =  (len(num_letter[90])) + (len(num_letter[j-90]))                   
                    sum_letter += kari      

       elif i == 500:
               kari = (len(num_letter[500]))
               sum_letter += kari 
       elif 500 < i < 600:
               kari = (len(num_letter[500])) + 3
               sum_letter += kari
               j = i - 500
               if j <= 20:
                    kari = (len(num_letter[j]))
                    sum_letter += kari
               elif 20< j < 30:
                    kari = (len(num_letter[20])) + (len(num_letter[j-20]))
                    sum_letter += kari
               elif j == 30:
                    kari = (len(num_letter[30]))
                    sum_letter += kari
               elif 30 < j < 40:
                    kari =  (len(num_letter[30])) + (len(num_letter[j-30]))
                    sum_letter += kari
               elif j == 40:
                    kari = (len(num_letter[40]))   
                    sum_letter += kari 
               elif 40 < j < 50:
                    kari =  (len(num_letter[40])) + (len(num_letter[j-40]))
                    sum_letter += kari   
               elif j == 50:
                    kari = (len(num_letter[50]))
                    sum_letter += kari 
               elif 50 < j < 60:    
                    kari =  (len(num_letter[50])) + (len(num_letter[j-50]))                   
                    sum_letter += kari 
               elif j == 60:
                    kari = (len(num_letter[60]))
                    sum_letter += kari 
               elif 60 < j < 70:
                    kari =  (len(num_letter[60])) + (len(num_letter[j-60]))                   
                    sum_letter += kari
               elif j == 70:
                    kari = (len(num_letter[70]))
                    sum_letter += kari            
               elif 70 < j < 80:
                    kari =  (len(num_letter[70])) + (len(num_letter[j-70]))                   
                    sum_letter += kari
               elif j == 80:
                    kari = (len(num_letter[80]))
                    sum_letter += kari  
               elif 80 < j < 90:
                    kari =  (len(num_letter[80])) + (len(num_letter[j-80]))                   
                    sum_letter += kari
               elif j == 90:
                    kari = (len(num_letter[90]))
                    sum_letter += kari 
               elif 90 < j < 100:
                    kari =  (len(num_letter[90])) + (len(num_letter[j-90]))                   
                    sum_letter += kari              
       elif i == 600:
               kari = (len(num_letter[600]))
               sum_letter += kari 
       elif 600 < i < 700:
               kari = (len(num_letter[600])) + 3
               sum_letter += kari
               j = i - 600
               if j <= 20:
                    kari = (len(num_letter[j]))
                    sum_letter += kari
               elif 20< j < 30:
                    kari = (len(num_letter[20])) + (len(num_letter[j-20]))
                    sum_letter += kari
               elif j == 30:
                    kari = (len(num_letter[30]))
                    sum_letter += kari
               elif 30 < j < 40:
                    kari =  (len(num_letter[30])) + (len(num_letter[j-30]))
                    sum_letter += kari
               elif j == 40:
                    kari = (len(num_letter[40]))   
                    sum_letter += kari 
               elif 40 < j < 50:
                    kari =  (len(num_letter[40])) + (len(num_letter[j-40]))
                    sum_letter += kari   
               elif j == 50:
                    kari = (len(num_letter[50]))
                    sum_letter += kari 
               elif 50 < j < 60:    
                    kari =  (len(num_letter[50])) + (len(num_letter[j-50]))                   
                    sum_letter += kari 
               elif j == 60:
                    kari = (len(num_letter[60]))
                    sum_letter += kari 
               elif 60 < j < 70:
                    kari =  (len(num_letter[60])) + (len(num_letter[j-60]))                   
                    sum_letter += kari
               elif j == 70:
                    kari = (len(num_letter[70]))
                    sum_letter += kari            
               elif 70 < j < 80:
                    kari =  (len(num_letter[70])) + (len(num_letter[j-70]))                   
                    sum_letter += kari
               elif j == 80:
                    kari = (len(num_letter[80]))
                    sum_letter += kari  
               elif 80 < j < 90:
                    kari =  (len(num_letter[80])) + (len(num_letter[j-80]))                   
                    sum_letter += kari
               elif j == 90:
                    kari = (len(num_letter[90]))
                    sum_letter += kari 
               elif 90 < j < 100:
                    kari =  (len(num_letter[90])) + (len(num_letter[j-90]))                   
                    sum_letter += kari              
       elif i == 700:
               kari = (len(num_letter[700]))
               sum_letter += kari 
       elif 700 < i < 800:
               kari = (len(num_letter[700])) + 3
               sum_letter += kari
               j = i - 700
               if j <= 20:
                    kari = (len(num_letter[j]))
                    sum_letter += kari
               elif 20< j < 30:
                    kari = (len(num_letter[20])) + (len(num_letter[j-20]))
                    sum_letter += kari
               elif j == 30:
                    kari = (len(num_letter[30]))
                    sum_letter += kari
               elif 30 < j < 40:
                    kari =  (len(num_letter[30])) + (len(num_letter[j-30]))
                    sum_letter += kari
               elif j == 40:
                    kari = (len(num_letter[40]))   
                    sum_letter += kari 
               elif 40 < j < 50:
                    kari =  (len(num_letter[40])) + (len(num_letter[j-40]))
                    sum_letter += kari   
               elif j == 50:
                    kari = (len(num_letter[50]))
                    sum_letter += kari 
               elif 50 < j < 60:    
                    kari =  (len(num_letter[50])) + (len(num_letter[j-50]))                   
                    sum_letter += kari 
               elif j == 60:
                    kari = (len(num_letter[60]))
                    sum_letter += kari 
               elif 60 < j < 70:
                    kari =  (len(num_letter[60])) + (len(num_letter[j-60]))                   
                    sum_letter += kari
               elif j == 70:
                    kari = (len(num_letter[70]))
                    sum_letter += kari            
               elif 70 < j < 80:
                    kari =  (len(num_letter[70])) + (len(num_letter[j-70]))                   
                    sum_letter += kari
               elif j == 80:
                    kari = (len(num_letter[80]))
                    sum_letter += kari  
               elif 80 < j < 90:
                    kari =  (len(num_letter[80])) + (len(num_letter[j-80]))                   
                    sum_letter += kari
               elif j == 90:
                    kari = (len(num_letter[90]))
                    sum_letter += kari 
               elif 90 < j < 100:
                    kari =  (len(num_letter[90])) + (len(num_letter[j-90]))                   
                    sum_letter += kari         
       elif i == 800:
               kari = (len(num_letter[800]))
               sum_letter += kari 
       elif 800 < i < 900:
               kari = (len(num_letter[800])) + 3
               sum_letter += kari
               j = i - 800
               if j <= 20:
                    kari = (len(num_letter[j]))
                    sum_letter += kari
               elif 20< j < 30:
                    kari = (len(num_letter[20])) + (len(num_letter[j-20]))
                    sum_letter += kari
               elif j == 30:
                    kari = (len(num_letter[30]))
                    sum_letter += kari
               elif 30 < j < 40:
                    kari =  (len(num_letter[30])) + (len(num_letter[j-30]))
                    sum_letter += kari
               elif j == 40:
                    kari = (len(num_letter[40]))   
                    sum_letter += kari 
               elif 40 < j < 50:
                    kari =  (len(num_letter[40])) + (len(num_letter[j-40]))
                    sum_letter += kari   
               elif j == 50:
                    kari = (len(num_letter[50]))
                    sum_letter += kari 
               elif 50 < j < 60:    
                    kari =  (len(num_letter[50])) + (len(num_letter[j-50]))                   
                    sum_letter += kari 
               elif j == 60:
                    kari = (len(num_letter[60]))
                    sum_letter += kari 
               elif 60 < j < 70:
                    kari =  (len(num_letter[60])) + (len(num_letter[j-60]))                   
                    sum_letter += kari
               elif j == 70:
                    kari = (len(num_letter[70]))
                    sum_letter += kari            
               elif 70 < j < 80:
                    kari =  (len(num_letter[70])) + (len(num_letter[j-70]))                   
                    sum_letter += kari
               elif j == 80:
                    kari = (len(num_letter[80]))
                    sum_letter += kari  
               elif 80 < j < 90:
                    kari =  (len(num_letter[80])) + (len(num_letter[j-80]))                   
                    sum_letter += kari
               elif j == 90:
                    kari = (len(num_letter[90]))
                    sum_letter += kari 
               elif 90 < j < 100:
                    kari =  (len(num_letter[90])) + (len(num_letter[j-90]))                   
                    sum_letter += kari          
       elif i == 900:
               kari = (len(num_letter[900]))
               sum_letter += kari 
       elif 900 < i < 1000:
               kari = (len(num_letter[900])) + 3
               sum_letter += kari
               j = i - 900
               if j <= 20:
                    kari = (len(num_letter[j]))
                    sum_letter += kari
               elif 20< j < 30:
                    kari = (len(num_letter[20])) + (len(num_letter[j-20]))
                    sum_letter += kari
               elif j == 30:
                    kari = (len(num_letter[30]))
                    sum_letter += kari
               elif 30 < j < 40:
                    kari =  (len(num_letter[30])) + (len(num_letter[j-30]))
                    sum_letter += kari
               elif j == 40:
                    kari = (len(num_letter[40]))   
                    sum_letter += kari 
               elif 40 < j < 50:
                    kari =  (len(num_letter[40])) + (len(num_letter[j-40]))
                    sum_letter += kari   
               elif j == 50:
                    kari = (len(num_letter[50]))
                    sum_letter += kari 
               elif 50 < j < 60:    
                    kari =  (len(num_letter[50])) + (len(num_letter[j-50]))                   
                    sum_letter += kari 
               elif j == 60:
                    kari = (len(num_letter[60]))
                    sum_letter += kari 
               elif 60 < j < 70:
                    kari =  (len(num_letter[60])) + (len(num_letter[j-60]))                   
                    sum_letter += kari
               elif j == 70:
                    kari = (len(num_letter[70]))
                    sum_letter += kari            
               elif 70 < j < 80:
                    kari =  (len(num_letter[70])) + (len(num_letter[j-70]))                   
                    sum_letter += kari
               elif j == 80:
                    kari = (len(num_letter[80]))
                    sum_letter += kari  
               elif 80 < j < 90:
                    kari =  (len(num_letter[80])) + (len(num_letter[j-80]))                   
                    sum_letter += kari
               elif j == 90:
                    kari = (len(num_letter[90]))
                    sum_letter += kari 
               elif 90 < j < 100:
                    kari =  (len(num_letter[90])) + (len(num_letter[j-90]))                   
                    sum_letter += kari         
       else:
               kari = (len(num_letter[1000]))
               sum_letter += kari                                                    

          
    return sum_letter   

print(euler17())    