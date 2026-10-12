board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]
current_player = 'X'
game_over = False
winner = None

def setup():
    size(600, 600)
    strokeWeight(6)
    textAlign(CENTER, CENTER)

def draw():
    background(245)
    draw_grid()
    draw_marks()
    display_status()

def draw_grid():
    stroke(80)
    strokeCap(ROUND)

    line(200, 20, 200, 580)
    line(400, 20, 400, 580)

    line(20, 200, 580, 200)
    line(20, 400, 580, 400)

def draw_marks():
    for r in range(3):
        for c in range(3):
            mark = board[r][c]
            x = c * 200 + 100
            y = r * 200 + 100
            
            if mark == 'X':
                stroke(220, 60, 60)
                offset = 45
                line(x - offset, y - offset, x + offset, y + offset)
                line(x + offset, y - offset, x - offset, y + offset)
            elif mark == 'O':
                stroke(50, 120, 220)
                noFill()
                ellipse(x, y, 110, 110)

def mousePressed():
    global current_player, game_over, winner
    

    if game_over:
        reset_game()
        return


    c = mouseX // 200
    r = mouseY // 200

    if 0 <= r < 3 and 0 <= c < 3:
        if board[r][c] == '':
            board[r][c] = current_player
            
            if check_win(current_player):
                game_over = True
                winner = current_player
            elif is_full():
                game_over = True
                winner = 'Tie'
            else:
                current_player = 'O' if current_player == 'X' else 'X'

def check_win(player):

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
            

    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
        
    return False

def is_full():
    for row in board:
        if '' in row:
            return False
    return True

def reset_game():
    global board, current_player, game_over, winner
    board = [['', '', ''] for _ in range(3)]
    current_player = 'X'
    game_over = False
    winner = None

def display_status():
    if game_over:
        fill(20, 20, 20, 210)
        noStroke()
        rect(80, 220, 440, 160, 16)
        
        fill(255)
        textSize(32)
        if winner == 'Tie':
            msg = "Draw!\nClick to Play Again"
        else:
            msg = "Player {} Wins!\nClick to Play Again".format(winner)
        text(msg, width / 2, height / 2)
        
        
        
        
