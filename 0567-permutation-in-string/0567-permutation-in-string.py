class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        need = {}
        window = {}

        for ch in s1:
            need[ch] = need.get(ch, 0) + 1

        left = 0

        for right in range(len(s2)):

            window[s2[right]] = window.get(s2[right], 0) + 1

            if right - left + 1 > len(s1):

                window[s2[left]] -= 1

                if window[s2[left]] == 0:
                    del window[s2[left]]

                left += 1

            if right - left + 1 == len(s1):

                if need == window:
                    return True

        return False

# Time: O(m + n)
# Space: O(26) = O(1)