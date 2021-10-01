import datetime
name = 'guru'
print('hi {name}'.format(name=name))

print(datetime.date.today())
print(datetime.time(2, 3, 4))

print('{date.day}/{date.month}/{date.year}'.format(date=datetime.date.today()))


def print_Name(name):
    print('hello {name}'.format(name=name))


print_Name('guru')
print_Name('charan')
elements = [1, 2, 4, 5, 6]
key = 6


def binary_search(elements, left, right, key):
    mid = (left+right)/2
