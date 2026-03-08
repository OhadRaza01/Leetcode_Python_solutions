

nums = [1,2,3,4]

result = [1]

# for i in range(1 , len(nums)):
#     result[i] = result[i-1] * nums [i-1]
    
# print(result)

# right = 1
# for i in range(len(nums) - 1 , -1 , -1 ):
#     result[i] = result[i] * right
#     right = right * nums[i]

# print(result)

for i in range(len(nums) - 2 , -1 , -1):
    result.insert(0 , result[0] * nums[i+1])

left = 1
for i in range(len(nums)):
    result[i] *= left
    left = left * nums[i]
print(result)