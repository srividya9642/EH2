# using raise keyword
print("good morning")

try:
    raise ZeroDivisionError
except:
    print("we  are raising runtime error")
    print("good evening")
    