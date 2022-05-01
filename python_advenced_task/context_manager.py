""""
Implementing a program Context Manager in class.
"""


class ContextManager:
    """"
    Create class ContextManager.
    """
    def __init__(self, file_path):
        self.file_path = file_path

    def __enter__(self):  # Open file and write something in this file.
        self.file_obj = open(self.file_path, mode="w+")
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):  # Comes out of the file and close.
        if self.file_obj:
            self.file_obj.close()


with ContextManager("text_manager.txt") as file:
    file.write("Write program context manager!")
    file.write("\nSecond sentence")
    file.write("\nThird sentence in this file!")


