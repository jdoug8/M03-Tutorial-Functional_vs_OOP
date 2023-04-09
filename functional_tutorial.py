def subtract(x, y):
    return x - y

def divide(x, y):
    return x // y

def do_math(action, x, y):
    return action(x, y)

print(do_math(subtract, 10, 5))
print(do_math(divide, 10, 5))