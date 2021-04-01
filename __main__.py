from time import time
from inspect import stack
import functools


password = 'correct horse battery staple'


# Capitalizes arguments before call
def upper(func):
    def wrapper(*args):
        args = [str(i).upper() for i in args]
        func(*args)
    return wrapper


# Calculates run time
def runtime(func):
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time()
        print('Run time: {} s'.format(end - start))
    return wrapper


# Requests password before call
def check_password(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Check for recursion
        if stack()[1][3] != func.__name__:
            if input('Password: ') == password:
                return func(*args, **kwargs)
            else:
                return 'Access denied.'
        return func(*args, **kwargs)
    return wrapper


# Caches previous results
def cached(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args in cache.keys():
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper


# Testing
if __name__ == '__main__':
    print = upper(print)
    print('Demonstration of new print()')

    pow_runtime = runtime(pow)
    pow_runtime(2, 3)


    @check_password
    @cached
    def fib(n):
        if n <= 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
    print(fib(100))
