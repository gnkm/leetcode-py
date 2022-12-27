"""55. Jump Game

URL: https://leetcode.com/problems/jump-game/

## Description

You are given an integer array `nums`. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return `true` if you can reach the last index, or `false` otherwise.

difficulty: Medium
"""

from typing import Dict, List, Union

import icecream


debug = icecream.ic


# my code.
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True

        if nums[0] >= len(nums):
            return True

        if 0 not in nums:
            return True

        # @TODO: Implement main logic.

        return True


class SolutionRecursively:
    """Implemented with recursion.

    Time limit exceed in case 72.
    """
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True

        if nums[0] >= len(nums):
            return True

        if 0 not in nums:
            return True

        return any([self.canJump(nums[i:]) for i in range(1, nums[0] + 1)])


class SolutionModelAnswer:
    """
    {URL}
    """

    def canJump(self, nums: List[int]) -> bool:
        return True


class SolutionEx01(object):
    """
    https://leetcode.com/problems/jump-game/solutions/774588/python-easy-linear-time-o-n-and-space-o-1-explanation/?orderBy=most_votes&languageTags=python3
    """

    def canJump(self, nums: List[int]) -> bool:
        reachableIndex = 0
        for index, num in enumerate(nums):
            if index + num >= reachableIndex:
                reachableIndex = index + num
            if index == reachableIndex:
                break

        return reachableIndex >= len(nums) - 1


if __name__ == "__main__":
    pass
