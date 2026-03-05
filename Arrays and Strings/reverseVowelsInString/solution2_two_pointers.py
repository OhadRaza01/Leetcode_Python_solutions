def reverseVowels(s):
    
    vowels = "aeiouAEIOU"
    s_list = list(s)
    
    start = 0
    end = (len(s_list) - 1)
    
    while start < end:
        
        if s_list[start] not in vowels:
            start += 1
            
        elif s_list[end] not in vowels:
            end -= 1
            
        else:
            s_list[start] , s_list[end] = s_list[end] , s_list[start]
            
            start += 1
            end -= 1
        
    return "".join(s_list)

print(reverseVowels("IceCreAm"))
print(reverseVowels("leetcode"))