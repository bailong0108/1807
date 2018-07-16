
x = float(input("请输入一个x值:"))
y = float(input("请输入一个y值:"))
z = input("请输入+-*/:")
'''
if z == "+":
	print(x+y)
elif z == "-":
	print(x-y)
elif z == "*":
	print(x*y)
elif z == "/":
	print(x/y)
'''
'''
x = float(input("请输入一个x值:"))
y = float(input("请输入一个y值:"))
a = (x+y)
print(a)
'''
if z == "+":
	print("x+y的值%.02f"%(x+y))
elif z == "-":
	print("x-y的值%.02f"%(x-y))
elif z == "*":
	print("x*y的值%.02f"%(x*y))
elif z == "/":
	if y == 0:
		print("不合法")
	else:
		print("x/y的值%.02f"%(x/y))
