
import collections


def isValidSudoku( board):
    cols = collections.defaultdict(set) # making a hashset for rows
    rows = collections.defaultdict(set)# making a hashset for cols
    squares = collections.defaultdict(set)  # key = (r /3, c /3) for calculating whether the numbers repeat inside the 3x3 square

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if (
                board[r][c] in rows[r]
                or board[r][c] in cols[c]
                or board[r][c] in squares[(r // 3, c // 3)]
            ):
                return False
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])

    return True

'''
Algorithm

1.declare hashmap for rows cols and square with row_no, col_no, and (row //3, col//3) as the keys
2. check for the conditions where the sudoku is not valid
    if the number repeats in that certain row
    if the number repeats in that certain col
    if the number repeats in that certain square
        return false

    here board[r][c] is the number and in the dict initally it is empty
    if the number is found inside the value set of row,col or square
    the sudoku is invalid and returns false

    else the number is added to the hashmap with the certain keys 

3.if not then return true



'''