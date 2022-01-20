my_str = input("Введите несколько слов разделяя их пробелами: ").split()

for i in range(0, len(my_str)):
    print(f"{i+1}. {my_str[i][:10]}")
