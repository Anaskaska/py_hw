rating = [7, 5, 3, 3, 2]
new_el = int(input("Введите новый элемент рейтинга (целое число) "))
index_new = 0
while new_el <= rating[index_new]:
        index_new  += 1
        if index_new == len(rating):
                break
#print(index_new)
rating.insert(index_new, new_el)
print(rating)

