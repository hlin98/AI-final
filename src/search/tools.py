"""
Copyright 2017 ManerFan

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from graph import canvas


def cell_equal(cell1: (int, int), cell2: (int, int)):
    """
    returns if the two cells are equal
    """
    if cell1 and not cell2:
        return False

    if not cell1 and cell2:
        return False

    if not cell1 and not cell2:
        return True

    (x1, y1) = cell1
    (x2, y2) = cell2

    return x1 == x2 and y1 == y2


def cell_coordinates(cell):
    (x, y) = cell
    return f"({x},{y})"


def is_adjacent(cell1, cell2):
    # returns whether or not the cells are neighbors
    (x1, y1) = cell1
    (x2, y2) = cell2
    if x1 == x2 and abs(y1 - y2) == 1:
        return True
    if y1 == y2 and abs(x1 - x2) == 1:
        return True
    return False


def graph(cell, mark={}, obstacles=[]):
    """
    parameter meanings:
        cell: coordinates
        mark: traversed neighbors
        param obstacles: obstacle positions
        return: available neighbors
    """
    (x, y) = cell
    cells = [
        (x, y - 1),
        (x + 1, y),
        (x, y + 1),
        (x - 1, y)
    ]
    return filter(valid_cell(mark, obstacles), cells)


def path(mark, cell_id):
    """
    mark: visited cells
    cell_id: end position coordinates
    return: path

    # cell contains last visited neighbor before reaching end position
    # while there is still a previous neighbor:
    # set parent_id to be the coordinates of last visited neighbor
    # if neighbor was already visited then update cell to equal last visited neighbor of parent_id
    """
    path = []
    cell = mark[cell_id]

    while cell:
        path.append(cell)
        parent_id = cell_coordinates(cell)
        if parent_id in mark.keys():
            cell = mark[parent_id]
        else:
            break

    path.reverse()
    return path


def valid_cell(mark={}, obstacles=[]):
    def valid(cell):
        (x, y) = cell
        if x < 0 or x >= canvas.WIDTH:
            return False
        if y < 0 or y >= canvas.HEIGHT:
            return False
        if cell_coordinates(cell) in mark.keys():
            return False
        for obstacle in obstacles:
            if cell_equal(cell, obstacle):
                return False
        return True

    return valid


if __name__ == "__main__":
    assert cell_equal(None, None)
    assert not cell_equal(None, (1, 2))
    assert not cell_equal((1, 2), None)
    assert not cell_equal((1, 2), (3, 4))
    assert cell_equal((1, 2), (1, 2))

    print(cell_coordinates((1, 2)))
