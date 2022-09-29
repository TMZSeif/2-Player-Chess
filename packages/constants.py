import pygame
import os
import sys


def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


pygame.font.init()

# CONSTANTS

WIDTH, HEIGHT = 800, 600

SIZE_OF_BOARD_PIECE = (100, 75)

FPS = 90
board_url = resource_path("Assets/Chess_Board.svg")
w_pawn_url = resource_path("Assets/white_pawn.png")
w_bishop_url = resource_path("Assets/white_bishop.png")
w_king_url = resource_path("Assets/white_king.png")
w_knight_url = resource_path("Assets/white_knight.png")
w_queen_url = resource_path("Assets/white_queen.png")
w_rook_url = resource_path("Assets/white_rook.png")
b_pawn_url = resource_path("Assets/black_pawn.png")
b_bishop_url = resource_path("Assets/black_bishop.png")
b_king_url = resource_path("Assets/black_king.png")
b_knight_url = resource_path("Assets/black_knight.png")
b_queen_url = resource_path("Assets/black_queen.png")
b_rook_url = resource_path("Assets/black_rook.png")
spot_url = resource_path("Assets/spot.png")

WIN_FONT = pygame.font.SysFont("consolas", 60)
BOARD_IMG = pygame.image.load(board_url)
BOARD = pygame.transform.scale(BOARD_IMG, (WIDTH, HEIGHT))
BLACK_PAWN = pygame.image.load(b_pawn_url)
BLACK_ROOK = pygame.image.load(b_rook_url)
BLACK_QUEEN = pygame.image.load(b_queen_url)
BLACK_KING = pygame.image.load(b_king_url)
BLACK_BISHOP = pygame.image.load(b_bishop_url)
BLACK_KNIGHT = pygame.image.load(b_knight_url)
WHITE_PAWN = pygame.image.load(w_pawn_url)
WHITE_ROOK = pygame.image.load(w_rook_url)
WHITE_QUEEN = pygame.image.load(w_queen_url)
WHITE_KING = pygame.image.load(w_king_url)
WHITE_BISHOP = pygame.image.load(w_bishop_url)
WHITE_KNIGHT = pygame.image.load(w_knight_url)
SPOT = pygame.image.load(spot_url)

WIN = pygame.display.set_mode((WIDTH, HEIGHT), vsync=1)
pygame.display.set_caption("2 Player Chess")
