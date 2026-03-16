

def maxOp(nums , k):
    
    nums.sort()
    
    operations = 0
    j = len(nums) - 1
    i = 0
    while i < j:
        
        current_sum = nums[i] + nums[j]
        
        if current_sum == k:   
            operations += 1
            i += 1
            j -= 1
            
        elif current_sum < k:
            i += 1
        else:
            j -= 1
        
        
    return operations

print(maxOp([1,2,3,4] , 5))
print(maxOp([3,1,3,4,3] , 6))