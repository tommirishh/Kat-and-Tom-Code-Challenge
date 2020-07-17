#CHALLENGE
#Given a list of numbers and a number k, 
#return whether any two numbers from the list add up to k.

#For example, given [10, 15, 3, 7] and k of 17, 
#return true since 10 + 7 is 17

#NOTES
#got this running with O(n^2)
#works for any length of list 

#Bonus - do this in one pass
#I tested my function and the time taken to run it increases quadratically 
#I did some research to find a more efficient solution for this bonus 
#This page explained a more efficient algorithm
#https://stackoverflow.com/questions/51300360/given-a-list-of-numbers-and-a-number-k-return-whether-any-two-numbers-from-the

def list_add2(x,lis):
    
    #items need to be in size order
    lis.sort()
    
    i=0
    j=len(lis)-1
    
    # if i meets j all numbers have been tested 
    while i<j:
        #if the sum of 2 numbers is too small try the next smallest number
        if lis[i]+lis[j]<x:
            i=i+1
        #if the sum of 2 numbers is too big try the next largest number    
        elif lis[i]+lis[j]>x:
            j=j-1
        #if the sum is equal then return true    
        else: return True

    return False
