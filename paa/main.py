def equals_str(str1, str2, in1, fim1, in2):
    i = 0
    for i in range(in1,fim1):
        in2 += 1
        if str1[i] != str2[in2]:
            return False
    
    return True

def check(str1, str2, in1, fim1, in2, fim2):
    leght = (fim1 - in1 + 1)

    if leght and 1:
        return equals_str(str1,str2,in1,fim1,in1)
    else:
        mid = leght / 2
        if check(str1, str2, in1, in1 + mid - 1, in2, in2 + mid - 1) and check(str1, str2, in1 + mid, fim1, in2 + mid, fim2):
            return True
        if check(str1, str2, in1, in1+ mid - 1, in2 + mid, fim2) and check(str1, str2, in1+mid, fim1, in2,in2 + mid - 1):
            return True

    return False        

input01 = str(input())
input02 = str(input())

if check(input01, input02, 0, len(input01) - 1, 0, len(input02) - 1):
    print('YES')
else:
    print('NO')