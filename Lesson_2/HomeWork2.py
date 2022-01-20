# обмен элементов списка
# В переменную запишим строку и разделим её на элементы при помощи split()
my_list = input("Введите значение элементов списка: ").split()

# Поменяем соседние элементы местами
for i in range(0, len(my_list)-1, 2):
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]


print(my_list)
