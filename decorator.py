# refresh on decorators...

def f(msg):
    print(f"Greetings from f() {msg}")

def g(func, *args, **kwargs):
    def inner(*args, **kwargs):
        print("Greetings from g()")
        for arg in args:
            print(arg)
        for kwarg in kwargs:
            print(kwarg, kwargs[kwarg])

        func(*args, **kwargs)
    return inner

print("1----------------")
g(f)("Hello")
print("2----------------")
f=g(f)
f("Again")
