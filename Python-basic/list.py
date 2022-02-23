
"""
Add numbers to a list called "numbers" and words to a list called "string"
add name to variable "second_name".
"""

numbers = []
string = []
names = ["Din", "Sam", "Kaz", "Crouly"]

second_name = names[1]

for num in range(1, 4):
    numbers.append(num)
print(numbers)
for words in ("Hello", "world"):
    string.append(words)
print(string)
print(second_name)
