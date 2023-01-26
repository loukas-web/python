my_list = [1, 2, 3, 4, 5, 6]

a = iter(my_list)

print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))


# generators
def reverse():
    for i in range(5):
        yield i


b = reverse()

print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))

# map functions map(func, *iterables)
mylist = [10, 20, 30]
c = map(lambda element: element + 5, mylist)

print(next(c))
print(next(c))
print(next(c))

# filter functions filter(func, iterable) yes or no

grades = [20, 80, 100, 50, 60, 70]


def pass_grade(grade):
    return grade > 50


passed = list(filter(lambda grade: grade > 50, grades))

print(passed)
