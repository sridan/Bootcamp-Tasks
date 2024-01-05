# This is an example python program of using Lists and Dictionaries.
# The user creates a predefined list called menu and predefined dictionaries for the stock and price.
# This program outputs the total stock value of the items in the menu.

menu = ['Cappuccino','Latte','Espresso','Mocaccino']

stock = {'Cappuccino' : 24,'Latte' : 34,'Espresso' : 20,'Mocaccino' : 16}

price = {'Cappuccino' : 3.50,'Latte' : 3.25,'Espresso' : 3.75,'Mocaccino' : 3.50}

total_stock = 0

for items in menu:

    item_value = (stock[items]*price[items])
    total_stock += item_value

print(f'Total Stock Value is:{total_stock}')