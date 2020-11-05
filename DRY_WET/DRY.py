def less_than(x, y):

    # Checks if x is less than y
    if x < y:
        print("%s is less than %s"%(x, y))
    else:
        print("%s is not less than %s"%(x, y))

def more_than(x, y):

    # Checks if x is less than y
    if x > y:
        print("%s is more than %s"%(x, y))
    else:
        print("%s is not more than %s"%(x, y))

def equal_to(x, y):

    # Checks if x is equal to y
    if x == y:
        print("%s is equal to %s"%(x, y))
    else:
        print("%s is not equal to %s"%(x, y))

def wrapper(func, x, y):

    print("The function has started!")

    # Calls the function
    func(x, y)

    print("The function has ended!")

# Call some functions
wrapper(less_than, 10, 15)
wrapper(more_than, 10, 15)
wrapper(equal_to, 10, 15)
