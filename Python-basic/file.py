
"""
Train with files: open file
"""
try:  # catch an error if the user entered the wrong file
    with open("text.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("This file not find!")

print(file.closed)

# """
# train with file: write file
# """
#
# films = "8. Морбиус\n 9. Черный Адам"
#
# with open("text.txt", "a") as file:  # If we write argument "a", we append string, if "w", write new text in file
#     file.write(films)


"""
train with files: copy
"""
#
# import shutil
# # use operation in "shutil" "copyfile" and designate a new directory
# shutil.copyfile("text.txt", "//home//nikolay//Projects//my_projects//NIX-python//python-education//.copy_text.txt")

"""
file move at the other place
"""

# import os
# # Use import "os"
# sourse = "text.txt"
# direction = "//home//nikolay//text.txt"
#
# try:  # we catch an error in case of incorrect file input
#     if os.path.exists(direction):  # determine if it is a file
#         print("There are file is there")
#     else:  # move the file to the specified directory
#         os.replace(sourse, direction)
#         print(sourse + " Was moved.")
# except FileNotFoundError:
#     print(sourse + " not find")

