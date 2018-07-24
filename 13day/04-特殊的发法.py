d = {"name":"laowwng","age":18}

#print(d["name"])
#print(d.get("name"))  #没有键不报错 返回None



d["name"] = "老宋"
d.setdefault("name","老宋") #如果键存在，不会改变  如果键不存在，则添加一对键值对
print(d)


d1 = {"sex":"男"}
d.updata(d1)
print(d)

d.popitem()  #随机删除
print(d)
