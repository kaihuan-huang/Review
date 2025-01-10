from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        使用深度优先搜索 (DFS) 计算岛屿的数量。
        :param grid: 2D 网格，包含 '1'（陆地）和 '0'（水）
        :return: 岛屿数量
        """
        def dfs(r, c):
            # 如果越界或当前位置为水，直接返回
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == "0":
                return

            # 将当前陆地标记为已访问
            grid[r][c] = "0"

            # 递归搜索上下左右的格子
            dfs(r - 1, c)  # 上
            dfs(r + 1, c)  # 下
            dfs(r, c - 1)  # 左
            dfs(r, c + 1)  # 右

        # 边界条件：如果网格为空，返回 0
        if not grid or not grid[0]:
            return 0

        num_islands = 0

        # 遍历整个网格
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # 如果遇到陆地，说明发现了一个新岛屿
                if grid[r][c] == "1":
                    num_islands += 1  # 岛屿计数加一
                    dfs(r, c)  # 使用 DFS 沉没这个岛屿

        return num_islands