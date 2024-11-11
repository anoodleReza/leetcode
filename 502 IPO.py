import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        size = len(profits)
        projects = zip(capital, profits)
        projects = sorted(projects)
        maxHeap = []
        i = 0

        for x in range(k):
            # iterate all projects and check if we can afford it
            while i < size and w >= projects[i][0]:
                # push the profit to the maxHeap
                # Python uses minHeap -> maxHeap = -minHeap
                heapq.heappush(maxHeap, -projects[i][1])
                i += 1
            if maxHeap:
                # subtract the cost of the project
                w -= heapq.heappop(maxHeap)
        return w