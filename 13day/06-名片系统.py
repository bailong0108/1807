students = [] #装学生
while True:
	print("欢迎来到学生管理系统")
	print("1:添加学生信息")
	print("2:查找学生信息")
	print("3:修改学生信息")
	print("4:删除学生信息")
	print("5:删除学生信息")
	print("6:退出学生系统")
	num = int(input("请选择功能"))
	if num == 1:
		i = {} #来一个学生创建一个字典  相等于学籍
		name = input("请输入名字:")
		age = int(input("请输入年龄:"))
		phone = int(input("请输入电话:"))
		i["name"] = name
		i["age"] = age
		i["phone"] = phone
		students.append(i) #把学籍存起来
		print(students)
	elif num == 2:
		name = input("请输入学生名字:")
		for i in students:
			if i ["name"] == name:
				print("学生名字是:%s\n学生年龄是:%d\n学生手机号:%d"%(i["name"],i["age"],i["phone"]))
				break 
		print("查找学生")
	elif num == 3:
		name = input("请输入学生名字:")
		for i in students:
			if i ["name"] == name:
				print("学生名字:%s\n学生年龄:%d\n学生手机号:%d"%(i["name"],i["age"],i["phone"]))
				print("1:修改名字")
				print("2:修改年龄")
				print("3:修改手机号")
				num = int(input("请选择修改序号"))
				if num == 1:
					name = input("请输入新的名字")
					i["name"] = name
				elif num == 2:
					age = int(input("请输入新的年龄"))
					i["age"] = age
				elif nume == 3:
					phone = int(input("请输入新的手机号"))
					i["phone"] = phone
				print("修改成功")
				break
	elif num == 4:
		name = input("请输入学生姓名:")
		for i in students:
			if i["name"] == name:
				students.remove(i)
				print("删除成功")
				break
	elif num == 5:
		print("打印全部信息")
		print("")



	elif num == 6:
		print("谢谢使用")
		break



