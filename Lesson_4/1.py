from sys import argv

chas, stavka, premia = argv

print("сколько наработали часов: ", chas)
print("какая ставка: ", stavka)
print("сколько премия: ", premia)

print("Зарплата сотрудника: ", (float(chas) * float(stavka)) + float(premia))