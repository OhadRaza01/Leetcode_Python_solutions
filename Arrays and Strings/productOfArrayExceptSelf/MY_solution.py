def productExceptSelf(nums):
        
        answer = []
        left = [1]
        right = [1]

        for i in range(1 ,len(nums)):
            left.append(left[i-1] * nums[i-1])
        
        
        for i in range(len(nums) - 2 , -1 , -1):
            right.insert(0 , right[0] * nums[i+1])
            

        for i in range(len(nums)):
            answer.append(left[i] * right[i])

        return answer
    
print(productExceptSelf([1,2,3,4]))

#time complexity O(n)
#space complexity O(n)