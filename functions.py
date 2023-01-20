def myfunc1(x):
    return x + 5

print(myfunc1(10))

def myfunc2(x, y, z):
    return x + y + z

print(myfunc2(5, 10, 15))

def myfunc3(*x):
    return sum(x)

print(myfunc3(1, 2, 3, 4))