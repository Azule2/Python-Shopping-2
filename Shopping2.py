import sys



User = input('Enter Your Username: ')
Pass = input('Enter Your Password: ')
ConfirmPass = input('Confirm Password:')

#Here is the Bank_Account code
class Bank_Account:
	def __init__(self):
		self.balance=0
		print("IMine Bank ")

	def deposit(self):
		amount=float(input("Enter amount to be Deposited: "))
		self.balance += amount
		print("\n Amount Deposited:",amount)

	def withdraw(self):
		amount = float(input("Enter amount to be Withdrawn: "))
		if self.balance>=amount:
			self.balance-=amount
			print("\n You Withdrew:", amount)
		else:
			print("\n Insufficient balance ")

	def display(self):
		print("\n Net Available Balance=",self.balance)


s = Bank_Account()
s.deposit()
s.withdraw()
s.display()




#Confirm Password
if Pass == ConfirmPass:
    print('Successful')
else :
    print('Not Found Password')
    sys.exit()

#Welcome Print
print('Welcome ',User, 'to the Market')

#Here is the code shopping.
shop_List = [
	['Steak','Pig','Cow'],
	['Water','orange juice','Pomegranate juice'],
]

print('These are available: meat,drinking')

shop = Usera = input('Enter the request: ')

if Usera == 'meat':
 	print(shop_List[0])

elif Usera == 'drinking':
 	print(shop_List[1])
#Order
shop = Usera = input('Enter the request: ')
if Usera == 'Steak':
 	print('Here you are Request:',shop_List[0][0])

elif Usera == 'Pig':
 	print('Here you are Request:',shop_List[0][1])

elif Usera == 'Cow':
 	print('Here you are Request:',shop_List[0][2])

elif Usera == 'Water':
 	print('Here you are Request:',shop_List[1][0])

elif Usera == 'orange juice':
 	print('Here you are Request:',shop_List[1][1])

elif Usera == 'Pomegranate juice':
 	print('Here you are Request:',shop_List[1][2])
else:
	print('Not availbile: ',Usera)
	
#IMine Code (Azule).
