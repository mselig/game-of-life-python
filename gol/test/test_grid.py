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
        assert  not grid.cells[0][0].is_alive
        assert  not grid.cells[0][1].is_alive
        assert      grid.cells[0][2].is_alive
        grid = Grid("demo")
        assert [[int(cell.is_alive) for cell in row] for row in grid.cells] \
                == [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]

    def test_neighbourhood(self):
        grid = Grid([[0, 1, 0, 0],
                     [0, 0, 1, 1],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]])
        grid.update_neighbourhood(0, 0)
        assert [[cell.neighbours for cell in row] for row in grid.cells] \
                ==  [[2, 1, 3, 2],
                     [2, 2, 2, 1],
                     [1, 1, 2, 2],
                     [1, 1, 1, 0]]
        grid.update_neighbourhood(0, 1)
        assert [[cell.neighbours for cell in row] for row in grid.cells] \
                ==  [[3, 1, 4, 2],
                     [3, 3, 3, 1],
                     [1, 1, 2, 2],
                     [2, 2, 2, 0]]
        grid.update_neighbourhood(1, 1)
        assert [[cell.neighbours for cell in row] for row in grid.cells] \
                ==  [[3, 1, 4, 2],
                     [3, 3, 3, 1],
                     [1, 1, 2, 2],
                     [2, 2, 2, 0]]
        grid.update_neighbourhood(1, 2)
        assert [[cell.neighbours for cell in row] for row in grid.cells] \
                ==  [[3, 2, 5, 3],
                     [3, 4, 3, 2],
                     [1, 2, 3, 3],
                     [2, 2, 2, 0]]

    def test_neighbourhoods(self):
        grid = Grid([[0, 1, 0, 0],
                     [0, 0, 1, 1],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]])
        assert [[cell.neighbours for cell in row] for row in grid.cells] \
                ==  [[2, 1, 3, 2],
                     [2, 2, 2, 1],
                     [1, 1, 2, 2],
                     [1, 1, 1, 0]]
        grid.update_neighbourhoods()
        assert [[cell.neighbours for cell in row] for row in grid.cells] \
                ==  [[4, 2, 6, 4],
                     [4, 4, 4, 2],
                     [2, 2, 4, 4],
                     [2, 2, 2, 0]]

    def test_evolving_static_tub(self):
        cells = [[0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0],
                 [0, 1, 0, 1, 0],
                 [0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0]]
        grid = Grid(cells)
        grid.evolve()
        assert [[int(cell.is_alive) for cell in row] for row in grid.cells] \
                == cells

    def test_evolving_periodic_toad(self):
        cells =    [[0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0],
                    [0, 1, 0, 0, 1, 0],
                    [0, 1, 0, 0, 1, 0],
                    [0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0]]
        grid = Grid(cells)
        grid.evolve(1)
        assert [[int(cell.is_alive) for cell in row] for row in grid.cells] \
                == [[0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0],
                    [0, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0]]
        grid.evolve(1)
        assert [[int(cell.is_alive) for cell in row] for row in grid.cells] \
                == cells

    def test_evolving_glider(self):
        cells = [[0, 0, 1, 0, 0],
                 [1, 0, 1, 0, 0],
                 [0, 1, 1, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0]]
        grid = Grid(cells)
        grid.evolve(cycles=20)
        assert [[int(cell.is_alive) for cell in row] for row in grid.cells] \
                == cells

    def test_stringify(self):
        grid = Grid([[0, 0, 1], [0, 1, 0]])
        assert str(grid) == "    []\n  []  "

