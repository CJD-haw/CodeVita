
"""
Problem Statement:
    FULLY AUTOMATIC VENDING MACHINE - dispenses your cuppa on just press of button.
    A vending machine can serve range of products as follows:
        1. Coffee
            1. Espresso Coffee
            2. Cappuccino Coffee
            3. Latte Coffee
        2. Tea
            1. Plain Tea
            2. Assam Tea
            3. Ginger Tea
            4. Cardamom Tea
            5. Masala Tea
            6. Lemon Tea
            7. Green Tea
            8. Organic Darjeeling Tea
        3. Soups
            1. Hot and Sour Soup
            2. Veg Corn Soup
            3. Tomato Soup
            4. Spicy Tomato Soup
        4. Beverages
            1. Hot Chocolate Drink
            2. Badam Drink
            3. Badam-Pista Drink

Write a program to take input for main menu & sub menu,
And display the name of sub menu selected in the following format (enter the first letter to select main menu):

Welcome to CCD
Enjoy your

Example 1:

Input:
c
1
Output
Welcome to CCD!
Enjoy your Espresso Coffee!

Example 2:

Input
t
9
Output
INVALID OUTPUT!
"""

menu_list = ['Coffee', 'Tea', 'Soups', 'Beverages']
menu = {
    'Coffee': ['Espresso Coffee', 'Cappuccino Coffee', 'Latte Coffee'],
    'Tea': ['Plain Tea', 'Assam Tea', 'Ginger Tea', 'Cardamom Tea', 'Masala Tea',
            'Lemon Tea', 'Green Tea', 'Organic Darjeeling Tea'],
    'Soups': ['Hot and Sour Soup', 'Veg Corn Soup', 'Tomato Soup', 'Spicy Tomato Soup'],
    'Beverages': ['Hot Chocolate Drink', 'Badam Drink', 'Badam-Pista Drink'],
}

category = input()
if category not in 'cCtTsSbB':
    print('Invalid Input')
    exit()

number = int(input())
product = [menu[m] for m in menu_list if m[0].lower() == category[0] or m[0].upper() == category[0]][0]

if number in range(len(product)+1):
    print('Welcome To CCD!')
    print('Enjoy Your {}'.format(product[number-1]))
else:
    print('Invalid Input')
