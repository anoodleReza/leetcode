from typing import List

# You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:

# difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
# worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most worker[j]).
# Every worker can be assigned at most one job, but one job can be completed multiple times.

# For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker cannot complete any job, their profit is $0.
# Return the maximum profit we can achieve after assigning the workers to the jobs.
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Sort the jobs by difficulty
        jobs = [(d, p) for d, p in zip(difficulty, profit)]
        jobs.sort()
        worker.sort()
        max_profit = 0
        i = 0
        last_job = (0, 0)

        for w in worker:
        # For each worker, find the job with the highest profit that they can complete
            while i < len(jobs) and jobs[i][0] <= w:
                # If the current job has a higher profit than the last job, update the last job
                if jobs[i][1] > last_job[1]:
                    last_job = jobs[i]
                i += 1
            max_profit += last_job[1]
        return max_profit