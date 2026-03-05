def reverseVowels(s):
    
    vowels = "aeiouAEIOU"
    s_list = list(s)
    
    v,indexes = [],[]
    
    
    for i in range(len(s_list)):
        if s_list[i] in vowels:
            v.append(s_list[i])
            indexes.append(i)
    
    v.reverse()
    
    for i in range(len(indexes)):
        s_list[indexes[i]] = v[i]
        
    return "".join(s_list)

print(reverseVowels("IceCreAm"))
print(reverseVowels("leetcode"))