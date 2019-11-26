# TODO
from graph import canvas
from search import tools 

def bfs(start, end, obstacles = [], show_details = False):
    # 1. create empty queue for BFS
    # 2. insert start position to queue
    # 3. create visited dict containing position:neighbors 
    # 4. remove start from queue and then explore its neighbors
    # 5. set graph equal to all the available neighbors
    # 6. if neighbor has not been visited then add to visited{}. Push neighbor to queue.
    # 7 if neighbor is equal to end return path
    # 8. color in visited node

    queue = []                #(1)
    queue.append(start)                 #(2)
    visited = {tools.cell_coordinates(start): None}  #(3)

    while queue:                  
        node = queue.pop(0)          #(4)
        graph = tools.graph(node, visited, obstacles)    #(5)

        for neighbor in graph:                     
            if tools.cell_coordinates(neighbor) in visited.keys():  #(6)
                continue

            visited[tools.cell_coordinates(neighbor)] = neighbor
            queue.append(neighbor)

            if tools.cell_equal(neighbor, end):         #(7)
                path = tools.path(visited, tools.cell_coordinates(neighbor))
                return path[1:] + [end]

            if show_details:                        #(8)
                canvas.draw_cell(neighbor, canvas.COLOR.DARK_GREEN.value)
                canvas.update() 
    return None