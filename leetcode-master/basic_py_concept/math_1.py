# Division is decimal by default
print(7 / 4)
# Double slash rounds down
print(7 // 4)
# CAREFUL: most languages round towards 0 by default
# So negative numbers will round down
print(-5 // 2)

# A workaround for rounding towards zero
# is to use decimal division and then convert to int.
print(int(-5 / 2))

# Modding is similar to most languages, 
print(5 % 2)

