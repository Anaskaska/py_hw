def my_div(num_1, num_2):

    """
     result = num_1 / num_2
    :param num_1: float
    :param num_2: float
    :return : float
    """
    if num_2 == 0:
        print("Division by zero! ")
        return None
    else:
        return num_1/num_2

int_1 = int(input("Input num_1 "))
int_2 = int(input("Input num_2 "))
result = my_div(int_1, int_2)
print(f" num_1/num_2 =  {result}")

