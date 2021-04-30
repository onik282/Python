my_list = []
while True:
    line = input("начинаем вводить: ")
    if line == '':
        print(my_list)
        exit()
    else:
        newline = line + '\n'
        my_list.append(newline)

    with open("text.txt", "w") as file_obj:
        file_obj.writelines(my_list)