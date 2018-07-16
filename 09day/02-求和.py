i = 1
sum = 0 # 和
while i < 100:
	if i % 2 == 1:#奇数
		sum +=i#sum = sum+i
	else:#偶数
		sum -=i#sum = sum-i
	i +=1
print(sum)
