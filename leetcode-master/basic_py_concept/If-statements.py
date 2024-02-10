# If statements don't need parentheses 
# or curly braces

# Parentheses needed for multi-line conditions.

"""
Python Question 2: Implementing Multi-line Conditions
Consider you have a Python function check_conditions(a, b) that returns True if either a is greater than 10 and b is less than 5, or a is less than 10 and b is greater than 5. Implement this function adhering to the rule that parentheses are needed for multi-line conditions.

Python Question 3: Logical Operators
Python uses and and or for logical operations. Given the preference for && and ||, how would you explain the adjustment needed to write conditions in Python that follow the logical operation conventions you're accustomed to?

Python Question 4: Simplifying Conditions
Python allows for simplification and chaining of comparison operators. How would you simplify the following condition, considering Python's capabilities and your conventions?"""

def check_condition(a, b):
    if (a > 10 and b < 5) or (a < 10 and b > 5):
        return True
    else:
        return False
    




