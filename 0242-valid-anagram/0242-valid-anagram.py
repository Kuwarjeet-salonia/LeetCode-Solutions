class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for ch in t:
            if ch in s:
                t = t.replace(ch,"",1)
                s = s.replace(ch,"",1)
            else:
                return False
        return len(t)==0 and len(s)==0
