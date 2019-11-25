# TODO
# from queue import Queue 
from graph import canvas
from search import tools 

def bfs(start, end, obstacles = [], show_details = False):
    # 1. if start and end are the same return []
    # 2. if start and end are adjacent(neighbors) return end
    # 3. create empty queue for BFS
    # 4. insert start position to queue
    # 5. create visited dict containing position:neighbors 
    # 6. remove start from queue and then explore its neighbors
    # 7. set graph equal to all the available neighbors
    # 8. if neighbor has not been visited then add to visited{}. Push neighbor to queue.
    # 9 if neighbor is equal to end return path

    if tools.cell_equal(start, end):  #(1)
        return []

    if tools.is_adjacent(start, end): #(2)
        return [end]

    queue = []                #(3)
    queue.append(start)                 #(4)
    visited = {tools.cell_coordinates(start): None}  #(5)

    while queue:                  
        node = queue.pop(0)          #(6)
        adj = tools.graph(node, visited, obstacles)    #(7)

        for neighbor in adj:                     
            if tools.cell_coordinates(neighbor) in visited.keys():  #(8)
                continue

            visited[tools.cell_coordinates(neighbor)] = neighbor
            queue.append(neighbor)

            if tools.cell_equal(neighbor, end):         #(9)
                path = tools.path(visited, tools.cell_coordinates(neighbor))
                return path[1:] + [end]

            if show_details:
                canvas.draw_cell(neighbor, canvas.COLOR.DARK_GREEN.value)
                canvas.update() 
    return None