

def LCS(str1,str2):
    if not str1:
        return st2
    if not  st2:
        return  str1

    dp = [[0 for i in range(len(str2))]for j in range(len(str1))
