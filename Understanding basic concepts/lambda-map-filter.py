''' 
#map - (expects func and some iterable obj)
#filter - filters by a function that returns either true or false--> returns items of the iterables
#lambda - A lambda function can take any number of arguments, but can only have one expression. 
        Anonymous function: use once and never reference again
        Use lambda functions when an anonymous function is required for a short period of time.
'''
#-------------------------Understanding map

########Example 1:

#Simple function to square a number
def square(num):
    return num**2

my_list =[1,2,3,4,5]
print("My list of number to be squared:",my_list)
###First Method to find the squares of the number in above list
#using loops 
print('Squared number:map using loops')
for item in map(square,my_list):
    print(item) #prints individual elements


###Second Method: 

#Notice that we calling the function inside map without paranthesis
#By passing the map function inside list(), it returns a list of squared number  
print('List of squared number (using map):',list(map(square,my_list)))
#Assign it to another variable
squared_list=list(map(square,my_list))

######Example 2:

#Works for strings too

#Simple function returning 'EVEN' if string length is even or returns the first element of string, if otherwise.
def splicer(mystr):
    if len(mystr)%2 ==0:
        return 'EVEN'
    else:
        return mystr[0]

names=['Andy','Amy','Andrew']

print("Use of map on string: ",list(map(splicer,names)))


#---------------------------------Filter Function 

#Function returning true if number is even else returns false
def check_even(num):
    return num%2 == 0

mynums =[1,2,3,4,5,6]


###First Method
print('Check even number:filter using loops')
for item in filter(check_even,mynums):
    print(item)

###Second Method
print('original number list:',mynums)
#filter based of check_even
print('List of even numbers from original list',list(filter(check_even,mynums)))

#Lambda function
'''This is how a lamba function looks like:
                        lambda x:x*2
                        Anonymous function
'''
#We can noe use lambda in combination of map and filter and shown below
print("List of Squared numbers(using map & lambda) : ",list(map(lambda num:num**2,my_list)))
print("List of even numbers(using filter & lambda) : ",list(filter(lambda num:num%2==0,mynums)))
