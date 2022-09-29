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


def show_black_positions(piece, coll_pieces, pos, king):
    if piece.color == "black" and clicked_on_piece(piece, pos):
        spots = piece.show_positions(coll_pieces)
        c_spots = spots[:]
        piece_is_king_piece = piece == king
        for spot in c_spots:
            p_x, p_y = piece.x, piece.y
            piece.x, piece.y = spot.x, spot.y
            if check_for_black_check([king], coll_pieces):
                if not piece_is_king_piece:
                    attack_piece = check_for_black_check([king], coll_pieces)
                else:
                    attack_piece = check_for_black_check([piece], coll_pieces)
                a_spots = attack_piece.show_positions(coll_pieces)
                if piece_is_king_piece:
                    print(piece.x, piece.y)
                    print(attack_piece.x, attack_piece.y)
                    print(attack_piece)
                if piece.x == attack_piece.x and piece.y == attack_piece.y:
                    piece.x, piece.y = p_x, p_y
                    continue
                try:
                    # if piece_is_king_piece:
                    # print(spot.x, spot.y)
                    spots.remove(spot)
                except ValueError:
                    piece.x, piece.y = p_x, p_y
                    continue
            piece.x, piece.y = p_x, p_y
        piece.spots = spots
        return spots


def show_white_positions(piece, coll_pieces, pos, king):
    if piece.color == "white" and clicked_on_piece(piece, pos):
        spots = piece.show_positions(coll_pieces)
        c_spots = spots[:]
        for spot in c_spots:
            p_x, p_y = piece.x, piece.y
            piece.x, piece.y = spot.x, spot.y
            if check_for_white_check([king], coll_pieces):
                attack_piece = check_for_white_check([king], coll_pieces)
                a_spots = attack_piece.show_positions(coll_pieces)
                for a_spot in a_spots:
                    if piece.x != a_spot.x and piece.y != a_spot.y:
                        try:
                            spots.remove(spot)
                        except ValueError:
                            break
            piece.x, piece.y = p_x, p_y
        piece.spots = spots
        return spots


def move_white_piece(piece, coll_pieces, pos):
    if piece.color == "white":
        coll_piece = piece.move(coll_pieces, pos)
        if coll_piece:
            coll_pieces.remove(coll_piece)
            return coll_pieces
        return True


def check(king, pieces, w_pieces):
    if not king or not pieces:
        return
    for piece in w_pieces:
        spots = piece.show_positions(pieces)
        for spot in spots:
            if spot.collision_detection([king]):
                return piece


def checkmate(king, pieces, w_pieces, color):
    if not check(king, pieces, w_pieces):
        return False

    def no_moves():
        spots = king.show_positions(pieces)
        k_x, k_y = king.x, king.y
        for spot in spots:
            king.x, king.y = spot.x, spot.y
            if not check(king, pieces, w_pieces):
                print(king)
                king.x, king.y = k_x, k_y
                return False
        king.x, king.y = k_x, k_y
        return True

    def can_be_blocked():
        check_piece = check(king, pieces, w_pieces)
        check_spots = check_piece.show_positions(pieces)
        for piece in pieces:
            if piece is check_piece:
                continue
            spots = piece.show_positions(pieces)
            for check_spot in check_spots:
                for spot in spots:
                    if spot.x == check_spot.x and spot.y == check_spot.y:
                        p_x, p_y = piece.x, piece.y
                        piece.x, piece.y = spot.x, spot.y
                        if not check(king, pieces, w_pieces):
                            piece.x, piece.y = p_x, p_y
                            return True
                        piece.x, piece.y = p_x, p_y

    print(check(king, pieces, w_pieces), no_moves(), can_be_blocked())
    if check(king, pieces, w_pieces) and no_moves() and not can_be_blocked():
        return True


def check_for_black_checkmate(kings, pieces):
    carry = kings
    carry_p = pieces
    kings = filter(lambda king: king.color == "black", kings)
    king = None
    pieces = filter(lambda piece: piece.color == "white", pieces)
    for x_king in kings:
        king = x_king
    pieces = list(pieces)
    b_check = checkmate(king, carry_p, pieces, "black")
    kings = carry
    pieces = carry_p
    return b_check


def check_for_white_checkmate(kings, pieces):
    carry = kings
    carry_p = pieces
    kings = filter(lambda king: king.color == "white", kings)
    king = None
    pieces = filter(lambda piece: piece.color == "black", pieces)
    for x_king in kings:
        king = x_king
    pieces = list(pieces)
    w_check = checkmate(king, carry_p, pieces, "white")
    kings = carry
    pieces = carry_p
    return w_check


def check_for_black_check(kings, pieces):
    carry = kings
    carry_p = pieces
    kings = filter(lambda king: king.color == "black", kings)
    king = None
    pieces = filter(lambda piece: piece.color == "white", pieces)
    for x_king in kings:
        king = x_king
    pieces = list(pieces)
    b_check = check(king, carry_p, pieces)
    kings = carry
    pieces = carry_p
    return b_check


def check_for_white_check(kings, pieces):
    carry = kings
    carry_p = pieces
    kings = filter(lambda king: king.color == "white", kings)
    king = None
    pieces = filter(lambda piece: piece.color == "black", pieces)
    for x_king in kings:
        king = x_king
    pieces = list(pieces)
    w_check = check(king, carry_p, pieces)
    kings = carry
    pieces = carry_p
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
    txt = WIN_FONT.render("White Wins!", 1, (125, 125, 125))
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
    txt = WIN_FONT.render("Black Wins!", 1, (125, 125, 125))
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
                            spots = show_black_positions(
                                piece, pieces, event.pos, kings[1]
                            )
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
                            spots = show_white_positions(
                                piece, pieces, event.pos, kings[0]
                            )
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
