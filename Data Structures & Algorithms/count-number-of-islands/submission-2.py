class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # land = []
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == 1:
        #             land.append([i,j])
        # island = 0
        # for i in range(1, len(land)):
        #     if ( land[i][0] - land[i-1][0] ) < 2   or ( land[i][1] - land[i-1][1] ) < 2:

        ROW,COL=len(grid),len(grid[0]) ; visited=[]
        def dfs(r,c):
            if (r<0 or c<0 or r>=ROW or c>=COL or 
                grid[r][c]=="0" or (r,c) in visited):
               return 0
            visited.append((r,c))
            return (1+ dfs(r+1,c)+ dfs(r-1,c)+
                       dfs(r,c+1)+ dfs(r,c-1))
        area = []; island=0; max_area = 0
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j]=="1":
                    island = dfs(i,j)
                    if island:
                        max_area = max(max_area, island)
                        area.append(island)
        print('area',area); print('max_area',max_area); 
        return len(area)
                     
