#file = open("file.txt", "r")  # r is used to read a file

#file_text = file.read()  # read the file
#print(file_text)

#lines = file.readlines()    
#print(lines)
#
#for line in file:
 #   print(line)

#file.close()  # close the file


file = open("Numbers.txt", "r")  # r is used to read a file

total = 1

for line in file:
    try:
        number = int(line)
        total *= number
    except Exception as e:  #NameError
        print
        print('Only numbers are allowed')
        sys.exit()
        
print(total)

file.close()  # close the file