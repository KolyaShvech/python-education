"""
In this module implement methods of linked list.
"""
from data_structure.data_structure.basic_node import BasicNode


class LinkedList:
    """
    Create class LinkedList.
    """

    count = 0

    def __init__(self, data):
        base = BasicNode
        node = base(data)
        self.head = node
        self.tail = node
        self.count += 1

        self._previous = None

    def prepend(self, data):
        """
        Create method prepend. Add element start at list.
        A -> B -> C -> D -> None
        E -> A -> B -> C -> D
        """
        node = BasicNode(data, self.head)
        self.head = node
        self.count += 1

    def append(self, data):
        """
        Create method append. Added element in back list.
        A -> B -> C -> D -> None
        A -> B -> C -> D -> E -> None
        """
        node = BasicNode(data)
        self.tail.link = node
        self.tail = node
        self.count += 1

    def look_up(self, data):
        """
         Method look_up index by first in position selected element
         """
        node = self.head
        index = 0
        while index != self.count:
            if node.data == data:
                return index
            index += 1
            node = node.link

    def insert(self, data, index):
        """
         Method insert_element with parameters index and value.
         In this method add element to a specific index.
         """
        element_node = BasicNode(data)
        if index < 0 or self.count < index:
            raise IndexError
        if index == 0:
            self.prepend(data)
        elif index == self.count:
            self.append(data)
        else:
            node = self.head
            counter = 0
            while counter != self.count:
                if counter == index - 1:
                    current_node_link = node.link
                    node.link = element_node
                    element_node.link = current_node_link
                    break
                counter += 1
                node = node.link

    def _delete_first_arg(self):
        """Method _delete_arg first element to delete.
        A -> B -> C -> D -> None
            B -> C -> D -> None"""
        if self.count != 0:
            self.head = self.head.link
            self.count -= 1

    def _delete_arg_by_index(self, index):
        """
        This method delete_element. Delete element by index.
        """
        node = self.head
        counter = 0
        while counter != self.count:
            if counter == index:
                if node.link is None:
                    self._previous.link = None
                    self.count -= 1
                    break
                self._previous.link = node.link
                self.count -= 1
                break
            counter += 1
            self._previous = node
            node = node.link

    def delete(self, index):
        """Delete element by index"""
        if index > self.count or index < 0:
            raise IndexError
        if index == 0:
            self._delete_first_arg()
        else:
            self._delete_arg_by_index(index)

    def __iter__(self):
        return LinkedListIterator(self.head)


class LinkedListIterator:
    """
    Create class LinkedListIterator.
    """
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            item = self.current.data
            self.current = self.current.link
            return item

