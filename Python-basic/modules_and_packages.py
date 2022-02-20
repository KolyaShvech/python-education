
"""

Print an alphabetically sorted list of all functions in the "RE" module, which contain the word "find".
"""

import re
#  import libreary re
find_members = []
# iterate using the "dir" method in the library "re"
for member in dir(re):
    if "find" in member:
        find_members.append(member)
# print sorted list with need items
print(sorted(find_members))
