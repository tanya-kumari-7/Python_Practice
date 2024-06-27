# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 19:11:26 2024

@author: user
"""

# =============================================================================
# You work for a manufacturer, and have been asked to calculate the total
# profit made on the sales of a product. You are given a dictionary 
# containing the cost price per unit (in dollars), sell price per unit 
# (in dollars), and the starting inventory. Return the total profit made, 
# rounded to the nearest dollar.
# =============================================================================
dict_1={
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
  }

def Calculate_the_Profit_func(cost_price,sell_price,inventory):
    total_cost = inventory * cost_price
    total_sell = inventory * sell_price
    profit = total_sell - total_cost
    return f'proft is {round(profit)}'

result=Calculate_the_Profit_func(dict_1['cost_price'], dict_1['sell_price'], dict_1['inventory'])
print(result) 

