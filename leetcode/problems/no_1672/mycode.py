"""1672. Richest Customer Wealth

URL: https://leetcode.com/problems/richest-customer-wealth/

## Description

You are given an `m x n` integer grid `accounts` where `accounts[i][j]` is the amount of money the i th customer has in the j th bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

difficulty: Easy
"""

from typing import Dict, List, Union


# my code.
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(account) for account in accounts])


class SolutionModelAnswer:
    """
    nothing.
    """

    pass
