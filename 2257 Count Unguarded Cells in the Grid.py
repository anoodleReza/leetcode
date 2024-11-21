class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        vision = [[0]*n for _ in range(m)]
        for x in walls:
            vision[x[0]][x[1]] = 2
        for x in guards:
            vision[x[0]][x[1]] = 3
        wg = (2,3)

        for x in guards:
            r, c = x[0], x[1]
            # up
            for i in range(r-1, -1, -1):
                if vision[i][c] in wg:
                    break
                vision[i][c] = 1
            # down
            for i in range(r+1, m):
                if vision[i][c] in wg:
                    break
                vision[i][c] = 1
            # left
            for i in range(c-1, -1, -1):
                if vision[r][i] in wg:
                    break
                vision[r][i] = 1
            # right
            for i in range(c+1, n):
                if vision[r][i] in wg:
                    break
                vision[r][i] = 1
        unguarded = 0
        for i in range(m):
            for j in range(n):
                if vision[i][j] == 0:
                    unguarded += 1
        return unguarded
