from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
# [["1","2",".", ".","3",".", ".",".","."],
#  ["4",".",".", "5",".",".", ".",".","."],
#  [".","9","8", ".",".",".", ".",".","3"],

#  ["5",".",".", ".","6",".", ".",".","4"],
#  [".",".",".", "8",".","3", ".",".","5"],
#  ["7",".",".", ".","2",".", ".",".","6"],

#  [".",".",".", ".",".",".", "2",".","."],
#  [".",".",".", "4","1","9", ".",".","8"],
#  [".",".",".", ".","8",".", ".","7","9"]]

#sets?
#hmap of sets? 

# 0 1 2 
# 3 4 5
# 6 7 8

# pass thru first row.
    # add num to row set
    # add num to col set in hmap at col[j] ( at end of iterating)
    # add num to box set in hmap at:
        # i=1, j = 4 -> i//3 = 0, j//3 = 1 --> (0, 1)
    
    # hmap: 
    # (0, 0) : 
    # (0, 1) : 
    # (0, 2) : 
    # (1, 0) : 
    # (1, 1) : 
    # (1, 2) : 
    # (2, 0) : 
    # (2, 1) : 
    # (2, 2) : 

        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(len(board)):
            print(i)
            rowNums = set()
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    # handle row
                    if board[i][j] in rowNums:
                        return False
                    else: 
                        rowNums.add(board[i][j])
                    #handle col
                    if board[i][j] in cols[j]:
                        return False
                    else: 
                        cols[j].add(board[i][j])
                    #handle box
                    r = i//3
                    c = j//3
                    tup = (r,c)
                    if board[i][j] in boxes[tup]:
                        return False
                    else:
                        boxes[tup].add(board[i][j])

        return True

