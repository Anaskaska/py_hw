def fact(num):
    factorial = 1
    for i in range(1, num+1):
        factorial *= i
#        print(factorial)
    yield factorial

n = int(input("Input n: "))
for i in range(1, n+1):
    for el in fact(i):
        print(f" {i}: {el}")

