# -*- coding: utf-8 -*-
"""
Created on Wed May 26 11:07:56 2021

@author: Xbenx
"""
def saving(current_savings , portion_down_payment , annual_salary , semi_annual_raise , guessed_savings_rate,no_of_months=36):    
    for number_of_months in range(0 , no_of_months):
        if number_of_months % 6 == 0 and number_of_months != 0:
            annual_salary += annual_salary * semi_annual_raise            
        current_savings += guessed_savings_rate * annual_salary / 12 + current_savings * 0.04 / 12                        
    return current_savings

current_savings = 0
annual_salary = int(input("Enter the start salary: "))
total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment=0.25*total_cost
r=0.04
no_of_months=36
low=0
high=10000
mid,mid_rate=0,0
current_savings = saving(0,portion_down_payment,annual_salary,semi_annual_raise,1)
no=0
if current_savings<portion_down_payment:
    print("It is not possible to pay the down payment in three years.")
else:

    current_savings=saving(0,portion_down_payment,annual_salary,semi_annual_raise,mid_rate)
    while abs(portion_down_payment-current_savings)>=100:
        mid=(low+high)//2
        mid_rate=mid/10000
        current_savings=int(saving(0,portion_down_payment,annual_salary,semi_annual_raise,mid_rate))
        if portion_down_payment > current_savings:
            low=mid
        else:
            high=mid
        no+=1
    
        
    print(f"Best savings rate:​ {mid_rate}")
    print(f"Steps in bisection search:​ {no}")
    
    
    
    
    
    '''  current_savings=saving(0,portion_down_payment,annual_salary,semi_annual_raise,mid_rate)
    while abs(current_savings-portion_down_payment)>=100:
        mid=int((low+high)/2)
        mid_rate=mid/10000
        current_savings=int(saving(0,portion_down_payment,annual_salary,semi_annual_raise,mid_rate))
        if portion_down_payment > current_savings:
            low=mid
        else:
            high=mid
        no+=1'''