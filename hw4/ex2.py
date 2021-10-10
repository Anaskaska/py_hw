begin_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list = [begin_list[i] for i in range(1, len(begin_list))
            if begin_list[i] > begin_list[i-1]]
print(new_list)
