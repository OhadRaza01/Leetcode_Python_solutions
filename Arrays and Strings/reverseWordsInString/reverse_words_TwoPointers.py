
def reverseWords(s):
    
    s_list = s.split()
    
    start = 0
    end = len(s_list) -1
    
    while start < end:
        s_list[start] , s_list[end] = s_list[end] , s_list[start]
        start += 1
        end -= 1

    return " ".join(s_list)

print(reverseWords("  my  name  is  ohad  "))
