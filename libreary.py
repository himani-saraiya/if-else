expected_date=int(input("enter a date"))
expected_month=int(input("enter a month"))
expected_year=int(input("entet a year"))
return_date=int(input("enter return date"))
return_month=int(input("enter return month"))
return_year=int(input("enter return year"))
if return_date==expected_date:
	if return_month==expected_month:
		if return_year==expected_year:
			print("no fine")
elif return_date>=expected_date:
    print(15*(return_date-expected_date))
    if return_month>=expected_month:
        print(500*(return_month-expected_month))
        if return_year>=expected_year:
            print(10000*(return_date-expected_date))
else:
	print("nothing")
