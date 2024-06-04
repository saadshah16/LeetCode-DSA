class Solution:
    def longestPalindrome(self, s: str) -> int:
        sett = set()
        for letter in s:
            if letter not in sett:
                sett.add(letter)
            else:
                sett.remove(letter)
        if len(sett) != 0:
            return len(s) - len(sett) + 1
        else:
            return len(s)