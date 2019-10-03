#python 3.5.2

class Solution:
    
    def numIslands(self, grid):
        # your code here
        x = [0 for _ in range(len(grid[0]))]
        max_area = 0
        for r in range(len(grid)):
            for j in range(len(grid[0])):
                x[j] += 1 if grid[r][j] == '1' else 0
            min_h = -1
            min_col = 1
            for j in range(1, len(grid[0])):
                if x[j] == 0:
                    max_area = max(max_area, min_col * min_h)
                    min_h = -1
                else:
                    if min_h == -1:
                        min_h = x[j]
                        min_col = 1
                    else:
                        min_h = min(min_h, x[j])
                min_col += 1
        return max_area

    
def get_matrix():
    row = int(input())
    col = int(input())
    grid = [["0"]*col]*row

    for i in range(row):
        line = input()
        grid[i] = list(line)[0:col]
    return grid

        
if __name__ == "__main__":
    sol = Solution()
    matrix = get_matrix()
    islands = sol.numIslands(matrix)
    print(islands)
