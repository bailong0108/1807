def shu():
	i =1
	while i<=100:
		if i%2 == 0:
			print("偶数%d"%i)
		else:
			print("奇数%d"%i)
		i+=1
shu()


def show_num():
	for i in range(1,101):
		if i %2 ==0:
			print("我是偶数%d"%i)
		else:
			print("奇数%d"%i)
show_num()
