import time
def climb_recursive(n: int) -> int:
	if n == 0 or n == 1:
		return 1
	return climb_recursive(n - 1) + climb_recursive(n - 2)

def climb_iterative(n: int) -> int:
	if n == 0 or n == 1:
		return 1
	first = 1
	second = 1
	for i in range(2, n + 1):
		current = first + second
		first = second
		second = current
	return second

test_values = [10, 20, 30, 35]
for n in test_values:
	start = time.time()
	recursive_result = climb_recursive(n)
	end = time.time()
	recursive_time = end - start

	start = time.time()
	iterative_result = climb_iterative(n)
	end = time.time()
	iterative_time = end - start

	print(f"\nСходинок: {n}")
	print (f"Рекурсивний результат: {recursive_result}")
	print (f"Рекурсивний час: {recursive_time :.6f} сек")

	print (f"Ітеративний результат: {iterative_result}")
	print (f" Ітеративний час: {iterative_time :.6f} сек")