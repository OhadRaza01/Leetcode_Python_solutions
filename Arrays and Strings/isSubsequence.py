
def isSubsequence(s , t):
    
    j = 0
    for char in t:
        if j < len(s) and s[j] == char:
            j +=1 
    
    return len(s) == j

print(isSubsequence("abc" , "ahbghmnhc"))
print(isSubsequence("" , "ahbghmnhc"))
print(isSubsequence("acb" , "ahbghmnhc"))