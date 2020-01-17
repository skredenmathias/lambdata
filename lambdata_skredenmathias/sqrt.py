def lazy_sqrt(x):
    """takes x and returns x square root"""
    return x**0.5


def builtin_sqrt(x):
    """uses python builtin math function to return square root of x"""
    from math import sqrt
    return sqrt(x)


def newton_sqrt1(x):
    """Return the square root of x using Newton's method"""
    val = x
    while True:
        last = val
        val = (val + x / val) * 0.5
        if abs(val - last) < 1e-9:
            break
    return val
