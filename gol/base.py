# -*- coding: utf-8 -*-
"""

"""

import random


class Cell(object):
    """

    """
    def __init__(self, is_alive=None, neighbours=0):
        """

        """
        self.is_alive = bool(is_alive if is_alive is not None else random.randint(0, 1))
        self.neighbours = neighbours

    def evolve(self):
        """

        """
        if self.neighbours == 2:
            pass
        elif self.neighbours == 3:
            self.is_alive = True
        else:
            self.is_alive = False
        self.neighbours = 0

    def __str__(self):
        return "[]" if self.is_alive else "  "


class Grid(object):
    """

    """
    def __init__(self, cells=None, rows=5, columns=11):
        """

        """
        if cells == "demo":
            cells = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                     [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]
        if cells is None:
            self.cells = [[Cell() for x in range(columns)] for y in range(rows)]
        else:
            self.cells = [[Cell(cell) for cell in row] for row in cells]
        self.update_neighbourhoods()


    def update_neighbourhoods(self):
        """

        """
        for y in range(len(self.cells)):
            for x in range(len(self.cells[y])):
                self.update_neighbourhood(y, x)

    def update_neighbourhood(self, row, column):
        """

        """
        if self.cells[row][column].is_alive:
            for y in range(row - 1, row + 2):
                for x in range(column - 1, column + 2, 2 if y == row else 1):
                    self.cells[y % len(self.cells)][x % len(self.cells[0])].neighbours += 1

    def evolve(self, cycles=1):
        """

        """
        for cycle in range(cycles):
            self.update_cells()
            self.update_neighbourhoods()


    def update_cells(self):
        """

        """
        for y in range(len(self.cells)):
            for x in range(len(self.cells[y])):
                self.cells[y][x].evolve()

    def __str__(self):
        string = ""
        for y in range(len(self.cells)):
            for x in range(len(self.cells[y])):
                string += str(self.cells[y][x])
            string += "\n"
        return string[:-1]

