"""
Implementation Queue in class.
"""
from linkedlist.linked_list import LinkedList


class Queue(LinkedList):
    """
    Create class Queue with empty list.
    """

    def enqueue(self, data):
        """
        Method enqueue which add data at element list.
         """
        self.prepend(data)

    def dequeue(self):
        """
        Create method dequeue which remove an item from the beginning of the queue.
        """
        self.delete(0)

    def peek(self):
        """
        Create method peek which gives the value of the element at the start of the queue.
        """
        if self.head is None:
            return None
        return self.head.data
