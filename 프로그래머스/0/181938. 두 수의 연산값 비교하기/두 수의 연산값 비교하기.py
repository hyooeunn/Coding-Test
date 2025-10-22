def solution(a, b):
    strPlus = int(str(a) + str(b))
    multiply = 2 * a * b
    
    if strPlus >= multiply:
        return strPlus
    else:
        return multiply