#      *
#      * *
#      * * *
n=int(input("enter a number:"))
for i in range(n):
    print('*'*(i+1))

#   1
#   2 2
#   3 3 3

n=int (input ("enter a number:"))
for i in range(1, n+1):
    print((str(i) + ' ') * i)

#A
#B B
#C C C
n=int (input ("enter a number:"))
for i in range(65, 65+n):
    print((chr(i) + ' ') * (i-64))

#1
#1 2
#1 2 3
n=int (input ("enter a number:"))
for i in range (1, n+1):
    for j in range (1,n+1):
        print (j, end=' ')
    print()

#A
#A B
#A B C
n=int (input ("enter a number:"))
for i in range(1, n+1):
    for j in range(65, 65+i):
        print(chr (j), end=' ')
    print()

#3 
#3 2 
#3 2 1 
n=int (input ("enter a number:"))
for i in range(1, n+1):
    for j in range(n, n-i, -1):
        print(j, end=' ')
    print()

# C
# C B
# C B A
n=int (input ("enter a number:"))
for i in range(1, n+1):
    for j in range(n, n-i, -1):
        print(chr(64+j), end=' ')
    print()
