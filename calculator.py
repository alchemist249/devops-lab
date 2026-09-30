
def add(a, b):
    """Return the sum of a and  b."""
    return a + b


def subtract(a, b):
    return a - b


while True:
    a, b = map(int, input().split())
    print(f"Sum is {add(a, b)}")
    print(f"Difference is {subtract(a, b)}")
