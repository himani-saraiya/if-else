a=int(input("enter no"))
b=int(input("enter no"))
c=int(input("enter no"))
if a==b and b==c and c==a:
	print("equilateral")
elif b==c and c==a and a==c:
	print("isoscales")
else:
	print("scalene")