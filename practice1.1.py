def find_product(products: list, target: str) -> int:
	for i in range(len(products)):
		if products[i] == target:
			return i + 1
	return "Товар не знайдено"
products = [
	"Ноутбук",
	"Мишка",
	"Клавіатура",
	"Монітор",
	"Навушники"
]
target = input("Введіть назву товару: ")
result = find_product(products, target)
print("Результат пошуку:", result)