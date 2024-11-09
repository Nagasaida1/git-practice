list = [1,0,2,0,3,0]
for i in list:
	if i == 0:
		list.remove(i)
		list.append(i)
print(list)
