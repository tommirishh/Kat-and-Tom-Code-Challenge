#Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, 
#count the number of ways it can be decoded.

#For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

from scipy.special import comb

#function that splits string into list of pairs
#e.g "2222" -> [22,22,22]
def listsplit(x):
    
    list2 = []
    
    for i in range(0,len(x)-1):
        list2.append(int(x[i:i+2]))
        
    return list2

#function that sums combinations of possible translations
def countcombos(i):
    
    #if statement determines number of nCr to run 
    #even numbers e.g 4 go 4c4, 3c1, 2c2
    if (i%2)==0:
        c=i/2
    #odd numbers e.g 5 go 5c5, 4c1, 3c2
    else:
        c=(i-1)/2

    #all lengths start with nCn=1 
    n=1

    #perform remaining nCr and return total 
    for j in range(1,c+2):
        n=n+comb(i-j,j)

    return n



def translator(l):
    
    #get list of pairs
    c=listsplit(l)
    
    #d is counter of pairs <27 
    d=0
    
    #check each pair to see if it's less than 26
    for i in range(0,len(c)):
        if c[i]<27:
            d=d+1
    
    #the number of pairs <26 +1 can be put into 
    #earlier formula to determine possible combinations
    return countcombos(d+1)

#possible combos -> "1 2 3 4" "12 3 4" "1 23 4"
print translator("1234")

#possible combos -> "2999"
print translator("2999")

#possible combos -> "1 1 1" "11 1" "1 11"
print translator("111")

#possible combos -> "2 6 2 6" "26 2 6" "2 6 26" "26 26"
#ERROR returns 3 not 4
print translator("2626")