"""
Implementation Data Structure - STACK in class.
"""
from linkedlist.linked_list import LinkedList


class Stack(LinkedList):
    """
    Create class Stack.
    """

    def push(self, item):
        """
        Method push. Add item in stack.
        30-->20-->10
        """
        self.prepend(item)

    def pop(self):
        """
        Method pop. Delete last  item which add.
        (30)pop 20-->10
        """
        item = self.tail.data
        self.delete(self.count - 1)
        return item

    def peek(self):
        """
        Method peek. Indicates the number at the top of the stack.
        """
        return self.tail.data
