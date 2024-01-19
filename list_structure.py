class ListItem:
    # """
    # Represents an item in a linked list.

    # Attributes:
    #     value: The value stored in the item.
    #     next_element: A reference to the next item in the linked list.
    # """

    def __init__(self, value):
        self.value: int = value
        self.next_element: ListItem = None


class ListStructure:
    # """
    # Represents a linked list data structure.

    # Attributes:
    #     first: The first element in the linked list.
    #     last: The last element in the linked list.
    #     __count: The number of elements in the linked list.
    # """
    def __init__(self):
        self.first: ListItem = None
        self.last: ListItem = None
        self.__count: int = 0

    def insert(self, value: int):
        # """
        # Inserts a new element with the given value at the end of the linked list.

        # Parameters:
        #     value (int): The value to be inserted.

        # Returns:
        #     None
        # """
        new_element: ListItem = ListItem(value)
        if self.last:
            self.last.next_element = new_element
            self.last = new_element
        else:
            self.first = new_element
            self.last = new_element
        self.__count += 1

    def remove(self, removing_value: int) -> bool:
        # """
        # Remove the first occurrence of the given value from the linked list.

        # Parameters:
        #     removing_value (int): The value to be removed.

        # Returns:
        #     bool: True if the value was found and removed, False otherwise.
        # """
        if not self.first:
            return False

        current: ListItem = self.first
        is_found: bool = False
        if self.first.value == removing_value:
            self.first = self.first.next_element
            is_found = True
        else:
            while current.next_element:
                if current.next_element.value == removing_value:
                    current.next_element = current.next_element.next_element
                    is_found = True
                    break
        if is_found:
            self.__count -= 1
        return is_found

    def find(self, value: int):
        # """
        #   """
        #   Find the first ListItem in the LinkedList that contains the given value.

        #   Parameters:
        #     - value: The value to search for in the LinkedList.

        #   Returns:
        #     - The first ListItem that contains the given value, or False if the value is not found.
        #   """
        current: ListItem = self.first
        while current:
            if current.value == value:
                return current
            current = current.next_element
        return False

    def size(self):
        return self.__count

    def __getitem__(self, key: int) -> int:
        # """
        # Get the value at the specified index in the list.

        # Parameters:
        #     key (int): The index of the value to retrieve.

        # Returns:
        #     int: The value at the specified index.

        # Raises:
        #     IndexError: If the index is out of range.
        # """
        index: int = 0
        current: ListItem = self.first
        while index != key:
            current = current.next_element
            index += 1
        return current.value
