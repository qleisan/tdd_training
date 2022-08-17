# refresh on decorators...

def g(func, *args, **kwargs):
    def inner(*args, **kwargs):
        print("Greetings from g()")
        for arg in args:
            print(arg)
        for kwarg in kwargs:
            print(kwarg, kwargs[kwarg])

        return func(*args, **kwargs)
    return inner


@g # or f=g(f) somewhere else
def f(msg, a=1, b=2):
    print(f"Greetings from f() {msg} {a} {b}")
    return a+b


# print("1----------------")
# g(f)("Hello")
# print("2----------------")
# f=g(f)
# f("Again")
# print("3----------------")

print(f("More", b=4))

