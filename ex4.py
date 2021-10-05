my_str = input("Введите вашу строку из нескольких слов с пробелами ")
n_str = my_str.count(" ")
#print (f" В строке было {n_str} пробела(ов) ")
i = 0
list_word = my_str.split()
for ind, el in enumerate(list_word):
    print(ind+1, el[:10])

