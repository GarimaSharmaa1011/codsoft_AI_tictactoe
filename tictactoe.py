
board = [[' ' for _ in range(3)] for _ in range(3)]


def print_board():
    for row in board:
        print("|".join(row))
        print("-" * 5)


def check_win(player):
   
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or \
           all([board[j][i] == player for j in range(3)]):
            return True


    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


def check_draw():
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))


def minimax_alpha_beta(board, depth, is_maximizing, alpha, beta):
    if check_win('X'):
        return 1 
    if check_win('O'):
        return -1  
    if check_draw():
        return 0 

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X' 
                    score = minimax_alpha_beta(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' ' 
                    best_score = max(score, best_score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break  
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'  
                    score = minimax_alpha_beta(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '  
                    best_score = min(score, best_score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break  
        return best_score

def best_move():
    best_score = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'  
                score = minimax_alpha_beta(board, 0, False, -float('inf'), float('inf'))
                board[i][j] = ' '  
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move


def player_move():
    while True:
        try:
            row, col = map(int, input("Enter your move (row col): ").split())
            if board[row][col] == ' ':
                board[row][col] = 'O'  
                break
            else:
                print("Cell is already taken!")
        except (ValueError, IndexError):
            print("Invalid move. Please enter row and col between 0 and 2.")

def play_game():
    while True:
        print_board()
        player_move()

        if check_win('O'):
            print_board()
            print("You win!")
            break
        elif check_draw():
            print_board()
            print("It's a draw!")
            break

        print("AI is making a move...")
        i, j = best_move()
        board[i][j] = 'X'  

        if check_win('X'):
            print_board()
            print("AI wins!")
            break
        elif check_draw():
            print_board()
            print("It's a draw!")
            break

# Start the game
if __name__ == "__main__":
    play_game()
