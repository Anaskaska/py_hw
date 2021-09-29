my_proceeds = int(input('input your proceeds '))
my_costs = int(input('input your costs '))
my_profit = my_proceeds - my_costs
if my_proceeds > my_costs and my_proceeds > 0:
    print('Congratulations! You have success! Your have a profit! ')
    print('your profit is ', my_profit)
    profitable = my_profit / my_proceeds * 100
    print('your profitable is ', profitable, '%')
    quantity = int(input('input your quantity of person '))
    profit_per_person = my_profit / quantity
    print('your profit per person is ', profit_per_person)
else:
    print('you spend too much!')

