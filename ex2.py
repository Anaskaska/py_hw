n = int(input('Введите количество элементов списка '))
i = 0
my_list = []
new_list = []
while i < n:
    el = input("Введите элемент списка ")
    my_list.append(el)
    i += 1
print(f"Ваш список {my_list} ")
i = 0
while (i + 2) <= len(my_list):
    new_list.insert(i,my_list[i+1])
    new_list.insert(i+1,my_list[i])
    i += 2

if i+1 == len(my_list):
    new_list.insert(i, my_list[i])
print(f"Новый список {new_list} ")

