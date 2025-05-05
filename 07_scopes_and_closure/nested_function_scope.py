x=98
def f1():
    x=88
    def f2():
        print(x) # it's called closure
    return f2
myRes = f1()
myRes()


def chaicoder(num):
    def actual(x):
        return x**num
    return actual
f = chaicoder(2)
g=chaicoder(3)
print(f(3))
print(g(3))