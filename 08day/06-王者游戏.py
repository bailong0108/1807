account = "bql"
passwd = "123456"
act = input("请输入你的账号:")
pwd = input("请输入你的密码:")
if act == account and pwd == passwd:
	print("登录成功")
	z = input("请选择英雄 0代表ADC、1代表肉、3代表法师:")
	if z == "0":
		print("鲁班大师")
	elif z == "1":
		print("程咬金")
	elif z == "3":
		print("王昭君")    
else:
	print("请重新输入")
	

