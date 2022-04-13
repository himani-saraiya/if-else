tax = 0
cost_price=int(input("Enter the price of bike"))
if cost_price > 100000:
    print(15/100*cost_price,tax)
elif cost_price >50000 and cost_price <=100000:
     print(10/100*cost_price,tax)
else:
     print(5/100*cost_price,tax)