import re

class StringCalc():
    def add(self, numbers):
        if numbers == "":
            return 0
        separators = r",|\n"
        if numbers[0:2] == "//":
            separator_end = numbers.index("\n")
            separators += "|" + numbers[2:separator_end]
            numbers = numbers[separator_end+1:]
        number_list = re.split(separators, numbers)
        total = 0
        for number in number_list:
            print("number =" + number)
            total += int(number)
        return total


