list = [] #装学生
def showError(msg): #显示错误
	print("输入有误，请重新输入"+msg)

def isNum(num): #判断是否一个数字
	if num.isdigit():
		return True
	else:
		return False
def add(): #添加功能
	stu = {}
	while True:
		name = input("请输入学生姓名")
		if len(name)>=2 and len(name)<=4:
			stu["name"] = name
			break
		else:
			showError("学生姓名必须大于2小于4")
	while True:
		age = input("请输入学生年龄")
		if isNum(age):
			age = int(age)
		else:
			print("输入有误")
			continue
		if age >1 and age< 130:
			stu["age"] = age
			break
		else:
			showError("年龄必须大于1小于130")
	list.append(stu)
	print("添加成功")

def find(): #查找功能
	name = input("请输入要查找的名字")
	for stu in list:
		if stu["name"] == name:
			print("学生姓名:%s\n学生年龄:%d"%(stu["name"],stu["age"]))
			break

def change(): #修改功能
	name = input("请输入要修改的名字")
	for stu in list:
		if stu["name"] == name:
			print("1、修改名字")
			print("2、修改年龄")
			num = int(input("请选择功能"))
			if num == 1:
				name = input("请输入新的名字")
				stu["name"]=name
			elif num == 2:
				age = input("请输入新的年龄")
				stu["age"] = age
			break

def delete(): #删除功能
	name = input("请选择要删除的名字")
	for stu in list:
		if stu["name"] == name:
			list.remove(stu)
			print("删除成功")
			break

def print_list(): #打印全部
	print("姓名        年龄")
	for stu in list:
		print("%s        %d"%(stu["name"],stu["age"]))

def print_menu():
	print("欢迎来到学生管理系统".center(30," "))
	while True:
		print("1、添加学生信息")
		print("2、查找学生信息")
		print("3、修改学生信息")
		print("4、删除学生信息")
		print("5、打印学生信息")
		print("6、退出学生系统")
		input_info() #调用选择功能函数

def input_info():
	num = input("请选择功能")
	if isNum(num):
		num = int(num)
	else:
		print("输入有误")
	if num == 1:
		add() #调用添加函数
	elif num == 2:
		find()
	elif num == 3:
		change()
	elif num == 4:
		delete()
	elif num == 5:
		print_list()
	elif num ==6:
		print("谢谢使用")
		exit()
print_menu()
		


