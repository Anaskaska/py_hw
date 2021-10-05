num = int(input("Введите количество товара "))
i = 1
goods = {}
list_goods = []
while i <= num:
    name = input('name ')
    price = input('price ')
    quantity = input ('quantity ')
    unit = input ('unit ')
    list_goods.append(
        (i, {"name": name,"price": price,"quantity": quantity,"unit": unit}))
    i += 1
dict_goods={}
i = 0
for numb, prod_dict in list_goods:
    for key, value in prod_dict.items():
        if not dict_goods.get(key):
            dict_goods[key] = [value]
        else:
            dict_goods[key].append(value)
for key, value in dict_goods.items():
    dict_goods[key] = list(set(value))
print(dict_goods)
