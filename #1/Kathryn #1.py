#CHALLENGE
#Given a list of numbers and a number k, 
#return whether any two numbers from the list add up to k.

#For example, given [10, 15, 3, 7] and k of 17, 
#return true since 10 + 7 is 17

#Bonus - do this in one pass

#NOTES
#got this running with O(n^2)
#works for any length of list 

def list_add(x,lis):
    
    #ends function if x isn't a number
    if isinstance(x,int)==False:
        return "input an integer as the first variable"
    
    #ends function if lis isn't a list    
    if isinstance(lis,list)==False:
        return "input a list as the second variable"
    
    #ends function if lis contains anything other than numbers    
    for i in range(0,len(lis)):
        if isinstance(lis[i],int)==False:
            return "input a list of integers as the second variable"

    
   # for loop to check each number
    for i in range (0,len(lis)):
        
        #check the difference between x and first list item
        y=x-lis[0]
        
        #remove list item 
        #this prevents false positive if lis[0]=x/2
        #also prevents second pass of number 
        lis.pop(0)
        
        #see if the difference is in the list
        if y in lis:
            return("True")
            
        
    if len(lis)==0:
        return("False")

print (list_add(17,[10,11,12,13,14]))
#result is false

print (list_add(20,[10,12,13,14]))
#result is false

print (list_add(20,[10,10,12,13]))
#result is true

print (list_add(5,[1,2,3,4]))
#result is true

print (list_add("q",[1,2,3,4]))
# result is "input an integer as the first variable"

print (list_add(2,3))
# result is "input a list as the second variable"

print (list_add(2,[1,2,3,"q"]))
# result is "iput a list of integers as the second variable"
