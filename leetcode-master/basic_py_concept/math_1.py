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

# Modding is similar to most languages: remaining
print(5 % 2)
print(10 % 3)

# To be consistent with other languages module
import math
from multiprocessing import heap
print(math.fmod(-10, 3))

#More math helper: floor(): round down
print(math.floor(5 / 3))
# ceiling: round up
print(math.ceil(5 / 3))
# square root
print(math.sqrt(4))
# power 10^3 十的三次方
print(math.pow(10, 3))

# get Max /Min Integer:
float("inf")
float("-inf")

# because python numbers are infinite, it will never overfloat
print(math.pow(2, 200))
# But still less than infinity
print(math.pow(2, 200) < float("inf"))


