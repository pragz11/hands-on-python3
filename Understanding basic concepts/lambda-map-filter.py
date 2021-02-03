''' This lesson is under progress'''

#Anonymous function: use once and never reference again
#map -(expects func and some iterabke obj)
#filter-
#lamba -

#Unnderstanding map 
def square(num):
    return num**2

my_list =[1,2,3,4,5]

#Fist Method
for item in map(square,my_list):
    print(item)

#We are not calling the function with paranthesis
squared_list=list(map(square,my_list))
print(list(map(square,my_list)))

#2nd example
#Works for strings too
def splicer(mystr):
    if len(mystr)%2 ==0:
        return 'EVEN'
    else:
        return mystr[0]

names=['Andy','Amy','Andrew']
print(list(map(splicer,names)))


# Filter Function :- filters by a function that returns either true or false--> returns items of the iterables

def check_even(num):
    return num%2 == 0

mynums =[1,2,3,4,5,6]

for item in filter(check_even,mynums):
    print(item)

#filter based of check_even
print(list(filter(check_even,mynums)))

#Lambda function

print(list(map(lambda num:num**2,my_list)))
print(list(filter(lambda num:num%2==0,mynums)))
