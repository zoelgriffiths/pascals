#Use this code to find which numbers repeat an interesting number of times in Pascal's triangle.

import math 

def search(row_limit):
    list_numbers = []
    
    #Below I am dictating the rows and columns I will compute cell values for. 
    
    #(I have excluded the outer two diagonals (on either side) of Pascal's triangle, because we know that the numbers in those diagonals (across the whole triangle) are an infinite number of 1s and two appearances of all other positive integers apart from 2 (for which there is only one appearance).)
    
    for n in range(4,row_limit):
        for r in range(2,n-1):
            nCr = math.factorial(n)/(math.factorial(n-r)*math.factorial(r))
            list_numbers.append(nCr)
    
    set_numbers = set(list_numbers)
    how_many_times = []
    which_ones = []
    
    #Below I am checking how many times each distinct number appears in the cells we've generated. If a number appears more than twice (therefore more than four times across the whole triangle) I am storing both the number and the minimum number of times it appears across the whole triangle.
    
    for number in set_numbers:
        count = list_numbers.count(number)
        if count >= 3:
            how_many_times.append(count+2)
            which_ones.append(number)
        
    final_info = dict(zip(which_ones,how_many_times))
    
    for entry,frequency in final_info.items(): 
        print ("The number {0} appears at least {1} times across the whole triangle".format(entry,frequency))
        
    return "END"

search(501)
