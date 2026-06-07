class PhoneBook:
    def __init__(self):    
        self.size = 8
        self.count = 0
        self.table = []
        for i in range(self.size):
            self.table.append([])

    def hash_function(self, key):
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value % self.size

    def add(self, name, phone):
        load_factor = self.count / self.size
        if load_factor > 0.75:
            self.resize()
        index = self.hash_function(name)
        chain = self.table[index]
        for pair in chain:
            if pair[0] == name:
                pair[1] = phone
                return
        chain.append([name, phone])
        self.count += 1

    def get(self, name):
        index = self.hash_function(name)
        chain = self.table[index]
        for pair in chain:
            if pair[0] == name:
                return pair[1]
        return "Контакт не знайдено"

    def remove(self, name):
        index = self.hash_function(name)
        chain = self.table[index]
        for i in range(len(chain)):
            if chain[i][0] == name:
                chain.pop(i)
                self.count -= 1
                return True
        return False

    def contains(self, name):
        index = self.hash_function(name)
        chain = self.table[index]
        for pair in chain:
            if pair[0] == name:
                return True
        return False

    def length(self):
        return self.count

    def resize(self):
        old_table = self.table
        self.size = self.size * 2
        self.table = []
        for i in range(self.size):
            self.table.append([])
        self.count = 0
        for chain in old_table:
            for pair in chain:
                self.add(pair[0], pair[1])


phonebook = PhoneBook()

while True:

    print("\n1 - Додати контакт")
    print("2 - Знайти контакт")
    print("3 - Видалити контакт")
    print("4 - Кількість контактів")
    print("5 - Вихід")

    choice = input("Ваш вибір: ")

    if choice == "1":

        name = input("Ім'я: ")
        phone = input("Телефон: ")

        phonebook.add(name, phone)

    elif choice == "2":

        name = input("Ім'я: ")

        print(phonebook.get(name))

    elif choice == "3":

        name = input("Ім'я: ")

        if phonebook.remove(name):
            print("Контакт видалено")
        else:
            print("Контакт не знайдено")

    elif choice == "4":

        print("Кількість контактів:", phonebook.length())

    elif choice == "5":

        break