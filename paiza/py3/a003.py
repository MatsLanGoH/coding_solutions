# coding: utf-8
# 自分の得意な言語で
# A003: 盤面ゲーム

#
# 補助メソッド
#


# 空盤面を作る
def initializeBoard():
    board = []
    for i in range(0, 8):
        board.append([])
        for j in range(0, 8):
            board[i].append(' ')
    return board


# 盤面に存在する位置か確認する
def isOnGrid(grid, x, y):
    if (0 <= x < len(grid) and 0 <= y < len(grid)):
        return True
    return False


# 盤面に石を置く（置き換える）
def addTileToGrid(grid, x, y, val):
    # NOTE: Without the condition, lines will wrap due to slicing!
    if (isOnGrid(grid, x, y)):
        grid[x][y] = val


# 盤面に置かれている石を数える
def countStones(board):
    blacks = 0
    whites = 0
    for row in board:
        blacks += row.count('B')
        whites += row.count('W')
    return(whites, blacks)


# 盤面を画面に出力　（DEBUG用）
def printBoard(board):
    for row in board:
        print(row)


#
# 本題
#

# 盤面の初期化
board = initializeBoard()
initialState = {(3, 3): 'W', (3, 4): 'B', (4, 3): 'B', (4, 4): 'W'}  # 中央石を置く
for k, v in initialState.items():
    addTileToGrid(board, k[0], k[1], v)

# 方向の定義
directions = [[0, 1], [0, -1],  # y-axis
              [1, 0], [-1, 0],  # x-axis
              [1, 1], [-1, -1],  # llur-axis
              [-1, 1], [1, -1]]  # ullr-axis


# 入力処理
num_moves = int(input())

try:
    while True:
        move = input().split()
        color = move[0]
        movX, movY = [int(i)-1 for i in move[1:]]

        addTileToGrid(board, movX, movY, color)  # 石を置く

        flips = []  # ひっくり返すx/yを入れる

        for d in directions:  # 全方面にひっくり返す対象を確認する
            curFlips = []
            curX, curY = movX, movY
            curX += d[0]
            curY += d[1]

            while True:
                if (isOnGrid(board, curX, curY)):
                    # 次が空いている場合、ひっくり返さない
                    if (" " == board[curX][curY]):
                        break
                    # 次が違う色の場合、ひっくり返す対象になる可能性あり
                    elif (color != board[curX][curY]):
                        curFlips.append((curX, curY))
                    # 次が同じ色の場合、間の意思すべてひっくり返し確定
                    elif (color == board[curX][curY]):
                        for f in curFlips:
                            flips.append(f)
                        break

                    curX += d[0]
                    curY += d[1]
                else:
                    # 枠外でた場合、ひっくり返さない
                    # for f in curFlips:
                        # flips.append(f)
                    break

        # ひっくり返す候補に入れたもの、ひっくり返す。
        for f in flips:
            addTileToGrid(board, f[0], f[1], color)

except EOFError:
    pass

# 結果出力
whites, blacks = countStones(board)

if (blacks > whites):
    result = "The black won!"
elif (whites > blacks):
    result = "The white won!"
else:
    result = "Draw!"
winner = "black" if (blacks > whites) else "white"
print("{:02d}-{:02d} {}".format(blacks, whites, result))
