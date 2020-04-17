#LC_16
#Time - O(n)


def checkValidString(s):
    if len(s) == 0 or s == "*":
        return True
    if len(s) == 1:
        return False
    
    leftBalance = 0
    for char in s:
        if char == ')':
            leftBalance -= 1
        else:
            leftBalance += 1
        if leftBalance < 0:
            return False
    if leftBalance == 0:
        return True
    
    rightBalance  = 0
    for char in reversed(s):
        if char == '(':
            rightBalance -= 1
        else:
            rightBalance += 1
        if rightBalance < 0:
            return False
    return True



print(checkValidString("(*))"))