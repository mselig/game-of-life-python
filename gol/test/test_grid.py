# -*- coding: utf-8 -*-

from gol.base import Cell, Grid


class TestGrid(object):

    def test_initialisation(self):
        grid = Grid()
        assert type(grid.cells) == list
        assert  len(grid.cells) == 5
        assert type(grid.cells[0]) == list
        assert  len(grid.cells[0]) == 11
        assert type(grid.cells[0][0]) == Cell
        grid = Grid(rows=3, columns=7)
        assert  len(grid.cells) == 3
        assert  len(grid.cells[0]) == 7
        grid = Grid([[0, 0, 1]])
        assert  len(grid.cells) == 1
        assert  len(grid.cells[0]) == 3
        assert type(grid.cells[0][0]) == Cell
        assert  not grid.cells[0][0].isAlive
        assert  not grid.cells[0][1].isAlive
        assert      grid.cells[0][2].isAlive


    def test_neighbourhood(self):
        grid = Grid([[0, 1, 0, 0],
                     [0, 0, 1, 1],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]])
        grid.update_neighbourhood(0, 0)
        assert [[cell.neighbours for cell in row] for row in grid.cells] \
                ==  [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]]
        grid.update_neighbourhood(0, 1)
        assert [[cell.neighbours for cell in row] for row in grid.cells] \
                ==  [[1, 0, 1, 0],
                     [1, 1, 1, 0],
                     [0, 0, 0, 0],
                     [1, 1, 1, 0]]
        grid.update_neighbourhood(1, 1)
        assert [[cell.neighbours for cell in row] for row in grid.cells] \
                ==  [[1, 0, 1, 0],
                     [1, 1, 1, 0],
                     [0, 0, 0, 0],
                     [1, 1, 1, 0]]
        grid.update_neighbourhood(1, 2)
        assert [[cell.neighbours for cell in row] for row in grid.cells] \
                ==  [[1, 1, 2, 1],
                     [1, 2, 1, 1],
                     [0, 1, 1, 1],
                     [1, 1, 1, 0]]

    def test_neighbourhoods(self):
        grid = Grid([[0, 1, 0, 0],
                     [0, 0, 1, 1],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]])
        grid.update_neighbourhoods()
        assert [[cell.neighbours for cell in row] for row in grid.cells] \
                ==  [[2, 1, 3, 2],
                     [2, 2, 2, 1],
                     [1, 1, 2, 2],
                     [1, 1, 1, 0]]

    def test_evolving_static_tub(self):
        cells = [[0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0],
                 [0, 1, 0, 1, 0],
                 [0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0]]
        grid = Grid(cells)
        grid.evolve()
        assert [[int(cell.isAlive) for cell in row] for row in grid.cells] \
                == cells

    def test_evolving_periodic_toad(self):
        cells =    [[0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0],
                    [0, 1, 0, 0, 1, 0],
                    [0, 1, 0, 0, 1, 0],
                    [0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0]]
        grid = Grid(cells)
        grid.evolve()
        assert [[int(cell.isAlive) for cell in row] for row in grid.cells] \
                == [[0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0],
                    [0, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0]]
        grid.evolve()
        assert [[int(cell.isAlive) for cell in row] for row in grid.cells] \
                == cells

    def test_evolving_glider(self):
        cells = [[0, 0, 1, 0, 0],
                 [1, 0, 1, 0, 0],
                 [0, 1, 1, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0]]
        grid = Grid(cells)
        for cycle in range(20):
            grid.evolve()
        assert [[int(cell.isAlive) for cell in row] for row in grid.cells] \
                == cells

    def test_stringify(self):
        grid = Grid([[0, 0, 1], [0, 1, 0]])
        assert str(grid) == "    []\n  []  "

