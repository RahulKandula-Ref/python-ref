# functions with default valued parameters
def hello_world(name = 'world'):
    print('Hello ' + name)

hello_world()

hello_world('nini')


def do_sum(n1 = 0, n2 = 0):
    if type(n1) is not int or type(n2) is not int:
        return
    return n1 + n2

print(do_sum('1', 1))
print(do_sum())



# args and kwargs
def multiple_args(*args):
    print(args)
    print(type(args))

multiple_args(12, 34, 55)

def multiple_named_args(**kwargs):
    print(kwargs)
    print(type(kwargs))

multiple_named_args(first='nihi', last='anap', alias='nini')