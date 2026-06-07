class Deque:
    def __init__(self):
        self.items = []
    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def remove_rear(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def is_palindrome(phrase: str) -> bool:
    deque = Deque()

    cleaned = ""
    for char in phrase:
        if char.isalnum():
            cleaned += char.lower()

    for char in cleaned:
        deque.add_rear(char)
    while deque.size() > 1:
        front = deque.remove_front()
        rear = deque.remove_rear()
        if front != rear:
            return False
    return True


phrase = input("Введіть фразу: ")
result = is_palindrome(phrase)
print("Результат:")
print(result)