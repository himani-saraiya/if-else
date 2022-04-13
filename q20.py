elctry=int(input("enter no"))
if elctry<=50:
	amount=elctry*0.50
	surcharge=amount*20/100
	print(amount+surcharge)
if elctry<=100:
	amount=elctry*0.75
	surcharge=amount*20/100
	print(amount+surcharge)
elif elctry<=100:
	amount=elctry*1.20
	surcharge=amount*20/100
	print(amount+surcharge)