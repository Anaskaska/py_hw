
sum_salary = 0
count_string = 0
low_salary_name = []
with open("test2.txt") as file:
    for string in file:
        my_list = string.split()
        if float(my_list[1]) < 20000:
            low_salary_name.append(my_list[0])
        sum_salary += float(my_list[1])
        count_string += 1
#print(f" Total sum:  {sum_salary}, {count_string} people")
print(f"Salary < 20000 has  {len(low_salary_name)} people: ")
for i in range(len(low_salary_name)):
    print(f" {low_salary_name[i]}", end =" ")
print()
print(f"Average salary is {sum_salary/count_string:2}")