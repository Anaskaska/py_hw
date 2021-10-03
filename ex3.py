month = int(input("Введите номер месяца (от 1 до 12) "))
my_list =["зима","весна", "лето", "осень"]
my_dict = {1:my_list[0], 2:my_list[0], 3:my_list[1],
           4:my_list[1], 5:my_list[1], 6:my_list[2],
           7:my_list[2], 8:my_list[2], 9:my_list[3],
            10:my_list[3], 11:my_list[3], 12:my_list[0]}

print(my_dict.get(month))