class StringCalc():
    def add(self, numbers):
        if numbers == "":
            return 0
        number_list = numbers.split(",")
        total = 0
        for number in number_list:
            total += int(number)
        return total

