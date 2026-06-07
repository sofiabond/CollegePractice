def create_rating(students: list) -> list: 
	n = len(students) 
	for i in range(n): 
		max_index = i 
		for j in range(i + 1, n): 
			if students[j][1] > students[max_index][1]: 
				max_index = j 
		students[i], students[max_index] = students[max_index], students[i] 
	return students 
students = [ 
	["Микита", 8],
	["Олег", 6],
	["Іван", 9],
	["Марія", 12],
	["Поліна", 10] 
]
rating = create_rating(students)
print("Рейтинг студентів:")
for student in rating:
	print(student[0], "-", student[1])