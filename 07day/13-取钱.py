account = "abc"
passwd = "12345600"
money = 100000.00
act = input("请输入你的账户:")
pwd = input("请输入你的密码:")
if act == account and pwd == passwd:
	print("可以取钱")
	mey = float(input("请输入取钱金额:"))
	m = money-mey
	if mey > money:
		print("没钱取毛线")
	else:
		print("取了%.02f，还剩%.02f"%(mey,m))
else:
	print("非法账户")
