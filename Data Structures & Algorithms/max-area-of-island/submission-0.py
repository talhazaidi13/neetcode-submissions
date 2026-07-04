class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW,COL=len(grid),len(grid[0]) ; visited=[]
        def dfs(r,c):
            if (r<0 or c<0 or r>=ROW or c>=COL or 
                grid[r][c]==0 or (r,c) in visited):
               return 0
            visited.append((r,c))
            return (1+ dfs(r+1,c)+ dfs(r-1,c)+
                       dfs(r,c+1)+ dfs(r,c-1))
        area = []; island=0; max_area = 0
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j]==1:
                    island = dfs(i,j)
                    if island:
                        max_area = max(max_area, island)
                        area.append(island)
        print('area',area); print('max_area',max_area); 
        return max_area