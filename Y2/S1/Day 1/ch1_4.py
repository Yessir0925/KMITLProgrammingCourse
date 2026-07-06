"""
Write a function:  odd_list(alist):

The function should work as follows:

# Returns a list that contains only the odd numbers from alist

# For example, if alist = [10, 11, 13, 24, 25], the result should be [11, 13, 25]

Please modify from the following part of the code:"


def  odd_list ( al ): 
    # put your code here 


print ( " ***Function Odd List***" ) 
ls  = [ int ( e )  for  e  in  input ( "Enter list numbers : " ). split ()] 
print ( ls ) 
opls  =  odd_list ( ls ) 
print ( "Input list : " ,  ls ,  "\nOutput list : " ,  opls ) 

Then display the results as shown in the example.

 ***Function Odd List***
Enter list numbers : 1 2 3 4 5 6 7 8 9 10
Input list :  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
Output list :  [1, 3, 5, 7, 9]


"""


def  odd_list ( ls ): 
    for  i  in  ls : 
        if  i % 2 != 0 : 
            yield  i


print( " ***Function Odd List***" ) 
ls  = [ int ( e )  for  e  in  input ( "Enter list numbers : " ). split ()] 
opls  =  [ x for x in odd_list(ls) ] 
print ( "Input list : " ,  ls ,  "\nOutput list : " ,  opls ) 