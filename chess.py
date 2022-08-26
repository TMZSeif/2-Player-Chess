from typing import List
import pygame
from packages.constants import *
from packages.pieces import *
from packages.math_and_collisions import *


pygame.display.set_caption("2 Player Chess")


def draw_window(pieces, window, spots):
    window.blit(BOARD, (0, 0))
    for piece in pieces:
        piece.draw(window)
        pygame.draw.rect(
            window,
            (255, 0, 0),
            (
                piece.x + piece.piece_img.get_width() / 2,
                piece.y + piece.piece_img.get_height() / 2,
                10,
                10,
            ),
        )
    for spot in spots:
        window.blit(
            spot.img,
            (spot.x + spot.img.get_height() / 2, spot.y + spot.img.get_height() / 2),
        )
    pygame.display.update()


def move_black_piece(piece, coll_pieces, pos):
    if piece.color == "black":
        coll_piece = piece.move(coll_pieces, pos)
        if coll_piece:
            coll_pieces.remove(coll_piece)
            return coll_pieces
        return True


def show_black_positions(piece, coll_pieces, pos):
    if piece.color == "black" and clicked_on_piece(piece, pos):
        spots = piece.show_positions(coll_pieces)

        return spots


def show_white_positions(piece, coll_pieces, pos):
    if piece.color == "white" and clicked_on_piece(piece, pos):
        spots = piece.show_positions(coll_pieces)
        return spots


def move_white_piece(piece, coll_pieces, pos):
    if piece.color == "white":
        coll_piece = piece.move(coll_pieces, pos)
        if coll_piece:
            coll_pieces.remove(coll_piece)
            return coll_pieces
        return True


def main():
    run = True
    clock = pygame.time.Clock()
    pieces = initialize_white_pieces()
    pieces += initialize_black_pieces()
    pawns, rooks, knights, bishops, kings, queens = separate_pieces(pieces)
    turn = "black"
    spots = []
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if turn == "black":
                    for piece in pieces:
                        for spot in spots:
                            if clicked_on_piece(spot, event.pos):
                                if clicked_on_black_king_spot(spot, piece, event.pos):
                                    coll_pieces = move_black_piece(
                                        piece, pieces, (spot.x, spot.y)
                                    )
                                    if type(coll_pieces) == List:
                                        pieces = coll_pieces
                                    turn = "white"
                                    spots = []
                                    moved = True

                                if clicked_on_black_knight_spot(spot, piece, event.pos):
                                    coll_pieces = move_black_piece(
                                        piece, pieces, (spot.x, spot.y)
                                    )
                                    if type(coll_pieces) == List:
                                        pieces = coll_pieces
                                    turn = "white"
                                    spots = []
                                    moved = True

                                if clicked_on_black_queen_spot(spot, piece, event.pos):
                                    coll_pieces = move_black_piece(
                                        piece, pieces, (spot.x, spot.y)
                                    )
                                    if type(coll_pieces) == List:
                                        pieces = coll_pieces
                                    turn = "white"
                                    spots = []
                                    moved = True

                                if clicked_on_black_pawn_spot(spot, piece, event.pos):
                                    coll_pieces = move_black_piece(
                                        piece, pieces, (spot.x, spot.y)
                                    )
                                    if type(coll_pieces) == List:
                                        pieces = coll_pieces
                                    turn = "white"
                                    spots = []
                                    moved = True

                                elif clicked_on_black_rook_spot(spot, piece, event.pos):
                                    coll_pieces = move_black_piece(
                                        piece, pieces, (spot.x, spot.y)
                                    )
                                    if type(coll_pieces) == List:
                                        pieces = coll_pieces
                                    turn = "white"
                                    spots = []
                                    moved = True

                                elif clicked_on_black_bishop_spot(
                                    spot, piece, event.pos
                                ):
                                    coll_pieces = move_black_piece(
                                        piece, pieces, (spot.x, spot.y)
                                    )
                                    if type(coll_pieces) == List:
                                        pieces = coll_pieces
                                    turn = "white"
                                    spots = []
                                    moved = True

                        if moved:
                            break
                        if clicked_on_piece(
                            piece, event.pos
                        ) and not piece.collision_detection(spots):
                            spots = show_black_positions(piece, pieces, event.pos)
                            if not spots:
                                spots = []
                else:
                    for piece in pieces:
                        for spot in spots:
                            if clicked_on_piece(spot, event.pos):
                                if clicked_on_white_king_spot(spot, piece, event.pos):
                                    coll_pieces = move_white_piece(
                                        piece, pieces, (spot.x, spot.y)
                                    )
                                    if type(coll_pieces) == List:
                                        pieces = coll_pieces
                                    turn = "black"
                                    spots = []
                                    moved = True

                                if clicked_on_white_knight_spot(spot, piece, event.pos):
                                    coll_pieces = move_white_piece(
                                        piece, pieces, (spot.x, spot.y)
                                    )
                                    if type(coll_pieces) == List:
                                        pieces = coll_pieces
                                    turn = "black"
                                    spots = []
                                    moved = True

                                if clicked_on_white_queen_spot(spot, piece, event.pos):
                                    coll_pieces = move_white_piece(
                                        piece, pieces, (spot.x, spot.y)
                                    )
                                    if type(coll_pieces) == List:
                                        pieces = coll_pieces
                                    turn = "black"
                                    spots = []
                                    moved = True

                                if clicked_on_white_pawn_spot(spot, piece, event.pos):
                                    coll_pieces = move_white_piece(
                                        piece, pieces, (spot.x, spot.y)
                                    )
                                    if type(coll_pieces) == List:
                                        pieces = coll_pieces
                                    turn = "black"
                                    spots = []
                                    moved = True

                                elif clicked_on_white_rook_spot(spot, piece, event.pos):
                                    coll_pieces = move_white_piece(
                                        piece, pieces, (spot.x, spot.y)
                                    )
                                    if type(coll_pieces) == List:
                                        pieces = coll_pieces
                                    turn = "black"
                                    spots = []
                                    moved = True

                                elif clicked_on_white_bishop_spot(
                                    spot, piece, event.pos
                                ):
                                    coll_pieces = move_white_piece(
                                        piece, pieces, (spot.x, spot.y)
                                    )
                                    if type(coll_pieces) == List:
                                        pieces = coll_pieces
                                    turn = "black"
                                    spots = []
                                    moved = True
                        if moved:
                            break
                        if clicked_on_piece(piece, event.pos):
                            spots = show_white_positions(piece, pieces, event.pos)
                            if not spots:
                                spots = []

        moved = False
        draw_window(pieces, WIN, spots)


if __name__ == "__main__":
    main()
