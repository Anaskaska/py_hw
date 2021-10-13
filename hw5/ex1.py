
with open("text.txt", "w") as file:
    while True:
        name = input("input the name ")
        file.writelines(f"{name} \n")
        if name == '':
            break




