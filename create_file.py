#file = open("file.txt", "x")   # x is used to create a file, if file already exists it will give an error

#file.write("X marks the spot")      

#file.close()


#file = open("file.txt", "w")  # w is used to write to a file, if file already exists it will overwrite the file

#file.write("Re-escrito")      

#file.close()

#file = open("file.txt", "a")  # a is used to append to a file, if file already exists it will append to the file

#file.write("y más texto")      

#file.close()


#Exercise 

import sys

file_name = sys.argv[1]

file = open(f"{file_name}.txt", "x")   # x is used to create a file, if file already exists it will give an error

file.close()







