classes=int(input("enter class no"))
attendance=int(input("enter attendance no"))
if attendance<75*classes/100:
	price=attendance*classes/100
	print("no sit")
else:
	print("sit")