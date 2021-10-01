# def func():
#     return 1


# print(func())

def new_dec(org_func):
    def wrap_func():
        print('some code', 1+2)
        org_func()
        print('some code DONE', 1+2)
    return wrap_func


@new_dec
def needy():
    print('i need dec')


# decfun = new_dec(needy)
# decfun()
needy()
