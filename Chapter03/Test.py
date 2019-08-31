class Solution:
    def reOrderArray(self, array):
        # write code here
        if array is None or len(array) == 0:
            return
        
        begin = 0
        end = len(array) - 1
        while begin < end:
            while begin < end and array[begin] % 2 != 0:
                begin += 1
            while begin < end and array[end] %2 == 0:
                end -= 1
            if begin < end:
                temp = array[begin]
                array[begin] = array[end]
                array[end] = temp
        return array

s = Solution()
print(s.reOrderArray([1,2,3,4,5,6,7]))