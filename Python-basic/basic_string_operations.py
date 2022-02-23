
"""
Fix the code to print out the correct information by changing string.
"""

s = "Hey there! what should this string be?"

print(f"Length of s = {len(s)}")

print(f"The first occurrence of the letter a = {s.index('a')}")

print(f"a occurs times: {s.count('a')}")

print("The first five characters are:", s[:5])
print("The next five characters are:", s[5:10])
print("The thirteenth character is:", s[12])
print("The characters with odd index are:", s[1::2])
print("The last five characters are:", s[-5:])

# Convert everything to uppercase
print(s.upper())

# Convert everything to lowercase
print(s.lower())

# Check how a string starts
print(s.startswith("Str"))

# Check how a string ends
print(s.endswith("ome!"))

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))
