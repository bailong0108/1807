'''
i = 1
money = 0
while i < 11:
	j = 1 
	while j < 3:
		money +=1
		j+=1
	i += 1
print(money)
'''
money = 0
for i in range(1,11):
	for j in range(1,3):
		money+=1
print(money)
