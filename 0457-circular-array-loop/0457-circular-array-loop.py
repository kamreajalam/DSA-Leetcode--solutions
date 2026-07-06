class Solution:
    def circularArrayLoop(self, nums):
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        for i in range(n):

            direction = nums[i] > 0

            slow = i
            fast = i

            while True:

                if (nums[slow] > 0) != direction:
                    break

                if (nums[fast] > 0) != direction:
                    break

                next_fast = next_index(fast)

                if (nums[next_fast] > 0) != direction:
                    break

                slow = next_index(slow)
                fast = next_index(next_fast)

                if slow == fast:

                    if slow == next_index(slow):
                        break

                    return True

        return False

# Time Complexity
# Time: O(n)
# # Space: O(1)