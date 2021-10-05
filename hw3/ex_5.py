def num_sum(list_1, stopper):
    num_summa = 0
    for num in list_1:
        if num == stopper:
            break
        num_summa += int(num)
    return num_summa

i = 0
my_num_sum = 0
stop_signal = "~"
flag = False
while not flag:
    my_str = input("Введите числа, разделенные пробелом, нажмите ~ для завершения ввода ")
    my_list = my_str.split(" ")
    my_num_sum += num_sum(my_list, stop_signal)
    flag = stop_signal in my_list
    print(f"{my_num_sum}")

print(f"Сумма чисел до знака {stop_signal} : {my_num_sum}")


