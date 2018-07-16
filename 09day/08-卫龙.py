i = 1
money = 0#没有买的时候钱数
while i <= 10:#逛了10家小卖店
	j = 1
	while j <= 2:#买俩袋卫龙
		money+=1
		j+=1
	i+=1
print("一共花了%.00f元"%money)
