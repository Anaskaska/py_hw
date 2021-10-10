def my_func(num_1, num_2, num_3):
    if (num_3 < num_1) and (num_3 < num_2):
        sum_num = num_1 + num_2
    elif (num_3 > num_2) and (num_1 > num_2):
        sum_num = num_1 + num_3
    else:
        sum_num = num_2 + num_3
    return sum_num

a = int(input(" a = "))
b = int(input(" b = "))
c = int(input(" c = "))
print(my_func(a, b, c))