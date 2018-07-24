def jisuanji(x,y,z): #形参
	if z == "+":
		c = x+y
		print(c)
	elif z == "-":
		c = x-y
		print(c)
	elif z == "*":
		c = x*y
		print(c)
	elif z == "/":
		if y!= 0:
			c = x/y
			print(c)
		else:
			print("不合法")
x = int(input("请输入x值:"))
y = int(input("请输入y值:"))
z = input("请输入+-*/")
jisuanji(x,y,z) #实参
