# -*- coding: utf-8 -*-

from gol.base import Grid
from gol.game import GameOfLife


class TestGame(object):

    def test_initialisation(self):
        game = GameOfLife()
        assert type(game.grid) == Grid
        assert  len(game.grid.cells) == 5
        assert  len(game.grid.cells[0]) == 11

    def test_evolution(self):
        game = GameOfLife("demo")
        game.evolve()
        assert [[int(cell.is_alive) for cell in row] for row in game.grid.cells] \
               == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                   [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                   [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]

