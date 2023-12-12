# https://leetcode.com/problems/maximum-profit-in-job-scheduling/ 

class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        dp = [0] * len(jobs)
        dp[0] = jobs[0][2]

        for i in range(1, len(jobs)):
            latest_non_overlapping_job = self.binary_search(jobs, i)
            incl_prof = jobs[i][2] + (dp[latest_non_overlapping_job] if latest_non_overlapping_job != -1 else 0)
            dp[i] = max(dp[i - 1], incl_prof)

        return dp[-1]

    def binary_search(self, jobs, current_job):
        low, high = 0, current_job - 1

        while low <= high:
            mid = (low + high) // 2
            if jobs[mid][1] <= jobs[current_job][0]:
                if jobs[mid + 1][1] <= jobs[current_job][0]:
                    low = mid + 1
                else:
                    return mid
            else:
                high = mid - 1

        return -1

sol = Solution()

startTime1 = [1, 2, 3, 3]
endTime1 = [3, 4, 5, 6]
profit1 = [50, 10, 40, 70]
print(sol.jobScheduling(startTime1, endTime1, profit1))  

startTime2 = [1, 2, 3, 4, 6]
endTime2 = [3, 5, 10, 6, 9]
profit2 = [20, 20, 100, 70, 60]
print(sol.jobScheduling(startTime2, endTime2, profit2)) 

startTime3 = [1, 1, 1]
endTime3 = [2, 3, 4]
profit3 = [5, 6, 4]
print(sol.jobScheduling(startTime3, endTime3, profit3))  
