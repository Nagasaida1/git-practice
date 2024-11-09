try:
    x = int(input('Enter 1st Number:'))
    y = int(input('Enter 2nd Number:'))
    print(x/y)
except ZeroDivisionError:
        print("Can't devide with zero")
except ValueError:
    print('Please provide int value only')


try:
	x = int(input('Enter 1st Number:'))
	y = int(input('Enter 2nd Number:'))
	print(x/y)
except ArithmeticError:
	print('ArithmeticError')
except ZeroDivisionError:
	print("ZeroDivisionError")

