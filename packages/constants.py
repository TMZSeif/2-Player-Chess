import pygame
import os

pygame.font.init()

# CONSTANTS

WIDTH, HEIGHT = 800, 600

SIZE_OF_BOARD_PIECE = (100, 75)

FPS = 90

WIN_FONT = pygame.font.SysFont("consolas", 60)
BOARD_IMG = pygame.image.load(os.path.join("Assets", "Chess_Board.svg"))
BOARD = pygame.transform.scale(BOARD_IMG, (WIDTH, HEIGHT))
BLACK_PAWN = pygame.image.load(os.path.join("Assets", "black_pawn.png"))
BLACK_ROOK = pygame.image.load(os.path.join("Assets", "black_rook.png"))
BLACK_QUEEN = pygame.image.load(os.path.join("Assets", "black_queen.png"))
BLACK_KING = pygame.image.load(os.path.join("Assets", "black_king.png"))
BLACK_BISHOP = pygame.image.load(os.path.join("Assets", "black_bishop.png"))
BLACK_KNIGHT = pygame.image.load(os.path.join("Assets", "black_knight.png"))
WHITE_PAWN = pygame.image.load(os.path.join("Assets", "white_pawn.png"))
WHITE_ROOK = pygame.image.load(os.path.join("Assets", "white_rook.png"))
WHITE_QUEEN = pygame.image.load(os.path.join("Assets", "white_queen.png"))
WHITE_KING = pygame.image.load(os.path.join("Assets", "white_king.png"))
WHITE_BISHOP = pygame.image.load(os.path.join("Assets", "white_bishop.png"))
WHITE_KNIGHT = pygame.image.load(os.path.join("Assets", "white_knight.png"))
SPOT = pygame.image.load(os.path.join("Assets", "spot.png"))

WIN = pygame.display.set_mode((WIDTH, HEIGHT), vsync=1)
pygame.display.set_caption("2 Player Chess")
