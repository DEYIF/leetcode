from typing import List
class Solution:
    def __init__(self):
        self.result = []
        self.directs = [(-1,0),(1,0),(0,-1),(0,1)]
        self.m, self.n = 0, 0
        self.visited = None
        self.canflowtopacific = None
        self.canflowtoatlantic = None
        
    def in_area(self,x,y):
        return 0 <= x < self.m and 0 <= y < self.n

    def dfs(self,heights,x,y,is_pacific):
        if self.visited[x][y] == 1:
            return
        self.visited[x][y] = 1
        if is_pacific:
            self.canflowtopacific[x][y] = 1
        else:
            self.canflowtoatlantic[x][y] = 1
        for i in range(4):
            newx = x+self.directs[i][0]
            newy = y+self.directs[i][1]
            if not self.in_area(newx,newy):
                continue
            if heights[x][y] > heights[newx][newy]:
                continue
            self.dfs(heights,newx,newy,is_pacific)
        return

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.m, self.n = len(heights), len(heights[0])
        self.canflowtoatlantic = [[0]*self.n for _ in range(self.m)]
        self.canflowtopacific = [[0]*self.n for _ in range(self.m)]

        self.visited = [[0]*self.n for _ in range(self.m)]
        i = 0
        for j in range(self.n):
            self.dfs(heights,i,j,True)
        
        self.visited = [[0]*self.n for _ in range(self.m)]
        j = 0
        for i in range(self.m):
            self.dfs(heights,i,j,True)
        
        self.visited = [[0]*self.n for _ in range(self.m)]
        i = self.m-1
        for j in range(self.n):
            self.dfs(heights,i,j,False)
        
        self.visited = [[0]*self.n for _ in range(self.m)]
        j = self.n-1
        for i in range(self.m):
            self.dfs(heights,i,j,False)

        for i in range(self.m):
            for j in range(self.n):
                if self.canflowtoatlantic[i][j] == 1 and self.canflowtopacific[i][j] == 1:
                    self.result.append([i,j])
        return self.result