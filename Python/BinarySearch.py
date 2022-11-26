from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """Binary Search Algorithm
         Youtube explanation : https://www.youtube.com/watch?v=s4DPM8ct1pI

        Args:
            nums (List[int]): List containing integers , must be sorted in asc
            target (int): integer to find index of

        Returns:
            int: index of the target in the array
                 -1 in case target not present in array
        """

        l = 0
        r = len(nums)-1

        while l <= r:
            mid = (l+r)//2

            if nums[mid] < target:
                l = mid+1

            elif nums[mid] > target:
                r = mid-1
            else:
                return mid

        return -1

if __name__ == "__main__":
    
    # input space separated list from user
    testArray = list(map(int,input("Enter a test array: ").split()))
    testTarget = int(input("Enter a target value: "))
    
    binary_search = Solution()
    print("Index =",binary_search.search(testArray,testTarget))
