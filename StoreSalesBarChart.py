# Author: Matthew Spiller
# Date Modified: February 7, 2022

# SalesCommissionCalculator
# Description: Prints a bar graph using a set of asterisks (*) in the console. For every 100 stores, one asterisk is printed. Program ends when user passes "-1".

def print_bar(store_num, store_sales):
    if store_sales == -1:
        return
    else:
        bar = ""
        for i in range(int(store_sales / 100)):
            bar += "*"
        print("Store " + str(store_num) + ": " + bar)

sales = 0
stores = 1
while sales != -1:
    print("Enter today's sales for store " + str(stores) + ": ", end='')
    sales = int(input())
    print_bar(stores, sales)
    stores += 1

