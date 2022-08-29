from calendar import c
from typing import List
import pygame
from packages.constants import *
from packages.pieces import *
from packages.math_and_collisions import *


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


def check(king, pieces):
    if not king or not pieces:
        return
    for piece in pieces:
        spots = piece.show_positions(pieces)
        for spot in spots:
            if spot.collision_detection([king]):
                return piece


def checkmate(king, pieces, color):
    def no_moves():
        spots = king.show_positions(pieces)
        for spot in spots:
            s_king = King(spot.x, spot.y, color)
            if not check(s_king, pieces):
                print(s_king)
                return False
        return True

    if check(king, pieces) and no_moves():
        return True


def check_for_black_checkmate(kings, pieces):
    carry = kings
    kings = filter(lambda king: king.color == "black", kings)
    king = None
    for x_king in kings:
        king = x_king
    b_check = checkmate(king, pieces, "black")
    kings = carry
    return b_check


def check_for_white_checkmate(kings, pieces):
    carry = kings
    kings = filter(lambda king: king.color == "white", kings)
    king = None
    for x_king in kings:
        king = x_king
    w_check = checkmate(king, pieces, "white")
    kings = carry
    return w_check


def check_for_black_check(kings, pieces):
    carry = kings
    kings = filter(lambda king: king.color == "black", kings)
    king = None
    for x_king in kings:
        king = x_king
    b_check = check(king, pieces)
    kings = carry
    return b_check


def check_for_white_check(kings, pieces):
    carry = kings
    kings = filter(lambda king: king.color == "white", kings)
    king = None
    for x_king in kings:
        king = x_king
    w_check = check(king, pieces)
    kings = carry
    return w_check


def draw_black_win(window, pieces):
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
    txt = WIN_FONT.render("Black Wins!", 1, (125, 125, 125))
    window.blit(
        txt, (WIDTH / 2 - txt.get_width() / 2, HEIGHT / 2 - txt.get_height() / 2)
    )
    txt = WIN_FONT.render("Press Enter To Restart.", 1, (125, 125, 125))
    window.blit(
        txt, (WIDTH / 2 - txt.get_width() / 2, HEIGHT / 2 - txt.get_height() / 2 - 70)
    )
    pygame.display.update()


def draw_white_win(window, pieces):
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
    txt = WIN_FONT.render("White Wins!", 1, (125, 125, 125))
    window.blit(
        txt, (WIDTH / 2 - txt.get_width() / 2, HEIGHT / 2 - txt.get_height() / 2)
    )
    txt = WIN_FONT.render("Press Enter To Restart.", 1, (125, 125, 125))
    window.blit(
        txt, (WIDTH / 2 - txt.get_width() / 2, HEIGHT / 2 - txt.get_height() / 2 - 70)
    )
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    pieces = initialize_white_pieces()
    pieces += initialize_black_pieces()
    pawns, rooks, knights, bishops, kings, queens = separate_pieces(pieces)
    turn = "black"
    spots = []
    b_check = False
    w_check = False
    b_checkmate = False
    w_checkmate = False
    changed = False
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
                                    b_check = check_for_black_check(kings, pieces)
                                    w_check = check_for_white_check(kings, pieces)
                                    b_checkmate = check_for_black_checkmate(
                                        kings, pieces
                                    )
                                    w_checkmate = check_for_white_checkmate(
                                        kings, pieces
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
                                    b_check = check_for_black_check(kings, pieces)
                                    w_check = check_for_white_check(kings, pieces)
                                    b_checkmate = check_for_black_checkmate(
                                        kings, pieces
                                    )
                                    w_checkmate = check_for_white_checkmate(
                                        kings, pieces
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
                                    b_check = check_for_black_check(kings, pieces)
                                    w_check = check_for_white_check(kings, pieces)
                                    b_checkmate = check_for_black_checkmate(
                                        kings, pieces
                                    )
                                    w_checkmate = check_for_white_checkmate(
                                        kings, pieces
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
                                    b_check = check_for_black_check(kings, pieces)
                                    w_check = check_for_white_check(kings, pieces)
                                    b_checkmate = check_for_black_checkmate(
                                        kings, pieces
                                    )
                                    w_checkmate = check_for_white_checkmate(
                                        kings, pieces
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
                                    b_check = check_for_black_check(kings, pieces)
                                    w_check = check_for_white_check(kings, pieces)
                                    b_checkmate = check_for_black_checkmate(
                                        kings, pieces
                                    )
                                    w_checkmate = check_for_white_checkmate(
                                        kings, pieces
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
                                    b_check = check_for_black_check(kings, pieces)
                                    w_check = check_for_white_check(kings, pieces)
                                    b_checkmate = check_for_black_checkmate(
                                        kings, pieces
                                    )
                                    w_checkmate = check_for_white_checkmate(
                                        kings, pieces
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
                                    b_check = check_for_black_check(kings, pieces)
                                    w_check = check_for_white_check(kings, pieces)
                                    b_checkmate = check_for_black_checkmate(
                                        kings, pieces
                                    )
                                    w_checkmate = check_for_white_checkmate(
                                        kings, pieces
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
                                    b_check = check_for_black_check(kings, pieces)
                                    w_check = check_for_white_check(kings, pieces)
                                    b_checkmate = check_for_black_checkmate(
                                        kings, pieces
                                    )
                                    w_checkmate = check_for_white_checkmate(
                                        kings, pieces
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
                                    b_check = check_for_black_check(kings, pieces)
                                    w_check = check_for_white_check(kings, pieces)
                                    b_checkmate = check_for_black_checkmate(
                                        kings, pieces
                                    )
                                    w_checkmate = check_for_white_checkmate(
                                        kings, pieces
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
                                    b_check = check_for_black_check(kings, pieces)
                                    w_check = check_for_white_check(kings, pieces)
                                    b_checkmate = check_for_black_checkmate(
                                        kings, pieces
                                    )
                                    w_checkmate = check_for_white_checkmate(
                                        kings, pieces
                                    )
                                    turn = "black"
                                    spots = []
                                    moved = True

                                elif clicked_on_white_rook_spot(spot, piece, event.pos):
                                    coll_pieces = move_white_piece(
                                        piece, pieces, (spot.x, spot.y)
                                    )
                                    b_check = check_for_black_check(kings, pieces)
                                    w_check = check_for_white_check(kings, pieces)
                                    b_checkmate = check_for_black_checkmate(
                                        kings, pieces
                                    )
                                    w_checkmate = check_for_white_checkmate(
                                        kings, pieces
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
                                    b_check = check_for_black_check(kings, pieces)
                                    w_check = check_for_white_check(kings, pieces)
                                    b_checkmate = check_for_black_checkmate(
                                        kings, pieces
                                    )
                                    w_checkmate = check_for_white_checkmate(
                                        kings, pieces
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
        if w_checkmate:
            draw_white_win(WIN, pieces)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                main()
            continue
        if b_checkmate:
            draw_black_win(WIN, pieces)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                main()
            continue
        if b_check:
            changed = True
            kings[1].piece_img = pygame.transform.scale(BLACK_KING, (63, 63))
        elif w_check:
            changed = True
            kings[0].piece_img = pygame.transform.scale(WHITE_KING, (63, 63))

        moved = False
        draw_window(pieces, WIN, spots)
        if changed:
            kings[1].piece_img = pygame.transform.scale(BLACK_KING, (60, 60))
            kings[0].piece_img = pygame.transform.scale(WHITE_KING, (60, 60))
            draw_window(pieces, WIN, spots)


if __name__ == "__main__":
    main()
