# Написать программу, которая из имеющегося массива строк формирует массив из строк,
# длина которых меньше либо равна 3 символа.


mas = ["hello", "2", "world", ":-)"]
i = 0
newMas = []

while (i < len(mas)):
    if (int(len(mas[i]) <= 3)):
        newMas.append(mas[i])
        i= i + 1
    else:
        i = i + 1
        
print(newMas)    