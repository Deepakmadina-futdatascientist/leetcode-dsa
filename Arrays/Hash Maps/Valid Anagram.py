"""
Problem: Valid Anagram
Platform: LeetCode
Difficulty: Easy

Approach:
1. If the lengths of both strings are different, return False.
2. Store the frequency of each character of the first string in a dictionary.
3. Traverse the second string:
   - If the character is not present in the dictionary, return False.
   - Otherwise, decrease its frequency.
   - If the frequency becomes negative, return False.
4. Finally, check whether all frequencies are 0.
   If yes, return True; otherwise return False.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def isAnagram(self, s, t):
        f = {}

        if len(s) != len(t):
            return False

        for i, n in enumerate(s):
            if n in f:
                f[n] = f[n] + 1
            else:
                f[n] = 1

        for j, m in enumerate(t):
            if m not in f:
                return False

            f[m] = f[m] - 1

            if f[m] < 0:
                return False

        for value in f.values():
            if value != 0:
                return False

        return True
