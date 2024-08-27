import pygame
import random

# Inicialização do pygame
pygame.init()

# Configurações do jogo
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Cria a tela do jogo
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# Definição das peças do Tetris
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 0, 0], [1, 1, 1]],
    [[0, 0, 1], [1, 1, 1]],
    [[0, 1, 0], [1, 1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]]
]

# Classe que representa o jogo
class TetrisGame:
    def __init__(self):
        self.board = [[0] * (SCREEN_WIDTH // BLOCK_SIZE) for _ in range(SCREEN_HEIGHT // BLOCK_SIZE)]
        self.current_piece = self.new_piece()
        self.game_over = False

    def new_piece(self):
        shape = random.choice(SHAPES)
        color = (random.randint(50, 200), random.randint(50, 200), random.randint(50, 200))
        piece = {
            "shape": shape,
            "color": color,
            "x": (len(self.board[0]) - len(shape[0])) // 2,
            "y": 0
        }
        return piece

    def draw_piece(self):
        piece = self.current_piece
        for y, row in enumerate(piece["shape"]):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, piece["color"], (piece["x"] * BLOCK_SIZE + x * BLOCK_SIZE, piece["y"] * BLOCK_SIZE + y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def draw_board(self):
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, WHITE, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

    def move_piece(self, dx, dy):
        piece = self.current_piece
        new_x = piece["x"] + dx
        new_y = piece["y"] + dy

        if self.is_valid_move(piece["shape"], new_x, new_y):
            piece["x"] = new_x
            piece["y"] = new_y
            return True
        return False

    def rotate_piece(self):
        piece = self.current_piece
        new_shape = list(zip(*reversed(piece["shape"])))
        if self.is_valid_move(new_shape, piece["x"], piece["y"]):
            piece["shape"] = new_shape

    def is_valid_move(self, shape, x, y):
        for y_offset, row in enumerate(shape):
            for x_offset, cell in enumerate(row):
                if cell:
                    board_x = x + x_offset
                    board_y = y + y_offset
                    if (
                        board_x < 0 or board_x >= len(self.board[0]) or
                        board_y >= len(self.board) or
                        self.board[board_y][board_x]
                    ):
                        return False
        return True

    def place_piece(self):
        piece = self.current_piece
        for y, row in enumerate(piece["shape"]):
            for x, cell in enumerate(row):
                if cell:
                    board_x = piece["x"] + x
                    board_y = piece["y"] + y
                    self.board[board_y][board_x] = piece["color"]
        self.current_piece = self.new_piece()
        if not self.is_valid_move(self.current_piece["shape"], self.current_piece["x"], self.current_piece["y"]):
            self.game_over = True

    def clear_lines(self):
        lines_to_clear = []
        for y, row in enumerate(self.board):
            if all(cell != 0 for cell in row):
                lines_to_clear.append(y)

        for y in lines_to_clear:
            del self.board[y]
            self.board.insert(0, [0] * (SCREEN_WIDTH // BLOCK_SIZE))

    def update(self):
        if self.game_over:
            return

        if not self.move_piece(0, 1):
            self.place_piece()
            self.clear_lines()

    def draw(self):
        screen.fill(BLACK)
        self.draw_piece()
        self.draw_board()
        pygame.display.update()

# Inicialização do jogo
game = TetrisGame()

# Loop principal do jogo
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.move_piece(-1, 0)
            elif event.key == pygame.K_RIGHT:
                game.move_piece(1, 0)
            elif event.key == pygame.K_DOWN:
                game.move_piece(0, 1)
            elif event.key == pygame.K_UP:
                game.rotate_piece()

    game.update()
    game.draw()
    clock.tick(2)  # Velocidade do jogo

pygame.quit()
