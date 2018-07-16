account = "123456"
passwd = "abc"
act = input("请输入你的账号:")
pwd = input("请输入你的密码:")
if act == account and pwd == passwd:
	print("登录成功")
elif act != account:
	print("账号不正确")
elif pwd != passwd:
	print("密码不正确")
else:
	print("重新输入")
