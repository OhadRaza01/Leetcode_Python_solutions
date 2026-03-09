# increasing triplet subsequence 

# Goal is to find if the current array contain increasing triplet subsequence

#APPROACH
'''
our goal is to track smallest and second smallest in the array
'''

def tripletSubsequence(nums):
    
    first_small = float("inf")
    second_small = float("inf")
    
    for n in nums:
        if n <= first_small:
            first_small = n
        
        elif n <= second_small:
            second_small = n
            
        else:
            return True
    
    return False

print(tripletSubsequence([5,4,3,2,1]))