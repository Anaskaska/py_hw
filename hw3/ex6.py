def int_func(word):
    new_word = word[0].upper() + word[1:].lower()
    return new_word

my_str = input("Введите строку из слов, разделенных пробелом: ")
my_list = my_str.split()
my_new_list = []
for txt in my_list:
#    print(f" {int_func(txt)}", end=" ")
    my_new_list.append(int_func(txt))

my_new_str = " ".join(my_new_list)
print(my_new_str)


