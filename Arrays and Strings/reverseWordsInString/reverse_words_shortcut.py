def reverseWords(s):
    l = s.split()
    return " ".join(l[::-1]) #pythonic way

print(reverseWords("  my name is   ohad"))