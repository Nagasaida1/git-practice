try:
	x = int(input('Enter 1st Number:'))
	y = int(input('Enter 2nd Number:'))
	print(x/y)
except (ZeroDivisionError,ValueError) as msg:
	print("Pls provide valid numbers only the problem is:",msg)
	


#other
try:
	x = int(input('Enter 1st Number:'))
	y = int(input('Enter 2nd Number:'))
	print(x/y)
except ZeroDivisionError:
	print("ZeroDivisionError:Can't devide with zero")
except :
	print('DefaultExcept:Please provide valid input')

