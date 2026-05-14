# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

# Task 1: Using a List to implement a simple Todo application
from collections import deque


class TodoList:
    def __init__(self):
        self.todos = []

    def add(self, task: str) -> None:
        self.todos.append(task)

    def remove(self, index: int) -> None:
        self.todos.pop(index)

    def get_all(self) -> list:
        return self.todos

# Task 2: Using a Set to implement a "deduplication" feature
def remove_duplicates(items: list) -> list:
    return list(set(items))


# Task 3: Using a Deque to implement a simple LRU cache
class SimpleLRU:
    def __init__(self, capacity: int):
        self.capacity = capacity    # Maximum number of items the cache can hold
        self.cache = deque()        # Deque to store the items in the cache, with the most recently used item at the end

    def access(self, item) -> None:
        if item in self.cache:      # If the item is already in the cache, remove it to update its position
            self.cache.remove(item) # Remove the item from its current position in the cache
        self.cache.append(item)     # Add the item to the end of the cache (most recently used position)

        if len(self.cache) > self.capacity: # If the cache exceeds its capacity, remove the least recently used item (the one at the front of the deque)
            self.cache.popleft()

# Task 1: Create a TodoList instance and add some tasks
my_todo = TodoList()
TODOLISTS = ["Exercise", "Studying", "IoT Work"]
for task in TODOLISTS:
    my_todo.add(task)

print(my_todo.get_all())
print("Removing the second task...")
my_todo.remove(1)
print(my_todo.get_all())


# Task 2: Test the remove_duplicates function
print("Testing duplicate removal...")
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))

# Task 3: Create a SimpleLRU instance and access some items
print("Testing LRU Cache...")
lru_cache = SimpleLRU(capacity=3)
items_to_access = ['A', 'B', 'C', 'D', 'A', 'E']
for item in items_to_access:
    lru_cache.access(item)
    print(f"Current LRU Cache: {list(lru_cache.cache)}")