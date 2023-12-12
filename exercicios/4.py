# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height):
        n = len(height)
        if n <= 2:
            return 0

        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        total_water = 0
        for i in range(n):
            total_water += min(left_max[i], right_max[i]) - height[i]

        return total_water

# Exemplos de uso:
sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # Saída: 6
print(sol.trap([4,2,0,3,2,5]))              # Saída: 9
