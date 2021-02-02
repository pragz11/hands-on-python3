#Reverse a string in different ways

## Method #1 : Using simple looping mechanism
def reverse(s): 
    str = "" 
    for i in s: 
        str = i + str
    return str
  
txt = "Welcome here!"
  
print ("Original string  is :{} ".format(txt))  
print ("Reversed string(using loops) is : {}".format(reverse(txt)))
# print (reverse(txt))

## Method #2: Extended slice syntax
msg = 'Use extended slice'
print("Original Msg before using slice: {}".format(msg))
msg=msg[::-1]
print("Reverse Msg after using slice: {}".format(msg))
