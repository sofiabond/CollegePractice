def validate_brackets(code: str) -> bool:
	stack = []
	brackets = {
		")": "(",
		"]": "[",
		"}": "{"
	}
	for symbol in code:
		if symbol == "(" or symbol == "[" or symbol == "{":
			stack.append(symbol)
		elif symbol == ")" or symbol == "]" or symbol == "}":
			if len(stack) == 0:
				return False
			last_bracket = stack.pop()
			if last_bracket != brackets [symbol]:
				return False
	if len(stack) != 0:
		return False
	return True
code = input("Введіть код: ")
result = validate_brackets(code)
print("Результат перевірки:")
print(result)