def mergeAlternately(word1, word2):
        new_word = []
        word1_length = len(word1)
        word2_length = len(word2)
        max_length = max(word1_length , word2_length)
        for i in range(max_length):
            if i < word1_length:
                new_word.append(word1[i])
            if i < word2_length:
                new_word.append(word2[i])
        
        return "".join(new_word)

print(mergeAlternately("abc" , "pqr"))
print(mergeAlternately("abc" , "pqrs"))