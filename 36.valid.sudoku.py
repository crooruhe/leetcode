class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # 0 - 2, 3 - 5, 6 - 8

        for row in board:
            rnums = set()
            for num in row:
                s = 0
                if num == '.':
                    continue

                else:
                    s = len(rnums)
                    rnums.add(num)
                    if len(rnums) == s:
                        print('False1')
                        return False
        
        for i in range(0, 9):
            cset = set()
            for row in board:
                if row[i] == '.':
                    continue
                else:
                    size = len(cset)
                    cset.add(row[i])
                    if len(cset) == size:
                        print('False2')
                        return False

        for r in range(9):
            if r % 3 == 0 or r == 0:
                fset = set()
                sset = set()
                tset = set()
            for c in range(3):
                if board[r][c] == '.':
                    continue
                else:
                    size = len(fset)
                    fset.add(board[r][c])
                    if len(fset) == size:
                        print('False3')
                        return False

            for c in range(3, 6):
                if board[r][c] == '.':
                    continue
                else:
                    size = len(sset)
                    sset.add(board[r][c])
                    if len(sset) == size:
                        print('False3')
                        return False

            for c in range(6, 9):
                if board[r][c] == '.':
                    continue
                else:
                    size = len(tset)
                    tset.add(board[r][c])
                    if len(tset) == size:
                        print('False3')
                        return False

        print(True)
        return True


if __name__ == "__main__":
    x = Solution()
    s = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    # s =[[".",".",".",".","5",".",".","1","."],
    #     [".","4",".","3",".",".",".",".","."],
    #     [".",".",".",".",".","3",".",".","1"],
    #     ["8",".",".",".",".",".",".","2","."],
    #     [".",".","2",".","7",".",".",".","."],
    #     [".","1","5",".",".",".",".",".","."],
    #     [".",".",".",".",".","2",".",".","."],
    #     [".","2",".","9",".",".",".",".","."],
    #     [".",".","4",".",".",".",".",".","."]]
    x.isValidSudoku(s)