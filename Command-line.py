import sys


#for arg in sys.argv:
 #   print(arg)


#Exercise

total = 1
del sys.argv[0]
for arg in sys.argv:
    try:
        #number = int(arg)
        number = float(arg)
        total *= number
    except Exception as e:  #NameError
        print
        print('Only numbers are allowed')
        sys.exit()
        
print(total)




