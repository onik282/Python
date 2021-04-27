spisok = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 1]
spisok2 = [el for el in spisok if spisok.count(el) == 1]
print(spisok2)