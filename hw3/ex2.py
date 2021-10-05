def print_str(name, surname, year_of_birth,
              city, email, tel):

    full_data = name + " " + surname + " " + str(year_of_birth) + " " + city + " " + email + " " + str(tel)
    print(full_data)
#    return full_data

my_name = input("name ")
my_surname = input("surname ")
my_year = input("year of birth ")
my_city = input("city ")
my_email = input("email ")
my_tel = input("tel ")

my_full_data = print_str(name=my_name, surname=my_surname, year_of_birth=my_year,
                         city=my_city, email=my_email, tel=my_tel)


