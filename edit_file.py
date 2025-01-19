#Read
#file = open("file.txt", "r")  # r is used to read a file
#lines = file.readlines()  # read the file
#file.close()  # close the file

#Edit
#lines = ["Hello\n", "World\n", "Python\n"]  # list of lines to write to the file
#lines.insert(0, "New line\n")  # insert a new line at index 1

#lines.append("New last line\n")  # append a new line at the end of the list


#Write
#file = open("file.txt", "w")  # w is used to write to a file, if file already exists it will overwrite the file
#file.writelines(lines)
#file.close()  # close the file

#Excersice

# Read the existing numbers from the file
with open("Numbers.txt", "r") as file:
    numbers = file.readlines()

# Convert the numbers to integers and multiply by 2
new_numbers = [str(int(number.strip()) * 2) + "\n" for number in numbers]

# Write the new numbers to the file, overwriting the original content
with open("Numbers.txt", "w") as file:
    file.writelines(new_numbers)