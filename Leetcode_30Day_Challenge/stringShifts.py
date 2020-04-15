#LC_14

#Approach -1
#Using the built-in python methods
#Time and Space - O(n)


def stringShift(s, shift):
    l = list(s)
    for move in shift:
        if move[0] == 0:
            for _ in range(move[1]):
                l.append(l.pop(0))
        if move[0] == 1:
            for _ in range(move[1]):
                l = [l.pop()] + l
                
    return ''.join(l)



print(stringShift("abc", [[0,1],[1,2]]))