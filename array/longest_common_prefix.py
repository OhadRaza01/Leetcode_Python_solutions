
def longestcommonprefix(strs):
    if len(strs) == 1:
        return strs[0]
    strs.sort()
    first = strs[0]
    last = strs[-1]
    i = 0 
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1
        
    return first[:i]

print(longestcommonprefix(["ohad" , "ohid" , "ohed"]))