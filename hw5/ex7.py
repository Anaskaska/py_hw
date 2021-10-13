import json
with open("test7_in.txt") as file:
    profit_ave = 0
    n = 0
    firm_dict ={}
    for string in file:
        string_file = string.split()
        if string_file != '':
#            print(string_file)
            profit = float(string_file[2]) - float(string_file[3])
            if profit > 0:
                profit_ave += profit
                n += 1
            firm_dict.update({string_file[0] : profit})
profit_ave = profit_ave / n
result = [firm_dict, {'average_profit': profit_ave}]
#print(result)
with open("test7_out.json", 'w') as file_out:
    json.dump(result, file_out)

