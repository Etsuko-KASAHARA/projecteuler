##by starting the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23
#    3
#   7 4
#  2 4 5
# 8 5 9 3
#that is, 3 + 7 + 4 + 9 = 23
##find the maximum total from top to bottom of the triangle below:

"""
              75
             95 64
            17 47 82
           18 35 87 10
          20 04 82 47 65
         19 01 23 75 03 34
        88 02 77 73 07 63 67
       99 65 04 28 06 16 70 92
      41 41 26 56 83 40 80 70 33
     41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
   70 11 33 28 77 73 17 78 39 68 17 57
  91 71 52 38 17 14 91 43 58 50 27 29 48
 63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""
##NOte as there are only 1643 routes, it is possible to solve this problem by trying every route. 
## However, problem64, is the same challenge with a triangle containig one-hundred rows; it cannot be solved by brute force, and require a clever method ;o)


print(max([1,2,3,2]))


line1  = "75"
line2  = "95 64"
line3  = "17 47 82"
line4  = "18 35 87 10"
line5  = "20 4 82 47 65"
line6  = "19 1 23 75 3 34"
line7  = "88 2 77 73 7 63 67"
line8  = "99 65 4 28 6 16 70 92"
line9  = "41 41 26 56 83 40 80 70 33"
line10 = "41 48 72 33 47 32 37 16 94 29"
line11 = "53 71 44 65 25 43 91 52 97 51 14"
line12 = "70 11 33 28 77 73 17 78 39 68 17 57"
line13 = "91 71 52 38 17 14 91 43 58 50 27 29 48"
line14 = "63 66 4 68 89 53 67 30 73 16 69 87 40 31"
line15 = "4 62 98 27 23 9 70 98 73 93 38 53 60 4 23"
all_lines = [line1, line2, line3 , line4 , line5 , line6 , line7, line8, line9, line10, line11, line12, line13, line14, line15]





def euler18():
    
    
    line1  = [75]
    line2  = [95, 64]
    line3  = [17, 47, 82]
    line4  = [18, 35, 87, 10]
    line5  = [20, 4, 82, 47, 65]
    line6  = [19, 1, 23, 75, 3, 34]
    line7  = [88, 2, 77, 73, 7, 63, 67]
    line8  = [99, 65, 4, 28, 6, 16, 70, 92]
    line9  = [41, 41, 26, 56, 83, 40, 80, 70, 33]
    line10 = [41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
    line11 = [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
    line12 = [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
    line13 = [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
    line14 = [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
    line15 = [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]



    result = 0
    
    for i in range(1,15):
        
        result += max(line + i)
    return result

print(euler18())        
