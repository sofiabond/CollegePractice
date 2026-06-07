def search_dictionary(dictionary: list, word: str) -> str:
	for i in range(len(dictionary)):
		current_word = dictionary[i][0]
		if current_word == word:
			return dictionary[i][1]
	return "Слово не знайдено"

dictionary = [
	["Алгоритм", "Послідовність дій"],
	["База данних", "Організована структура для зберігання інформації"],
	["Інтерфейс", "Засіб взаємодії користувача з програмою"],
	["Компілятор", "Програма для перекладу коду у машинну мову"],
	["Масив", "Структура данних для зберігання елементів"]
]

word = input("Введіть слово: ")
result = search_dictionary(dictionary, word)
print("Результат пошуку:")
print(result)
