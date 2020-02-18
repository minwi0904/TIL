import math

def sqrt_root(x):
    start = 1
    y = x
    while True:
        middle = (start + y) / 2
        if math.isclose((middle * middle), x) == False:
            if middle**2 >= x:
                y = middle
            else:
                start = middle
        else:
            return middle

print(sqrt_root(3))