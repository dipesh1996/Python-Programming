inputnumb = int(input("Enter Number for FizzBuzz:: "))


def fizz_buzz(numb):
    if (numb % 3 == 0) and (numb % 5 == 0):
        return "FizzBuzz"
    if numb % 3 == 0:
        return "Fizz"
    if numb % 5 == 0:
        return "Buzz"
    else:
        return numb


print(fizz_buzz(inputnumb))
