
russian_list = ["Один", "Два", "Три", "Четыре"]
num = 0
with open("test4.txt") as file_in:
    with open("test4_out.txt","w") as file_out:
        for string in file_in:
            new_list = []
            new_list.append(russian_list[num])
            new_list.append(string.split()[1])
            new_list.append(string.split()[2])
            new_list.append("\n")
            file_out.writelines(' '.join(new_list))
            print(' '.join(new_list), end=" ")
            num += 1

