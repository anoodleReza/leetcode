class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = set(range(n))
        for strong, weak in edges:
            graph.discard(weak)
        if len(graph) == 1:
            return graph.pop()
        else:
            return -1