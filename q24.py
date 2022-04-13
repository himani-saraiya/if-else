a=int(input("enter no"))
b=int(input("enter no"))
c=int(input("enter no"))
if a>b and a>c:
	print("a is oldest")
elif b>a and b>c:
	print("b is youngest")
elif c>a and c>b:
	print("smallest")