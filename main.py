
def invest(start, money_per_year, year_plan):
    count_of_money = start
    for i in range(0, year_plan):
        count_of_money += (count_of_money/100) * 14
        count_of_money += money_per_year

    return count_of_money

print(invest(10000, 108000, 15))
