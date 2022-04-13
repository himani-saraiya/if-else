pw=(input("enter a password"))
if (pw>="a" and pw>="z") or (pw>="A" and pw>="Z") or (pw=="@" ,pw=="$",pw=="#") or (pw>="0" and pw<="9"):
	if len(pw)>=8 and len(pw)<=15:
		print("strong password")
else:
	print("wrong password")


