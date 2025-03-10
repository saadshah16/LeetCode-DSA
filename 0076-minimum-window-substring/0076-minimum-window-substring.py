class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""
        
        t_count = {}
        window = {}
        
        for c in t:
            t_count[c] = 1 + t_count.get(c,0)
        
        have = 0
        need = len(t_count)
        min_w = float('inf')
        res = [-1,-1]
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)

            if c in t_count and window[c] == t_count[c]:
                have += 1
            
            while have == need:
                w = r-l+1
                if w < min_w:
                    res = [l,r]
                    min_w = w
                window[s[l]] -= 1
                if s[l] in t_count and window[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1
        l , r = res
        return s[l:r+1] if min_w != float('inf') else ""


