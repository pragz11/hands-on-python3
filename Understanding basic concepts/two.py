#two.py

import one

print('TOP LEVEL IN TWO.PY')

one.func()

if __name__=='__main__':
    print('TWO.PY is being run directly !')#python two.py
else:
    print('TWO.PY has been imported!') #Being called from other module since it is imported