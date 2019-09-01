class Solution:
    def reOrderArray(self, array):
        # write code here
        if array is None or len(array) == 0:
            return []
        
        for i in range(len(array)):
            for j in range(len(array) - 1, i, -1):
                if (array[j - 1] %2 == 0) and (array[j] %2 == 1):
                    array[j], array[j - 1] = array[j - 1], array[j]
        
        return array

s = Solution()
print(s.reOrderArray([2, 4, 6, 1, 3, 5]))