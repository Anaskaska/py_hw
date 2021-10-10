def my_func_1(x_1, y_1):
    result = x_1 ** y_1
    return result
def my_func_2(x_1,y_1):
    count = 2
    result = x_1
    while count <= abs(y_1):
        result *= x_1
#        print(f"{count}, {result}")
        count += 1
    result = 1 / result
    return result


x = abs(float(input("Input x > 0 ")))
y = - abs(int(input("Input y < 0 (integer) ")))
print(f"The first method: {x} ^ {y} = {my_func_1 (x,y)}")
print(f"The second method: {x} ^ {y} = {my_func_2 (x,y)}")




