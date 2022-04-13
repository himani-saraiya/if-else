print("Welcome To The SBI Bank")
print("swipe your card")
print("hindi/english")
lang=input("enter")
if lang=="hindi" or lang=="english":
		pin=input("enter a pin")
		if pin=='8285':
			print("correct pin ")
			print("choose your choice:-","•withdraw","•balance","•deposit","•exit")
			chs=input("enter a choose")
			if chs=="withdraw":
				withdraw=int(input("enter a  withdraw amount"))
				amount=20000
				if withdraw<=amount:
					print("total amount:-",amount-withdraw)
					print("callect your cash withdraw")
				print("thank you for using")
			elif chs=='deposit':
			 	print('1.saving account 2.current account')
			 	ac_type=input('enter type')
			 	if ac_type=='saving account':
			 		print('enter your account num')
			 		account_num=input('enter ac num')
			 		if account_num=='222222222222':
			 			print('enter your amount:')
			 			amount=int(input('enter money'))
			 			if amount>=500:
			 				print('deposit succesgully')