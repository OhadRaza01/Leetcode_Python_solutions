def kidsWithCandies(candies, extraCandies):
        result = []
        maximum = max(candies)
        for i in candies:
            if i + extraCandies >= maximum:
                result.append(True)
            else:
                result.append(False)
        return result
    
print(kidsWithCandies([2,3,5,1,1] , 3))  # expected [true , true , true , false , false]
