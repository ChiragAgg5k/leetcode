from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """Binary Search Algorithm
         Youtube explaination : https://www.youtube.com/watch?v=s4DPM8ct1pI

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
