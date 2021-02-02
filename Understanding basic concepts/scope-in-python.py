## Learning and understanding scope of your variables 
##  L(Local), E(Enclosing block), G(Global), Built-in variables(ex- len)

my_fav_fruit='Mango' #Declared in global scope

def find_my_fav_fruit():
    my_fav_fruit ='Banana' #in local scope now
    print ("My favourite fruit(local scope for find_my_fav-fruit() function): {}".format(my_fav_fruit))

    def change_my_fav():
        #If python does not find my_fav_fruit inside this function, it then looks this variable in the parent function's enclosing block
        print ("My favourite fruit(finds enclosed in find_my_fav-fruit() function): {}".format(my_fav_fruit))
    
    change_my_fav()

print("My favourite fruit (global scope): {}".format(my_fav_fruit)) #Executes first

find_my_fav_fruit() 

