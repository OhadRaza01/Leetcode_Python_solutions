
       
       
chars = ["a" , "a" , "b" , "b" , "c" , "c" , "c"]
        
prev = ""
current = ""
count = 1
chrr = []
for i in range(1 , len(chars)):
    prev += chars[i-1]
    current += chars[i]

    if prev == current:
        count += 1
        prev = ""
        current = ""
    else:
        chrr.append(prev)
        chrr.append(count)
        count = 0 
        prev = current

print(chrr)
