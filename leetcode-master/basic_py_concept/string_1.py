# Strings are similar to arrays
s = "abc"
print(s[0:1])

# So this creates a new string
s += 'def'
print(s)

# Valid numeric strings can be converted 
print(int("123") + int("456"))

# And numbers can be converted to strings
print(str(123) + str(456))

# In rare cases you may need the ASCII value of a char
print(ord("e"))
print(ord("a"))

# Combine a list of strings (with an empty string delimitor)
strings = ["ab", "cd", "ef"]
print("".join(strings))