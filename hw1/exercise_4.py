n = int(input ("input positive integer number n "))
if n < 0:
    n = abs(n)

n_str = str(n)
max_n = 0
l_n_str = len(n_str)
# print (l_n_str)
i = 0
while i < l_n_str:
    t = int(n_str[i])
#    print(t)
    if max_n < t:
        max_n = t
    i = i + 1
print ("max number of n is ", max_n)

