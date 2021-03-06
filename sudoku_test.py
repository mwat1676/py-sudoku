import pytest
import sudoku

puzzle1 =  [0,0,0,2,6,0,7,0,1,
            6,8,0,0,7,0,0,9,0,
            1,9,0,0,0,4,5,0,0,
            8,2,0,1,0,0,0,4,0,
            0,0,4,6,0,2,9,0,0,
            0,5,0,0,0,3,0,2,8,
            0,0,9,3,0,0,0,7,4,
            0,4,0,0,5,0,0,3,6,
            7,0,3,0,1,8,0,0,0,
            ]

puzzle1_solution = [4,3,5,2,6,9,7,8,1,
                    6,8,2,5,7,1,4,9,3,
                    1,9,7,8,3,4,5,6,2,
                    8,2,6,1,9,5,3,4,7,
                    3,7,4,6,8,2,9,1,5,
                    9,5,1,7,4,3,6,2,8,
                    5,1,9,3,2,6,8,7,4,
                    2,4,8,9,5,7,1,3,6,
                    7,6,3,4,1,8,2,5,9,]

puzzle2 = [0,2,0,0,0,0,0,0,0,
0,0,0,6,0,0,0,0,3,
0,7,4,0,8,0,0,0,0,
0,0,0,0,0,3,0,0,2,
0,8,0,0,4,0,0,1,0,
6,0,0,5,0,0,0,0,0,
0,0,0,0,1,0,7,8,0,
5,0,0,0,0,9,0,0,0,
0,0,0,0,0,0,0,4,0,]

puzzle2_solution = [1,2,6,4,3,7,9,5,8,
8,9,5,6,2,1,4,7,3,
3,7,4,9,8,5,1,2,6,
4,5,7,1,9,3,8,6,2,
9,8,3,2,4,6,5,1,7,
6,1,2,5,7,8,3,9,4,
2,6,9,3,1,4,7,8,5,
5,4,8,7,6,9,2,3,1,
7,3,1,8,5,2,6,4,9,]


def test_simple_puzzle():
    g = sudoku.Grid(puzzle1)
    solutions, _ = sudoku.solve(g)
    assert len(solutions) == 1 and solutions[0] == puzzle1_solution, "Puzzle not solved correctly"

def test_hard_puzzle():
    g = sudoku.Grid(puzzle2)
    solutions, _ = sudoku.solve(g)
    assert len(solutions) == 1 and solutions[0] == puzzle2_solution, "Puzzle not solved correctly"


def test_grid_row():
    g = sudoku.Grid(puzzle2_solution)
    assert g.row(27) == [4,5,7,1,9,3,8,6,2,]

def test_grid_column():
    g = sudoku.Grid(puzzle2_solution)
    assert g.col(5) == [7,1,5,3,6,8,4,9,2,]

def test_grid_block():
    g = sudoku.Grid(puzzle2_solution)
    assert g.block(51) == [8,6,2,5,1,7,3,9,4,]
    