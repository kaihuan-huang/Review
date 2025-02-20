
#*
#**
#***
#****
#*****
def triangle():
    for i in range(1, 6): #12345 not include 6
        print('*' * i)
        
        
        
        
        
        

''' 20. Valid Parentheses
S=([1}) output=true
S= (} output=false
'''

def check_brackets(S):
    stack = []
    for char in S:
        if char == '(' or char == '[' or char == '{':
            stack.append(char)
        elif char == ')' or char == ']' or char == '}':
            if len(stack) == 0:
                return False
            if char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False
    return len(stack) == 0

print(check_brackets("([1})"))  # Output: True
print(check_brackets("(}"))     # Output: False

                
# 48. Rotate Image
'''Input: matrix = [[1,1,1],[2,2,2],[3,3,3]]
           Output: [[1,2,3],[1,2,3],[1,2,3]]'''




def rotate_image(matrix):
     n = len(matrix)
     # Transpose the matrix
     for i in range(n):
         for j in range(i, n):
             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
     # Reverse each row
     for i in range(n):
         matrix[i] = matrix[i][::-1]
     return matrix
matrix = [[1,1,1],[2,2,2],[3,3,3]]
print(rotate_image(matrix))





