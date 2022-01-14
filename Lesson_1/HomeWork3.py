n = 0

while(n <1 or n > 9):
    n = int(input("Введите число от 1 до 9:"))

nn = n*10+n
nnn = nn*10+n
s = n + nn + nnn
print(s)