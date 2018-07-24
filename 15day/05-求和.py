'''
def qiuhe():
	num = int(input("请输入一个数 开头:"))
	x = int(input("请输入一个数 结尾:"))
	i = 0
	while num < x+1:
		 i+=num
		 num+=1
	print("总和是:",i)
qiuhe()
'''
def showsum(start,end): #声明函数 end是一个形参
	sum = 0
	for i in range(start,end+1):
		sum+=i
	print(sum)
start = int(input("请输入起始值"))
end=int(input("请输入终止值:"))
showsum(start,end) #实参
