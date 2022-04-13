unit=int(input("enter unit no"))
if unit<=100:
	amount=0
	print('no pay')
elif unit>=100 and unit<=200:
	amount=(unit-100)*5
	print('amount to pay', amount)
elif unit>=200:
	amount=100*5+(unit-200)*10
	print('amount to pay',amount)