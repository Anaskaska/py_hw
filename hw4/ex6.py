from itertools import count, cycle

list_int = []
for el in count(3):
    if el > 10:
        break
    else:
        list_int.append(el)

print(list_int)

list_new = []
c = 0
for el in cycle("ABCDEFG"):
    if c > 10:
        break
    list_new.append(el)
    c += 1
print(list_new)


