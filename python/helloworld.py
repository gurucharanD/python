# print('hello world')
# print(list1)
# list2=list1.append(5)
# list1.pop(1)
# print(list1)
# print(a_dict['a'])

list1=[1,2,3]
a_dict={
    'a':13,
    'b':2,
    'c':3
}

for i in list1:
    print(i)

for i in range(len(list1)):
    print(list1[i])

for i in a_dict:
    print(a_dict[i])

a=1
b=2
print(a==b)
print(a is b)

c= not b
print(c)