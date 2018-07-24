list = [1,2,3,4,5,6,6]
list1 = []
for i in list:
	if i not in list1:
		list1.append(i)
print(list1)
