'''
import random
i = 0
num = random.randint(1,100)#先随机一个数字
while i < 9:
	u_num = int(input("请输入猜的数字:"))
	if u_num > num:
		print("猜大了")
	elif u_num < num:
		print("猜小了")
	else:
		print("对了")
		break
	i += 1
'''
import random
pc = random.randint(1,20)
for i in range(1,11):
	player = int(input("请输入数字"))
	if player > pc:
		print("猜大了")
	elif player < pc:
		print("猜小了")
	elif player == pc:
		print("猜对了")
		break

