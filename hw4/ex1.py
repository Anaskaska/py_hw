from sys import argv

def salary (output_in_hours, rate_per_hour, prize):
    salary = (output_in_hours * rate_per_hour) + prize
    return salary

my_salary = salary(float(argv[1]),float(argv[2]),float(argv[3]))
print (f"Salary is {my_salary}")


