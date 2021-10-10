from functools import reduce

def product(a,b):
    return a * b

my_list = [i for i in range(100,1001) if i % 2 == 0]
my_product = reduce(lambda a, b: a * b, my_list)

print(my_list)
print(f"Произведение всех чисел списка = {my_product}")
my_product = reduce(product, my_list)
print(f"Произведение всех чисел списка = {my_product}")
