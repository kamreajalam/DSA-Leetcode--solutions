class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        left = 0
        window_cost = 0
        ans = 0

        for right in range(len(s)):

            window_cost += abs(ord(s[right]) - ord(t[right]))

            while window_cost > maxCost:

                window_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            ans = max(ans, right - left + 1)

        return ans

# Time: O(n)
# Space: O(1)