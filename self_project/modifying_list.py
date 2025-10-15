class ArrayList:
    # In your ArrayList class

    def __init__(self, capacity=0):
        # This part is fine
        self.capacity = int(capacity)
        self.length = 0
        self.items = [None] * self.capacity

    def add(self, item):
        # This is the corrected version you need
        if self.length == self.capacity:
            # If capacity is 0, grow to 4. Otherwise, double it.
            new_capacity = 4 \
            if self.capacity == 0 \
            else self.capacity * 2
            self._reserve(new_capacity)



        self.items[self.length] = item
        self.length += 1

    # In your ArrayList class in modifying_list.py

    # Make sure the name is exactly "__str__"
    def __str__(self):
        if self.is_empty():
            return "[]"

        # Slice the list to get only the items from 0 up to self.length
        items_to_show = self.items[0:self.length]

        # Join the items into a clean string like a real Python list
        return "[" + ", ".join(map(str, items_to_show)) + "]"

    def __len__(self):
        return self.length

    def is_empty(self):
        return self.length == 0

    def _reserve(self, new_capacity):
        tmp = [None] * new_capacity
        for i in range(self.length):
            tmp[i] = self.items[i]
        # This was the main bug
        self.capacity = new_capacity
        self.items = tmp

    def remove(self, item):
        """Removes the first occurrence of the specified item from the list."""
        try:
            # Find the index of the item
            index_to_remove = self.index_of(item)
            # Use the existing remove_at method to delete it
            self.remove_at(index_to_remove)
        except ValueError:
            # Re-raise the ValueError to match Python's list behavior
            raise ValueError(str(item) + " is not in the list.")

    def index_of(self, item):
        for i in range(self.length):
            if self.items[i] == item:
                return i
        raise ValueError(str(item) + " is not in the list.")

    def element_at(self, index):
        # Corrected index check
        if index < 0 or index >= self.length:
            raise IndexError("Index is out of range.")
        return self.items[index]

    def find(self, item):
        try:
            return self.index_of(item)
        except ValueError:
            return -1

    def insert(self, index, item):
        if index < 0 or index > self.length:
            raise IndexError("Index is out of range.")
        if self.length == self.capacity:
            self._reserve(self.capacity * 2)
        for i in range(self.length, index, -1):
            self.items[i] = self.items[i - 1]
        self.items[index] = item
        self.length += 1

    def first(self):
        if self.length == 0:
            raise IndexError("The list is empty.")
        return self.element_at(0)

    def last(self):
        if self.length == 0:
            raise IndexError("The list is empty.")
        return self.element_at(self.length - 1)

    def remove_at(self, index):
        # Corrected index check
        if index < 0 or index >= self.length:
            raise IndexError("Index is out of range.")

        # Shift elements to the left
        for i in range(index, self.length - 1):
            self.items[i] = self.items[i + 1]

        # Decrement length and clear the now-unused last slot
        self.length -= 1
        self.items[self.length] = None

    def clear(self):
        # A more memory-efficient clear that doesn't re-allocate
        for i in range(self.length):
            self.items[i] = None
        self.length = 0