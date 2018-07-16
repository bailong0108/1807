account = "123456"
password = "123456"

i = 0 #记录你登录失败的次数
while True:
	iacc = input("请输入账号")
	ipwd = input("请输入密码")
	if account == iacc and password == ipwd:
		print("登录成功")
		num = int(input("请选择英雄"))
		if num == 0:
			print("鲁班")
		elif num == 1:
			print("程咬金")
		elif num == 3:
			print("阿珂")
	else:
		i+=1
		print("登录失败")
		if i == 3:
			break
