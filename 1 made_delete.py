# f = lambda x: (
#     x + 1
# )

# def super(func):
#   return func

# def duper(arg):
#   return arg

# def cool(arg):
#   return arg

# @super
# @duper
# @cool
# def stuff():
#     pass
  
# stuff = super(duper(cool(stuff)))

# stuff = cool(stuff)
# stuff = duper(stuff)
# stuff = super(stuff)
import time

def retry(func):
    def _wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            time.sleep(1)
            func(*args, **kwargs)
    return _wrapper

@retry
def might_fail():
    print("might_fail")
    raise Exception

might_fail()