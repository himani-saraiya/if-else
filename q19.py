basic_salary=int(input("enter no"))
if basic_salary<=1000:
	print("HRA=20%,DA=80%")
elif basic_salary<=2000:
	print("HRA=25%,DA=90%")
elif basic_salary>2000:
	print("HRA=30%,DA=95%")