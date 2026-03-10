chars = ["a", "a", "b", "b", "c", "c", "c"]

writer, reader = 0, 0
while reader < len(chars):
		
    chars[writer] = chars[reader]
    count = 1
			
    while reader + 1 < len(chars) and chars[reader] == chars[reader+1]:
        reader += 1
        count += 1
			
    if count > 1:
        for c in str(count):
            chars[writer+1] = c
            writer += 1
            
    reader += 1
    writer += 1

print(writer)
print(chars)
