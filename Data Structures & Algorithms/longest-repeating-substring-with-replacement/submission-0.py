class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_freq = 0
        result = 0
        strs = {}

        for right in range(len(s)):
            window = s[left:right+1]

            if s[right] in strs:
                strs[s[right] ] += 1
            else:
                strs[s[right]] = 1
            
            max_freq = max(max_freq,strs[s[right]])

            window_size = right - left + 1
            while window_size - max_freq > k:
                strs[s[left]] -= 1
                left += 1
                window_size = right - left + 1

            result = max(result, right - left + 1)

        return result
            