def maxArea(height):
        
        water = 0
        i = 0
        j = len(height) -1

        while i < j:

            w = j - i
            h = min(height[i] , height[j])

            max_water = w * h
            
            if max_water > water:
                water = max_water

            if height[i] >= height[j]:
                j -= 1 
                
            else:
                i += 1

        return water
    
print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([1,1]))