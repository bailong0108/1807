def test(): #无参无返回值
	c=1+2
	print(c)
test()

def test1(a,b)  #形参 有参无返回值
	c=a+b
	print(c)
test1(1,2)

def test2(): #无参有返回值
	c=a+b
	return c
ret =test2()
print(ret)


def test3(a,b): #有参有返回值
	c=a+b
	return c
ret =test3(1,2)
print(ret)
