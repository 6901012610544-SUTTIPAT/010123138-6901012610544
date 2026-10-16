import random

ROWS = 10          # Number of rows
COLS = 10         # Number of columns
CELL_SIZE = 40     # Pixel width/height of each cell
NUM_MINES = 10     # Total number of hidden mines
HEADER_HEIGHT = 60 # Top HUD bar height

# Game state variables
mines = []
revealed = []
flagged = []
neighbor_counts = []
game_over = False
game_won = False
first_click = True

def settings():
    #Dynamic window size
    size(COLS * CELL_SIZE, ROWS * CELL_SIZE + HEADER_HEIGHT)

def setup():
    textAlign(CENTER, CENTER)
    reset_game()

def reset_game():
    global mines, revealed, flagged, neighbor_counts, game_over, game_won, first_click
    mines = [[False for _ in range(COLS)] for _ in range(ROWS)]
    revealed = [[False for _ in range(COLS)] for _ in range(ROWS)]
    flagged = [[False for _ in range(COLS)] for _ in range(ROWS)]
    neighbor_counts = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    game_over = False
    game_won = False
    first_click = True

def place_mines(first_r, first_c):
    all_cells = [(r, c) for r in range(ROWS) for c in range(COLS) if not (r == first_r and c == first_c)]
    
    # Ensure mines do not exceed available slots
    mine_count = min(NUM_MINES, len(all_cells))
    chosen = random.sample(all_cells, mine_count)
    for r, c in chosen:
        mines[r][c] = True

    # Precompute neighboring mine counts
    for r in range(ROWS):
        for c in range(COLS):
            if not mines[r][c]:
                count = 0
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < ROWS and 0 <= nc < COLS and mines[nr][nc]:
                            count += 1
                neighbor_counts[r][c] = count

def draw():
    background(240)
    draw_header()
    draw_board()

def draw_header():
    fill(45, 52, 54)
    noStroke()
    rect(0, 0, width, HEADER_HEIGHT)

    flags_count = sum(row.count(True) for row in flagged)
    remaining_mines = max(0, NUM_MINES - flags_count)

    # Left: Remaining flags / mines
    fill(255)
    textSize(max(13, int(HEADER_HEIGHT * 0.28)))
    textAlign(LEFT, CENTER)
    text("Mines: {}".format(remaining_mines), 16, HEADER_HEIGHT // 2)

    # Right: Grid dimensions
    textAlign(RIGHT, CENTER)
    text("{}x{}".format(ROWS, COLS), width - 16, HEADER_HEIGHT // 2)

    # Center: Game Status
    textAlign(CENTER, CENTER)
    textSize(max(14, int(HEADER_HEIGHT * 0.32)))
    if game_over:
        fill(255, 82, 82)
        text("Game Over! (Click)", width // 2, HEADER_HEIGHT // 2)
    elif game_won:
        fill(76, 175, 80)
        text("You Win! (Click)", width // 2, HEADER_HEIGHT // 2)
    else:
        fill(255)
        text("Minesweeper", width // 2, HEADER_HEIGHT // 2)

def draw_board():
    num_colors = {
        1: color(25, 118, 210),
        2: color(56, 142, 60),
        3: color(211, 47, 47),
        4: color(123, 31, 162),
        5: color(255, 143, 0),
        6: color(0, 151, 167),
        7: color(0, 0, 0),
        8: color(128, 128, 128)
    }

    for r in range(ROWS):
        for c in range(COLS):
            x = c * CELL_SIZE
            y = r * CELL_SIZE + HEADER_HEIGHT

            stroke(170)
            strokeWeight(1)

            if revealed[r][c]:
                fill(225, 228, 232)
                rect(x, y, CELL_SIZE, CELL_SIZE)

                if mines[r][c]:
                    # Proportional mine circle
                    fill(220, 53, 69)
                    noStroke()
                    ellipse(x + CELL_SIZE * 0.5, y + CELL_SIZE * 0.5, CELL_SIZE * 0.52, CELL_SIZE * 0.52)
                elif neighbor_counts[r][c] > 0:
                    # Scaled numbers
                    val = neighbor_counts[r][c]
                    fill(num_colors.get(val, color(0)))
                    textSize(int(CELL_SIZE * 0.55))
                    textAlign(CENTER, CENTER)
                    text(str(val), x + CELL_SIZE * 0.5, y + CELL_SIZE * 0.5)
            else:
                # Hidden tile
                fill(200, 205, 210)
                rect(x, y, CELL_SIZE, CELL_SIZE)

                if flagged[r][c]:
                    # Proportional flag icon
                    fill(230, 50, 50)
                    noStroke()
                    triangle(
                        x + CELL_SIZE * 0.32, y + CELL_SIZE * 0.22,
                        x + CELL_SIZE * 0.76, y + CELL_SIZE * 0.40,
                        x + CELL_SIZE * 0.32, y + CELL_SIZE * 0.58
                    )
                    stroke(60)
                    strokeWeight(max(1.5, CELL_SIZE * 0.05))
                    line(x + CELL_SIZE * 0.32, y + CELL_SIZE * 0.20, x + CELL_SIZE * 0.32, y + CELL_SIZE * 0.80)

def mousePressed():
    global game_over, game_won, first_click
    if game_over or game_won:
        reset_game()
        return

    if mouseY < HEADER_HEIGHT:
        return
    c = mouseX // CELL_SIZE
    r = (mouseY - HEADER_HEIGHT) // CELL_SIZE
    if not (0 <= r < ROWS and 0 <= c < COLS):
        return

    if mouseButton == RIGHT:
        if not revealed[r][c]:
            flagged[r][c] = not flagged[r][c]
    elif mouseButton == LEFT:
        if flagged[r][c]:
            return
        if first_click:
            place_mines(r, c)
            first_click = False
        reveal_cell(r, c)
        check_win()

def reveal_cell(r, c):
    global game_over
    if not (0 <= r < ROWS and 0 <= c < COLS):
        return
    if revealed[r][c] or flagged[r][c]:
        return

    revealed[r][c] = True

    if mines[r][c]:
        game_over = True
        reveal_all_mines()
        return

    #Recursive flood-fill for zero-neighbor cells
    if neighbor_counts[r][c] == 0:
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr != 0 or dc != 0:
                    reveal_cell(r + dr, c + dc)

def reveal_all_mines():
    for r in range(ROWS):
        for c in range(COLS):
            if mines[r][c]:
                revealed[r][c] = True

def check_win():
    global game_won
    for r in range(ROWS):
        for c in range(COLS):
            if not mines[r][c] and not revealed[r][c]:
                return
    game_won = True
