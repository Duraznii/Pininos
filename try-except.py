print("Try and Except")

try:
    #4 / 0
    #print(name)
    #print(age)
    "Hello" + 5
except NameError as e:
    print("An error occurred")
    print(e)
except ZeroDivisionError:
    print("Division by zero")
except:
    print("Something went wrong")   

def upper_myword(word):
    if len(word) < 3:
       # raise Exception("Word is too small")
        raise MyException("Word is tiny")
    return word.upper()

class MyException(Exception):
    pass

print(upper_myword("Cecilia"))
    
print("End of program")

