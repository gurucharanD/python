def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result


def create_cubes_gen(n):
    result = []
    for x in range(n):
        yield x**3


# for i in create_cubes_gen(10):
#     print(i)


def fibo(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a+b


# for i in fibo(10):
#     print(i)
# print(list(fibo(10)))


def random(x, y):
    for x in range(y):
        yield x


# print(list(random(1, 10)))


mylist = [1, 2, 4, 5, 6]
gencomp = (item for item in mylist if item > 3)
print(gencomp)
for item in gencomp:
    print(item)
