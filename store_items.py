# -*- coding: utf-8 -*-
"""store_items

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12NiU7DIQXsfEIHtEUffM5MOXKQZ5ttL6
"""

#CS 175
#Maggie Volker

#constant variables
myName = "Maggie"
item1 = "Burger"
item2 = "Fries"
item3 = "Tacos"
taxRate = .1
fee = 2.99

#declaring variables
item1Cost = 0
item2Cost = 0
item3Cost = 0
subTotal = 0
taxAmount = 0
grandTotal = 0

#setting variables
item1Cost = float(input(f"Enter the cost of the {item1}: $"))
item2Cost = float(input(f"Enter the cost of the {item2}: $"))
item3Cost = float(input(f"Enter the cost of the {item3}: $"))
subTotal = item1Cost + item2Cost + item3Cost
taxAmount = subTotal * taxRate
grandTotal = subTotal + taxAmount + fee

#display
print('My', item1, 'is delicious and it cost me $',item1Cost)
print('My', item2, 'is delicious and it cost me $',item2Cost)
print('My', item3, 'is delicious and it cost me $',item3Cost)

#printing subTotal, taxAmount, fee, and grandTotal on 4 separate lines
print('The subtotal is $', subTotal)
print(f"The tax is $"f'{taxAmount: .2f}')
print('The shipping fee is $', fee)
#last line using variable myName to print the grandTotal
print(f'{myName}',"paid the final bill of $"f'{grandTotal: .2f}')