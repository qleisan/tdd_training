def fizzbuzz(n):
    ret = ""
    if n % 3 == 0:
        ret = "Fizz"
    if n % 5 == 0:
        ret += "Buzz"
    if ret == "":
        ret = n
    return ret
