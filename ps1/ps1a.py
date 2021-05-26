# -*- coding: utf-8 -*-
"""
Created on Tue May 25 06:44:31 2021

@author: Xbenx
"""

current_savings = 0
annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home:​ "))
portion_down_payment=total_cost/4
r=0.04
no_of_saved=0
while current_savings<portion_down_payment:
    
    current_savings += current_savings*r/12 + portion_saved*annual_salary/12
    no_of_saved+=1

print(f"Number of months:​ {no_of_saved}")