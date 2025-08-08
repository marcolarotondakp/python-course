def product(x, y):
    result = 0
    while y > 0:
        result += x
        y -= 1
    return result


def product_recursive(x, y):
    result = 0
    if y != 0:
        result = product_recursive(x, y - 1) + x
    return result


counter = 0


def fibonacci(x):
    global counter
    counter += 1
    if x <= 1:
        return x
    return fibonacci(x - 1) + fibonacci(x - 2)
