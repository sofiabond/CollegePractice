def merge_orders(web_orders: list, app_orders: list) -> list:
	merged = []
	i = 0
	j = 0
	while i < len(web_orders) and j < len(app_orders):
		if web_orders[i][1] <= app_orders[j][1]: 
			merged.append(web_orders[i])
			i += 1
		else:
			merged.append(app_orders[j])
			j += 1
	while i < len(web_orders):
		merged.append(web_orders[i])
		i += 1
	while i < len(app_orders):
		merged.append(app_orders[j])
		j += 1 
	return merged

web_orders = [
	["WOrder1", 2],
	["WOrder2", 4],
	["WOrder3", 6],
	["WOrder4", 9]
]
app_orders = [
	["Aorder1", 1],
	["AOrder2", 7],
	["AOrder3", 8]
]
result = merge_orders(web_orders, app_orders)
print("Об'єднаний список замовлень: ")
for order in result: 
	print(order)