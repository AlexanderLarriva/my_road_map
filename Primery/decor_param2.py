from functools import wraps
def wrapped(function):
    @wraps(function)
    def inner(arg):
        return function(arg)
    return inner

def foo(_):
    """Bar."""
    return 42

foo = wrapped(foo)
print(foo)
# <function foo at 0x7f1057b15048>
#help(foo)