list = [] #装学生

def add(): #添加功能
	stu = {}
	name = input("请输入学生姓名")
	age = int(input("请输入学生年龄"))
	stu["name"] = name
	stu["age"] = age
	list.append(stu)
	print("添加成功")

def find(): #查找功能
	name = input("请输入查找的名字")
	for stu in list:
		if stu["name"] == name:
			print("学生姓名:%s\n学生年龄:%d"%(stu["name"],stu["age"]))
			break

def change(): #修改功能
	name= input("请输入要修改的名字")
	for stu in list:
		if stu["name"] == name:
			print("1、修改名字")
			print("2、修改年龄")
			num = int(input("请选择功能"))
			if num == 1:
				name = input("请输入新的名字")
			elif num ==2:
				age = int(input("请输入新的年龄"))
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
		print("6、退出学生信息")
		input_info() #调用选择功能函数

def input_info():
	num = int(input("请选择功能"))
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
	elif num == 6:
		print("再见")	
		exit()
print_menu()















