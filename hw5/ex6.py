

my_dict = {}
with open("test6_in.txt") as file:
    for string in file:
        h_int = 0
        my_list = string.split()
#        print(my_list)
        for h in my_list[1:]:
            if h != '-':
                num = '0'
                for i in h:
                    if i.isdigit():
                        num += i
                    else:
                        break
                h_int += int(num)
        my_dict.update({my_list[0].strip(':'): h_int})
    print(my_dict)