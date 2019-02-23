# -*- coding: utf-8 -*-
"""
    hosts the class `GameOfLife`
"""

from gol.base import Grid


class GameOfLife(object):
    """
        implements Conway's Game of Life
    """
    def __init__(self, cells=None, rows=5, columns=11):
        """
            initialises a `GameOfLife` on two-dimensional `Grid` of `Cell`s
        """
        self.grid = Grid(cells, rows, columns)

    def evolve(self, cycles=11):
        """
            processes a number of evolution cycles for the game
        """
        print(f"{'-' * 80}\nevolution cycle: 000\n{self.grid}\n")
        for cycle in range(cycles):
            self.grid.evolve()
            print(f"{'-' * 80}\nevolution cycle: {cycle + 1:#03d}\n{self.grid}\n")

