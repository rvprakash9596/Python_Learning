'''A closure is a function object that remembers values in enclosing scopes even if they are not in memory anymore. Closures allow functions to have "private" variables and create function factories.

Closure Requirements:
A nested function (function inside another function).

The inner function must refer to a variable from the enclosing function.

The outer function must return the inner function.'''


def outer(msg):
    def inner():
        print("Message:", msg)  # `msg` is a free variable captured in the closure
    return inner
my_func = outer("Hello")
my_func()  # Output: Message: Hello