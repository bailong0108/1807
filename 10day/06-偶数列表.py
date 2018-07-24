'''
list=[]
for i in range(1,101):
	if i%2 == 0:	
		list.append(i)
print(list)
list.pop(0)
list.remove(20)
print(list)
'''

list=[]
i = 1
while i <= 100:
	if i%2 == 0:
		list.append(i)
	i+=1
		
print(list)
