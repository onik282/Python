def division (a, b):
    try:
        c =  a / b
        return c
    except ZeroDivisionError:
        return "y is'n be a zero"
    except ValueError:
        return "enter only number"
print(division(int(input("введите первое число = ")), int(input("введите второе число = "))))