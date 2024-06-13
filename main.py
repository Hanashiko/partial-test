from functools import partial

def func(a: int, b: int, c: int, x: int) -> int:
    return 1000 * a + 100 * b + 10 * c + x

g: int = partial(func, 4, 11, 9)

print(g(5))

def power(a: int, b: int) -> int:
    return a**b

pow2 = partial(power, b=2)
pow4 = partial(power, b=4)
power_of_5 = partial(power, 5)

print(power(2, 3))
print(pow2(4))
print(pow4(3))
print(power_of_5(2))

print(f"{pow2.func = }")
print(f"{pow2.keywords = }")
print(f"{power_of_5.args = }")
