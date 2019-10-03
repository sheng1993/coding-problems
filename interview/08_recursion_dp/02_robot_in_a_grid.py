# Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
# The robot can only move in two directions, right and down, but certain cells are "off limits" such that
# the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
# the bottom right.

def get_path(maze):
    if not maze or len(maze) == 0:
        return None
    path = []
    if get_path(maze, len(maze) - 1, len(maze[0]) - 1, path):
        return path
    return None

def get_path(maze, row, col, path: list):
    if col < 0 or row < 0 or not maze[row][col]:
        return False
    
    is_at_origin = row == 0 and col == 0

    if is_at_origin or get_path(maze, row, col - 1, path) or\
        get_path(maze, row - 1, col, path):
        path.append((row, col))
        return True
    
    return False