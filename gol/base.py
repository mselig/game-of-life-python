# -*- coding: utf-8 -*-
"""

"""

import random


class Cell(object):
    """

    """
    def __init__(self, isAlive=None, neighbours=0):
        """

        """
        self.isAlive = bool(isAlive if isAlive is not None else random.randint(0, 1))
        self.neighbours = neighbours

    def evolve(self):
        """

        """
        if self.neighbours == 2:
            pass
        elif self.neighbours == 3:
            self.isAlive = True
        else:
            self.isAlive = False
        self.neighbours = 0

    def __str__(self):
        return "[]" if self.isAlive else "  "


class Grid(object):
    """

    """
    def __init__(self, cells=None, rows=5, columns=11):
        """

        """
        if cells is None:
            self.cells = [[Cell() for x in range(columns)] for y in range(rows)]
        else:
            self.cells = [[Cell(cell) for cell in row] for row in cells]


    def evolve(self):
        """

        """
        self.update_neighbourhoods()
        self.update_cells()


    def update_cells(self):
        """

        """
        for y in range(len(self.cells)):
            for x in range(len(self.cells[y])):
                self.cells[y][x].evolve()

    def update_neighbourhoods(self):
        """

        """
        for y in range(len(self.cells)):
            for x in range(len(self.cells[y])):
                self.update_neighbourhood(y, x)

#                self.cells[rr][cc].count_neighbours(
#                       [cell for row in self.cells[rr - 1:rr + 2] for cell in row[cc - 1:cc + 2]])

    def update_neighbourhood(self, row, column):
        """

        """
        if self.cells[row][column].isAlive:
            for y in range(row - 1, row + 2):
                for x in range(column - 1, column + 2, 2 if y == row else 1):
                    self.cells[y % len(self.cells)][x % len(self.cells[0])].neighbours += 1
#                    self.cells[y][x].increment_neighbours()
#                    print(self.cells[y][x].neighbours)

    def __str__(self):
        string = ""
        for y in range(len(self.cells)):
            for x in range(len(self.cells[y])):
                string += str(self.cells[y][x])
            string += "\n"
        return string[:-1]

