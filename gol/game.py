# -*- coding: utf-8 -*-
"""

"""

from gol.base import Grid


class GameOfLife(object):
    """

    """
    def __init__(self, cells=None, rows=5, columns=11):
        """

        """
        self.grid = Grid(cells, rows, columns)

    def evolve(self, cycles=11):
        """

        """
        print(f"{'-' * 80}\nevolution cycle: 000\n{self.grid}\n")
        for cycle in range(cycles):
            self.grid.evolve()
            print(f"{'-' * 80}\nevolution cycle: {cycle + 1:#03d}\n{self.grid}\n")

