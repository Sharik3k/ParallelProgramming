custom_power = lambda x=0, /, e=1: x ** e


def custom_equation(
    x: int = 0,
    y: int = 0,
    /,
    a: int = 1,
    b: int = 1,
    *,
    c: int = 1
) -> float:
    """
    Calculates the equation (a*x + b*y) / c.

    :param x: first integer value
    :param y: second integer value
    :param a: multiplier for x
    :param b: multiplier for y
    :param c: divisor value
    :return: result of the equation
    """

    values = [x, y, a, b, c]

    for value in values:
        if not isinstance(value, int):
            raise TypeError("All parameters must be integers")

    return (a * x + b * y) / c


counter = 0


def fn_w_counter() -> (int, dict[str, int]):
    global counter

    counter += 1
    module_name = __name__

    return counter, {module_name: counter}
