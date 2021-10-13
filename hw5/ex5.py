from random import randint

n = 10
sum = 0
with open("test5_in.txt", "w+") as file_in:
    for i in range(1,n+1):
        file_in.write(f" {str(randint(0,100))} ")

    file_in.seek(0)
    n = 0
    for string in file_in:
        my_list = string.split()

        for i in my_list:
            sum += int(i)
            n += 1
average = sum / n
print(f" Сумма всех чисел в файле равна: {sum}")
