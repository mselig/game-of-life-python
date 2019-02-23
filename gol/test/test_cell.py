# -*- coding: utf-8 -*-

from gol.base import Cell


class TestCell(object):

    def test_initialisation(self):
        cell = Cell()
        assert type(cell.isAlive)    == bool
        assert type(cell.neighbours) == int
        assert cell.neighbours == 0
        cell = Cell(1)
        assert cell.isAlive == True
        assert cell.neighbours == 0
        cell = Cell(neighbours=42, isAlive=False)
        assert cell.isAlive == False
        assert cell.neighbours == 42

    def test_evolution_rule_1(self):
        """
            1. Any live cell with fewer than two live neighbours dies,
               as if caused by underpopulation.
        """
        cell = Cell(True, 0)
        cell.evolve()
        assert cell.isAlive == False
        cell = Cell(True, 1)
        cell.evolve()
        assert cell.isAlive == False

    def test_evolution_rule_2(self):
        """
            2. Any live cell with two or three live neighbours lives
               on to the next generation.
        """
        cell = Cell(True, 2)
        cell.evolve()
        assert cell.isAlive == True
        cell = Cell(True, 3)
        cell.evolve()
        assert cell.isAlive == True

    def test_evolution_rule_3(self):
        """
            3. Any live cell with more than three live neighbours dies,
               as if by overpopulation.
        """
        cell = Cell(True, 4)
        cell.evolve()
        assert cell.isAlive == False

    def test_evolution_rule_4(self):
        """
            4. Any dead cell with exactly three live neighbours comes alive,
               as if by reproduction.
        """
        cell = Cell(False, 2)
        cell.evolve()
        assert cell.isAlive == False
        cell = Cell(False, 3)
        cell.evolve()
        assert cell.isAlive == True
        cell = Cell(False, 4)
        cell.evolve()
        assert cell.isAlive == False

    def test_stringify(self):
        cell = Cell(True)
        assert str(cell) == "[]"
        cell = Cell(False)
        assert str(cell) == "  "







