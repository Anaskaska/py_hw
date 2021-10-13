my_list = []
count_string = 0
with open("test1.txt") as file:
    for string in file:
        my_list = string.split()
#        print(my_list)
        count_string += 1
        print(f' В строке {count_string}  {len(my_list)} слов')
    print(f"Всего в файле {count_string} строк ")