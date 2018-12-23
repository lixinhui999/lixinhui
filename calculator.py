#!/usr/bin/env python3


import sys

salary = float(sys.argv[1])
insurance = 0
threshold = 3500
income_amount = salary - insurance - threshold 
def tax_result(rate, deduct):
    tax = income_amount * rate - deduct
    # print(salary, income_amount, rate, deduct, tax)
    print("%.2f" % tax)

if income_amount <= 1500:
    rate = 3/100
    deduct = 0
    tax_result(rate, deduct)
elif income_amount > 1500 and income_amount <= 4500:
    rate = 10/100
    deduct = 105
    tax_result(rate, deduct)
elif income_amount > 4500 and income_amount <= 9000:
    rate = 20/100
    deduct = 555
    tax_result(rate, deduct)
elif income_amount > 9000 and income_amount <= 35000:
    rate = 25/100
    deduct = 1005
    tax_result(rate, deduct)
elif income_amount > 35000 and income_amount <= 55000:
    rate = 30/100
    decuct = 2755
    tax_result(rate, deduct)
elif income_amount > 55000 and income_amount <= 80000:
    rate = 35/100
    decuct = 5505
    tax_result(rate, deduct)
elif salary > 80000:
    rate = 45/100
    deduct = 13500
    tax_result(rate, deduct)

while True:
    try:
        open(salary)
        print(salary.read())
        close()
    except ValueError as Error:
    print("Error:{}".format("salary"))
