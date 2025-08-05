def initialize_board():
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    return board

def print_board(board):
    for row in board:
        print(row)
    print()

def is_winner(board, player):
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
    for j in range(3):
        if board[0][j] == player and board[1][j] == player and board[2][j] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def is_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True

def get_empty_cells(board):
    empty = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                empty.append((i, j))
    return empty

def check_rows(board, player):
    for i in range(3):
        row = board[i]
        if row.count(player) == 2 and row.count(' ') == 1:
            return i, row.index(' ')
    return None

def check_columns(board, player):
    for j in range(3):
        col = [board[i][j] for i in range(3)]
        if col.count(player) == 2 and col.count(' ') == 1:
            return col.index(' '), j
    return None

def check_diagonals(board, player):
    diag1 = [board[i][i] for i in range(3)]
    if diag1.count(player) == 2 and diag1.count(' ') == 1:
        idx = diag1.index(' ')
        return idx, idx
    diag2 = [board[i][2 - i] for i in range(3)]
    if diag2.count(player) == 2 and diag2.count(' ') == 1:
        idx = diag2.index(' ')
        return idx, 2 - idx
    return None

# this moves says that if player takes moves at center and right-down corner then ai blocks his move by putting 0 at 2,0
def check_move1(board, player):
    
    if board[1][1] == 'X' and board[2][2] == 'X':
        if board[2][0] == ' ':
            return 2, 0  
    
    if board[0][1] == player and board[2][2] == player:
        if board[2][0] == ' ':
            return 2, 0
    return None


#def check_move2(board, player):
    
 #   if board[1][0] == 'X' or board[0][1] == 'X' or board[0][2] == 'X' or board[2][0] == 'X':
  #      if board[1][1] == ' ':
   #         return 1, 1
    #return None



def ai_move(board):
    empty_cells = get_empty_cells(board)
    if empty_cells:
        move = check_rows(board, 'O') or check_columns(board, 'O') or check_diagonals(board, 'O')
        if not move:
            move = check_rows(board, 'X') or check_columns(board, 'X') or check_diagonals(board, 'X')
        if not move:
            special = check_move1(board, 'O')
            if special:
                row, col = special
                board[row][col] = 'O'
                return
           # special1 = check_move2(board, 'O')
            #if special1:
             #   row, col = special1
              #  board[row][col] = 'O'
               # return
        if not move:
            move = empty_cells[0]
        row, col = move
        board[row][col] = 'O'


#center response to corner start
def respond_to_corner_start(board, move_count):
    corners = [(0, 0), (0, 2), (2, 0), (2, 2), (1, 0), (0, 1), (1, 2), (2, 1)]
    if move_count == 1:
        for corner in corners:
            if board[corner[0]][corner[1]] == 'X':
                if board[1][1] == ' ':
                    board[1][1] = 'O'
                    return True
    return False

def main():
    board = initialize_board()
    move_count = 0
    print("Welcome to Tic-Tac-Toe! You are X. AI is O.")
    while True:
        print_board(board)
        move = input("Enter your move as row and column (0 0 to 2 2): ")
        i, j = move.strip().split()
        i = int(i)
        j = int(j)
        if board[i][j] != ' ':
            print("Cell already taken. Try again.")
            continue
        board[i][j] = 'X'
        move_count += 1

        if is_winner(board, 'X'):
            print_board(board)
            print("You win!")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        if respond_to_corner_start(board, move_count):
            continue

        ai_move(board)
        if is_winner(board, 'O'):
            print_board(board)
            print("AI wins!")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
