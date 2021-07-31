#one.py

def func():
    print('This function is in one.py')

#comment the whole code below to call only the above method in another module
print('TOP LEVEL IN ONE.PY')

if __name__=='__main__':
    print('ONE.PY is being run directly') #python one.py
else:
    print('ONE.PY has been imported!') #being called somewhere in other module