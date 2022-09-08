def fizzbuzz(n):
    ret = ""
    if n % 3 == 0:
        ret = "Fizz"
    if n % 5 == 0:
        ret += "Buzz"
    if ret == "":
        ret = n
    return ret


def print_fizzbuzz_1_100(display_function):
    for i in range(1, 101):
        display_function(fizzbuzz(i))


print_fizzbuzz_1_100(print)
