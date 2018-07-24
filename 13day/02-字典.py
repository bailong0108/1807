d = {"name":"老王","sex":"男","minzu":"汉","brithday":"1999.5.8","address":"xxxx"}

#添加一对键值对
d["age"] = 18
print(d)
d["name"] = "老宋"
print(d)

#删除
d.pop("name")
print(d)
#查找
print(d["sex"])

#改：
d["name"] = "xxx"

#遍历
for i in d:
	print(i)
	print(d[i])


for i in d.keys():
	print(i)
	print(d[i])


for i in d.values():
	print(i)


for k,v in d.items():
	print(k)
	print(v)

for i in d.items():
	print(i)
	print(i[0])


