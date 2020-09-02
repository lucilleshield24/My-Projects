#write function, using yield to return #s 1-10
def func():
    for x in range(0, 9):
        print("Hi there!")
        yield x+1