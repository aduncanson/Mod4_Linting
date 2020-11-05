def less_than(x, y):

    print("The function has started!")

    # Checks if x is less than y
    if x < y:
        print("%s is less than %s"%(x, y))
    else:
        print("%s is not less than %s"%(x, y))

    print("The function has ended!")

def more_than(x, y):

    print("The function has started!")

    # Checks if x is less than y
    if x > y:
        print("%s is more than %s"%(x, y))
    else:
        print("%s is not more than %s"%(x, y))

    print("The function has ended!")

def equal_to(x, y):

    print("The function has started!")

    # Checks if x is equal to y
    if x == y:
        print("%s is equal to %s"%(x, y))
    else:
        print("%s is not equal to %s"%(x, y))

    print("The function has ended!")

# Call some functions
less_than(10, 15)
more_than(10, 15)
equal_to(10, 15)
