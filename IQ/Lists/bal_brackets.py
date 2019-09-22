"""
Check the given expression contains properly balanced brackets or not.
"""


def isValidPair(left, right):
    if left == '(' and right == ')':
        return True
    if left == '[' and right == ']':
        return True
    if left == '{' and right == '}':
        return True  
    return False
  
def isProperlyNested(S):
    stack = []
      
    for symbol in S:
        if symbol in ['[', '{', '(']:
            stack.append(symbol)
        elif symbol in [']', '}', ')']:
            if len(stack) == 0:
                return False
            last = stack.pop()
            if not isValidPair(last, symbol):
                return False
      
    if len(stack) != 0:
        return False
              
    return True

def main():
    N = int(input("Enter number of inputs: "))
 
    for _ in range(N):
        s = input("Enter the expression: ")
        if isProperlyNested(s):
            print("Valid Expression")
        else:
            print("Invalid Expression")


if __name__ == '__main__':
    main()
