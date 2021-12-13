#instruction link: https://www.codewars.com/kata/6177b4119b69a40034305f14
def solution(mtrx):
    a = ""
    for i in range(len(mtrx)):
        for j in range(len(mtrx[i])):
            if mtrx[i][j] == "^" or mtrx[i][j] == ">" or mtrx[i][j] == "<" or mtrx[i][j] == "v":
                a = str(mtrx[i][j])
                d = i
                key = j
                break
    
    if a == ">":
        if key + 1 == len(mtrx):
            return False
        for k in range(key + 1, len(mtrx[i])):
            if mtrx[d][k]=='x':
                return True
        return False
    if a == "v":
        if d + 1 == len(mtrx):
            return False
        for k in range(d + 1, len(mtrx)):
            if mtrx[k][key] == "x":
                return True
        return False
            
    if a == "<":
        if key == 0:
            return False
        for k in range(key):
            if mtrx[d][k]=='x':
                return True
        return False
    if a == "^":
        if d == 0:
            return False
        for k in range(d):
            if mtrx[k][key] == "x":
                return True
        return False