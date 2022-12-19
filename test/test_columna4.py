from FP_Superior_dual.David_Python.sudoku.src.checkSudoku import checkSudoku
incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,2]]
incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

def test_columnas():
    assert checkSudoku(incorrect) is False
def test_columnas2():
    assert checkSudoku(incorrect3) is False

