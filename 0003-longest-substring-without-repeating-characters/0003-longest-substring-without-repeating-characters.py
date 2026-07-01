class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        create_set = set()
        left = 0
        max_long = 0 
        for right in range(len(s)):
            while s[right] in create_set:
                create_set.remove(s[left])
                left += 1 
            create_set.add(s[right])
            max_long = max(max_long, right-left+1)
        return max_long