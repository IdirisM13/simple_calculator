def add(a: int, b: int) -> int:
    return a + b

def sub(a: int, b: int) -> int:
    return a - b


def multiply(a: int, b: int) -> int:
    return a * b


def divide(a: int, b: int) -> int | None:
    try:
        return a // b
    except ZeroDivisionError:
        print("Санды 0 го болгону болбойт!")

