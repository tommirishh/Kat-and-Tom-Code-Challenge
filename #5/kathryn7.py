#Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, 
#count the number of ways it can be decoded.

#For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

#first attempt I made a function for len 3
def translate3(x):

    #counter starts at 1 as anything could be read once
    n=1 

    for i in range(0,2):
        if x[i]==1:
            n=n+1
        if x[i]==2:
            if int(x[i+1])<7:
                   n=n+1

    return n 

print translate3([1,1,1])

#222222 ->
# 2 2 2 2 2 2  6c6 = 1
# 22 2 2 2 2   5c1 =5
#...
# 2 2 2 2 22   
# 22 22 2 2    4c2 = 6
# 22 2 22 2
# 22 2 2 22
# 2 22 2 22
# 2 2 22 22 
# 2 22 22 2

# 22 22 22     3c3 = 1


#22222 -> 
#2 2 2 2 2  1 = 5c5
#22 2 2 2   4 = 4c1
#2 22 2 2   
#2 2 22 2
#2 2 2 22
#22 22 2    3 = 3c2
#22 2 22
#2 22 22


#2222 ->
#2 2 2 2   1
#22 2 2    3
#2 22 2
#2 2 22
#22 22     1   