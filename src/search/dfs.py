from graph import canvas 
from search import tools 

def isValidCell(cell, visited, obstacles):
    x, y = cell
    if x < 0 or x >= canvas.WIDTH:
        return False
    if y < 0 or y >= canvas.HEIGHT:
        return False
    if cell in visited:
        return False
    for x, y in obstacles:
        if cell[0] == x and cell[1] == y:
            return False
    return True

def dfs(start, end, obstacles=[], show_details=False):
    # 1. create stack for DFS
    # 2. visited contains all visited nodes
    # 3. push start node to stack
    # 4. pop a node from stack

    stack = [(start, [start])]
    visited = set()

    mov = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while stack:
        (vertex, path) = stack.pop() 

        graph = list(filter(lambda x: isValidCell(x, visited, obstacles), [tuple(map(sum, zip(vertex, dir))) for dir in mov]))

        if vertex not in visited:
            if tools.cell_equal(vertex, end):
                return path 
            visited.add(vertex) 
            for neighbor in graph:
                stack.append((neighbor, path+[neighbor]))

        if show_details:
            canvas.draw_cell(vertex, canvas.COLOR.DARK_GREEN.value)
            canvas.update()

    return None