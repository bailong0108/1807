num = int(input("请输入一个数 开头:"))
x = int(input("请输入一个数 结尾:"))
i = 0
while num < x+1:
	i+=num
	num+=1
print("总和是:",i)
