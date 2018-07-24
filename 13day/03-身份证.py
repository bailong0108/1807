ID = {"name":"白庆龙","sex":"男","mz":"汉","brithday":"2000年1月8日","address":"陕西榆林"}

ID["age"] = 18
print(ID)

ID["name"] = "小白"
print(ID)

ID.pop("name")
print(ID)

print(ID["sex"])

for i in ID:
	print(i)
	print(ID[i])
