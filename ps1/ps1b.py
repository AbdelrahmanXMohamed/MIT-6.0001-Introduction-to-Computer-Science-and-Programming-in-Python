# -*- coding: utf-8 -*-
"""
Created on Tue May 25 08:00:11 2021

@author: Xbenx
"""

current_savings = 0
annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home:​ "))
semi_annual_raise = float(input("Enter your semi-annual salary raise, as decimal:   "))
portion_down_payment=total_cost/4
r=0.04
no_of_months=0
while current_savings<portion_down_payment:
    if no_of_months%6==0 and no_of_months!=0:
        annual_salary+=annual_salary*semi_annual_raise
    current_savings += current_savings*r/12 + portion_saved*annual_salary/12
    no_of_months+=1

print(f"Number of months:​ {no_of_months}")