print("Hello, world!")

def multiply_function(*args):
    result = 1

    for num in args:
        result *= args

    return result
