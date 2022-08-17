import re

class CustomException(Exception):
    pass

class StringCalc():
    def __init__(self, displaydriver=None):
        if displaydriver is None:
            self.displaydriver = print
        else:
            self.displaydriver = displaydriver

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
        outstr = ""
        for number in number_list:
            if int(number) < 0:
                raise CustomException("Negatives not allowed: " + number)
            # print("number =" + number)
            outstr += number + " + "
            total += int(number)
        # remove last " + " and add total
        outstr = outstr[:-3] + " = "+str(total)
        #print(outstr)
        self.displaydriver(outstr)
        return total


# real test mocks display, check that the real thing works
sc=StringCalc()
sc.add("1,2,3,4")
