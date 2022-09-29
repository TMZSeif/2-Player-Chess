import pygame
from .constants import *
from .pieces import *


def clicked_on_piece(piece, pos):
    try:

        if (
            pos[0]
            >= (piece.x + piece.piece_img.get_width() / 2) - SIZE_OF_BOARD_PIECE[0] / 2
            and pos[1]
            >= (piece.y + piece.piece_img.get_height() / 2) - SIZE_OF_BOARD_PIECE[1] / 2
        ) and (
            pos[0]
            <= (piece.x + piece.piece_img.get_width() / 2) + SIZE_OF_BOARD_PIECE[0] / 2
            and pos[1]
            <= (piece.y + piece.piece_img.get_height() / 2) + SIZE_OF_BOARD_PIECE[1] / 2
        ):

            return True
    except AttributeError:
        if (
            pos[0] >= (piece.x + piece.img.get_width() / 2) - SIZE_OF_BOARD_PIECE[0] / 2
            and pos[1]
            >= (piece.y + piece.img.get_height() / 2) - SIZE_OF_BOARD_PIECE[1] / 2
        ) and (
            pos[0] <= (piece.x + piece.img.get_width() / 2) + SIZE_OF_BOARD_PIECE[0] / 2
            and pos[1]
            <= (piece.y + piece.img.get_height() / 2) + SIZE_OF_BOARD_PIECE[1] / 2
        ):

            return True


def clicked_on_black_king_spot(spot, piece, pos):
    if (
        clicked_on_piece(spot, pos)
        and type(piece) == King
        and piece.color == "black"
        and spot in piece.spots
    ):
        return True


def clicked_on_white_king_spot(spot, piece, pos):
    if (
        clicked_on_piece(spot, pos)
        and type(piece) == King
        and piece.color == "white"
        and spot in piece.spots
    ):
        return True


def clicked_on_black_knight_spot(spot, piece, pos):
    if (
        clicked_on_piece(spot, pos)
        and type(piece) == Knight
        and piece.color == "black"
        and spot in piece.spots
    ):
        return True


def clicked_on_white_knight_spot(spot, piece, pos):
    if (
        clicked_on_piece(spot, pos)
        and type(piece) == Knight
        and piece.color == "white"
        and spot in piece.spots
    ):
        return True


def clicked_on_black_queen_spot(spot, piece, pos):
    if (
        clicked_on_piece(spot, pos)
        and type(piece) == Queen
        and piece.color == "black"
        and spot in piece.spots
    ):
        return True


def clicked_on_white_queen_spot(spot, piece, pos):
    if (
        clicked_on_piece(spot, pos)
        and type(piece) == Queen
        and piece.color == "white"
        and spot in piece.spots
    ):
        return True


def clicked_on_black_bishop_spot(spot, piece, pos):
    if (
        clicked_on_piece(spot, pos)
        and type(piece) == Bishop
        and piece.color == "black"
        and spot in piece.spots
    ):
        return True


def clicked_on_white_bishop_spot(spot, piece, pos):
    if (
        clicked_on_piece(spot, pos)
        and type(piece) == Bishop
        and piece.color == "white"
        and spot in piece.spots
    ):
        return True


def clicked_on_black_rook_spot(spot, piece, pos):
    if (
        clicked_on_piece(spot, pos)
        and type(piece) == Rook
        and piece.color == "black"
        and spot in piece.spots
    ):
        return True


def clicked_on_white_rook_spot(spot, piece, pos):
    if (
        clicked_on_piece(spot, pos)
        and type(piece) == Rook
        and piece.color == "white"
        and spot in piece.spots
    ):
        return True


def clicked_on_black_pawn_spot(spot, piece, pos):
    #
    if (
        clicked_on_piece(spot, pos)
        and type(piece) == Pawn
        and piece.color == "black"
        and spot in piece.spots
    ):
        return True


def clicked_on_white_pawn_spot(spot, piece, pos):
    if (
        clicked_on_piece(spot, pos)
        and type(piece) == Pawn
        and piece.color == "white"
        and spot in piece.spots
    ):
        return True
