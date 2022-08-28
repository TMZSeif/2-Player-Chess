from .constants import *


# CLASSES


class Piece:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.piece_img = None
        self.first_turn = True
        self.spots = []

    def collision_detection(self, pieces):
        for piece in pieces:
            try:
                if (
                    self.piece_img.get_rect(x=self.x, y=self.y).colliderect(
                        piece.piece_img.get_rect(x=piece.x, y=piece.y)
                    )
                    and piece is not self
                ):
                    return piece
            except AttributeError:
                if (
                    self.piece_img.get_rect(x=self.x, y=self.y).colliderect(
                        piece.img.get_rect(x=piece.x, y=piece.y)
                    )
                    and piece is not self
                ):
                    return piece
        return False

    def draw(self, window):
        window.blit(self.piece_img, (self.x, self.y))


class Pawn(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        if color == "black":
            self.piece_img = BLACK_PAWN
        else:
            self.piece_img = WHITE_PAWN

    def move(self, pieces, spot_pos):
        if self.color == "black":
            self.y += spot_pos[1] - self.y
            self.x += spot_pos[0] - self.x
            if self.collision_detection(pieces):
                piece = self.collision_detection(pieces)
                if self.first_turn:
                    self.first_turn = False
                return piece
            if self.first_turn:
                self.first_turn = False

        elif self.color == "white":
            self.y -= self.y - spot_pos[1]
            self.x += spot_pos[0] - self.x
            if self.collision_detection(pieces):
                piece = self.collision_detection(pieces)
                if self.first_turn:
                    self.first_turn = False
                return piece
            if self.first_turn:
                self.first_turn = False

    def show_positions(self, pieces):
        self.spots = []
        if self.first_turn and self.color == "black":
            self.spots.append(Spot(self.x, self.y + SIZE_OF_BOARD_PIECE[1]))
            self.spots.append(Spot(self.x, self.y + SIZE_OF_BOARD_PIECE[1] * 2))
            self.spots.append(
                Spot(self.x + SIZE_OF_BOARD_PIECE[0], self.y + SIZE_OF_BOARD_PIECE[1])
            )
            self.spots.append(
                Spot(self.x - SIZE_OF_BOARD_PIECE[0], self.y + SIZE_OF_BOARD_PIECE[1])
            )
            for spot in self.spots[-2:]:
                if not spot.collision_detection(pieces):
                    self.spots.remove(spot)
                elif spot.collision_detection(pieces).color == "black":
                    self.spots.remove(spot)
            for spot in self.spots:
                if spot.collision_detection(pieces):
                    if spot is self.spots[0]:
                        self.spots.remove(spot)
                        self.spots.remove(self.spots[0])
                    else:
                        self.spots.remove(spot)

        elif self.color == "black":
            self.spots.append(Spot(self.x, self.y + SIZE_OF_BOARD_PIECE[1]))
            self.spots.append(
                Spot(self.x + SIZE_OF_BOARD_PIECE[0], self.y + SIZE_OF_BOARD_PIECE[1])
            )
            self.spots.append(
                Spot(self.x - SIZE_OF_BOARD_PIECE[0], self.y + SIZE_OF_BOARD_PIECE[1])
            )
            for spot in self.spots[-2:]:
                if not spot.collision_detection(pieces):
                    self.spots.remove(spot)
                elif spot.collision_detection(pieces).color == "black":
                    self.spots.remove(spot)
            for spot in self.spots:
                if spot.collision_detection(pieces) and spot is self.spots[0]:
                    self.spots.remove(spot)
        elif self.first_turn and self.color == "white":
            self.spots.append(Spot(self.x, self.y - SIZE_OF_BOARD_PIECE[1]))
            self.spots.append(Spot(self.x, self.y - SIZE_OF_BOARD_PIECE[1] * 2))
            self.spots.append(
                Spot(self.x + SIZE_OF_BOARD_PIECE[0], self.y - SIZE_OF_BOARD_PIECE[1])
            )
            self.spots.append(
                Spot(self.x - SIZE_OF_BOARD_PIECE[0], self.y - SIZE_OF_BOARD_PIECE[1])
            )
            for spot in self.spots[-2:]:
                if not spot.collision_detection(pieces):
                    self.spots.remove(spot)
                elif spot.collision_detection(pieces).color == "white":
                    self.spots.remove(spot)
            for spot in self.spots:
                if spot.collision_detection(pieces):
                    if spot is self.spots[0]:
                        self.spots.remove(spot)
                        self.spots.remove(self.spots[0])
                    else:
                        self.spots.remove(spot)

        elif self.color == "white":
            self.spots.append(Spot(self.x, self.y - SIZE_OF_BOARD_PIECE[1]))
            self.spots.append(
                Spot(self.x + SIZE_OF_BOARD_PIECE[0], self.y - SIZE_OF_BOARD_PIECE[1])
            )
            self.spots.append(
                Spot(self.x - SIZE_OF_BOARD_PIECE[0], self.y - SIZE_OF_BOARD_PIECE[1])
            )
            for spot in self.spots[-2:]:
                if not spot.collision_detection(pieces):
                    self.spots.remove(spot)
                elif spot.collision_detection(pieces).color == "white":
                    self.spots.remove(spot)
            for spot in self.spots:
                if spot.collision_detection(pieces) and spot is self.spots[0]:
                    self.spots.remove(spot)
        return self.spots


class Bishop(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        if color == "black":
            self.piece_img = BLACK_BISHOP
        else:
            self.piece_img = WHITE_BISHOP

    def move(self, pieces, spot_pos):

        if self.color == "black":
            self.y += spot_pos[1] - self.y
            self.x += spot_pos[0] - self.x
            if self.collision_detection(pieces):
                piece = self.collision_detection(pieces)
                return piece
            if self.first_turn:
                self.first_turn = False

        elif self.color == "white":
            self.y -= self.y - spot_pos[1]
            self.x -= self.x - spot_pos[0]
            if self.collision_detection(pieces):
                piece = self.collision_detection(pieces)
                return piece
            if self.first_turn:
                self.first_turn = False

    def add_spots_black(self, pieces):
        run = True
        line_num = 1
        dr_spots = []
        while run:
            dr_spots.append(
                Spot(
                    self.x + SIZE_OF_BOARD_PIECE[0] * line_num,
                    self.y + SIZE_OF_BOARD_PIECE[1] * line_num,
                )
            )
            for spot in dr_spots:
                try:
                    if (
                        spot.y > HEIGHT
                        or spot.collision_detection(pieces).color == "black"
                    ):
                        dr_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False

                except AttributeError:
                    if spot.collision_detection(pieces):
                        print("down collision")
                        run = False
            line_num += 1
        run = True
        line_num = 1
        ul_spots = []
        while run:
            ul_spots.append(
                Spot(
                    self.x - SIZE_OF_BOARD_PIECE[0] * line_num,
                    self.y - SIZE_OF_BOARD_PIECE[1] * line_num,
                )
            )
            for spot in ul_spots:
                try:
                    if spot.y < 0 or spot.collision_detection(pieces).color == "black":
                        ul_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False

                except AttributeError:
                    if spot.collision_detection(pieces):
                        print("up collision")
                        run = False
            line_num += 1
        run = True
        line_num = 1
        ur_spots = []
        while run:
            ur_spots.append(
                Spot(
                    self.x + SIZE_OF_BOARD_PIECE[0] * line_num,
                    self.y - SIZE_OF_BOARD_PIECE[1] * line_num,
                )
            )
            for spot in ur_spots:
                try:
                    if (
                        spot.x > WIDTH
                        or spot.collision_detection(pieces).color == "black"
                    ):
                        ur_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False

                except AttributeError:
                    if spot.collision_detection(pieces):
                        print("right collision")
                        run = False
            line_num += 1
        run = True
        line_num = 1
        dl_spots = []
        while run:
            dl_spots.append(
                Spot(
                    self.x - SIZE_OF_BOARD_PIECE[0] * line_num,
                    self.y + SIZE_OF_BOARD_PIECE[1] * line_num,
                )
            )
            for spot in dl_spots:
                try:
                    if spot.x < 0 or spot.collision_detection(pieces).color == "black":
                        dl_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False
                except AttributeError:
                    if spot.collision_detection(pieces):
                        run = False
            line_num += 1
        self.spots = ul_spots + dr_spots + ur_spots + dl_spots

    def add_spots_white(self, pieces):
        run = True
        line_num = 1
        dr_spots = []
        while run:
            dr_spots.append(
                Spot(
                    self.x + SIZE_OF_BOARD_PIECE[0] * line_num,
                    self.y + SIZE_OF_BOARD_PIECE[1] * line_num,
                )
            )
            for spot in dr_spots:
                try:
                    if (
                        spot.y > HEIGHT
                        or spot.collision_detection(pieces).color == "white"
                    ):
                        dr_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False

                except AttributeError:
                    if spot.collision_detection(pieces):
                        print("down collision")
                        run = False
            line_num += 1
        run = True
        line_num = 1
        ul_spots = []
        while run:
            ul_spots.append(
                Spot(
                    self.x - SIZE_OF_BOARD_PIECE[0] * line_num,
                    self.y - SIZE_OF_BOARD_PIECE[1] * line_num,
                )
            )
            for spot in ul_spots:
                try:
                    if spot.y < 0 or spot.collision_detection(pieces).color == "white":
                        ul_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False

                except AttributeError:
                    if spot.collision_detection(pieces):
                        print("up collision")
                        run = False
            line_num += 1
        run = True
        line_num = 1
        ur_spots = []
        while run:
            ur_spots.append(
                Spot(
                    self.x + SIZE_OF_BOARD_PIECE[0] * line_num,
                    self.y - SIZE_OF_BOARD_PIECE[1] * line_num,
                )
            )
            for spot in ur_spots:
                try:
                    if (
                        spot.x > WIDTH
                        or spot.collision_detection(pieces).color == "white"
                    ):
                        ur_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False

                except AttributeError:
                    if spot.collision_detection(pieces):
                        print("right collision")
                        run = False
            line_num += 1
        run = True
        line_num = 1
        dl_spots = []
        while run:
            dl_spots.append(
                Spot(
                    self.x - SIZE_OF_BOARD_PIECE[0] * line_num,
                    self.y + SIZE_OF_BOARD_PIECE[1] * line_num,
                )
            )
            for spot in dl_spots:
                try:
                    if spot.x < 0 or spot.collision_detection(pieces).color == "white":
                        dl_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False
                except AttributeError:
                    if spot.collision_detection(pieces):
                        run = False
            line_num += 1
        self.spots = ul_spots + dr_spots + ur_spots + dl_spots

    def show_positions(self, pieces):
        self.spots = []
        if self.color == "black":
            self.add_spots_black(pieces)

        elif self.color == "white":
            self.add_spots_white(pieces)
        return self.spots


class Knight(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        if color == "black":
            self.piece_img = BLACK_KNIGHT
        else:
            self.piece_img = WHITE_KNIGHT

    def move(self, pieces, spot_pos):
        if self.color == "black":
            self.y += spot_pos[1] - self.y
            self.x += spot_pos[0] - self.x
            if self.collision_detection(pieces):
                piece = self.collision_detection(pieces)
                if self.first_turn:
                    self.first_turn = False
                return piece
            if self.first_turn:
                self.first_turn = False

        elif self.color == "white":
            self.y -= self.y - spot_pos[1]
            self.x += spot_pos[0] - self.x
            if self.collision_detection(pieces):
                piece = self.collision_detection(pieces)
                if self.first_turn:
                    self.first_turn = False
                return piece
            if self.first_turn:
                self.first_turn = False

    def show_positions(self, pieces):
        self.spots = []
        spots = []

        if self.color == "black":
            spots.append(
                Spot(
                    self.x + SIZE_OF_BOARD_PIECE[0], self.y + SIZE_OF_BOARD_PIECE[1] * 2
                )
            )
            spots.append(
                Spot(
                    self.x - SIZE_OF_BOARD_PIECE[0], self.y + SIZE_OF_BOARD_PIECE[1] * 2
                )
            )
            spots.append(
                Spot(
                    self.x - SIZE_OF_BOARD_PIECE[0] * 2, self.y + SIZE_OF_BOARD_PIECE[1]
                )
            )
            spots.append(
                Spot(
                    self.x + SIZE_OF_BOARD_PIECE[0] * 2, self.y + SIZE_OF_BOARD_PIECE[1]
                )
            )
            spots.append(
                Spot(
                    self.x + SIZE_OF_BOARD_PIECE[0], self.y - SIZE_OF_BOARD_PIECE[1] * 2
                )
            )
            spots.append(
                Spot(
                    self.x - SIZE_OF_BOARD_PIECE[0], self.y - SIZE_OF_BOARD_PIECE[1] * 2
                )
            )
            spots.append(
                Spot(
                    self.x - SIZE_OF_BOARD_PIECE[0] * 2, self.y - SIZE_OF_BOARD_PIECE[1]
                )
            )
            spots.append(
                Spot(
                    self.x + SIZE_OF_BOARD_PIECE[0] * 2, self.y - SIZE_OF_BOARD_PIECE[1]
                )
            )
            self.spots = spots[:]
            for spot in spots:
                if spot.x <= 0 or spot.x >= WIDTH or spot.y <= 0 or spot.y >= HEIGHT:
                    self.spots.remove(spot)
                if not spot.collision_detection(pieces):
                    continue
                if spot.collision_detection(pieces).color == "black":
                    self.spots.remove(spot)

        elif self.color == "white":
            spots.append(
                Spot(
                    self.x + SIZE_OF_BOARD_PIECE[0], self.y + SIZE_OF_BOARD_PIECE[1] * 2
                )
            )
            spots.append(
                Spot(
                    self.x - SIZE_OF_BOARD_PIECE[0], self.y + SIZE_OF_BOARD_PIECE[1] * 2
                )
            )
            spots.append(
                Spot(
                    self.x - SIZE_OF_BOARD_PIECE[0] * 2, self.y + SIZE_OF_BOARD_PIECE[1]
                )
            )
            spots.append(
                Spot(
                    self.x + SIZE_OF_BOARD_PIECE[0] * 2, self.y + SIZE_OF_BOARD_PIECE[1]
                )
            )
            spots.append(
                Spot(
                    self.x + SIZE_OF_BOARD_PIECE[0], self.y - SIZE_OF_BOARD_PIECE[1] * 2
                )
            )
            spots.append(
                Spot(
                    self.x - SIZE_OF_BOARD_PIECE[0], self.y - SIZE_OF_BOARD_PIECE[1] * 2
                )
            )
            spots.append(
                Spot(
                    self.x - SIZE_OF_BOARD_PIECE[0] * 2, self.y - SIZE_OF_BOARD_PIECE[1]
                )
            )
            spots.append(
                Spot(
                    self.x + SIZE_OF_BOARD_PIECE[0] * 2, self.y - SIZE_OF_BOARD_PIECE[1]
                )
            )

            self.spots = spots[:]
            for spot in spots:
                if spot.x <= 0 or spot.x >= WIDTH or spot.y <= 0 or spot.y >= HEIGHT:
                    self.spots.remove(spot)
                if not spot.collision_detection(pieces):
                    continue
                if spot.collision_detection(pieces).color == "white":
                    self.spots.remove(spot)

        return self.spots


class Bishop(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        if color == "black":
            self.piece_img = BLACK_BISHOP
        else:
            self.piece_img = WHITE_BISHOP

    def move(self, pieces, spot_pos):
        if self.color == "black":
            self.y += spot_pos[1] - self.y
            self.x += spot_pos[0] - self.x
            if self.collision_detection(pieces):
                piece = self.collision_detection(pieces)
                return piece
            if self.first_turn:
                self.first_turn = False

        elif self.color == "white":
            self.y -= self.y - spot_pos[1]
            self.x -= self.x - spot_pos[0]
            if self.collision_detection(pieces):
                piece = self.collision_detection(pieces)
                return piece
            if self.first_turn:
                self.first_turn = False

    def add_spots_white(self, pieces):
        run = True
        line_num = 1
        dr_spots = []
        while run:
            dr_spots.append(
                Spot(
                    self.x + SIZE_OF_BOARD_PIECE[0] * line_num,
                    self.y + SIZE_OF_BOARD_PIECE[1] * line_num,
                )
            )
            for spot in dr_spots:
                try:
                    if (
                        spot.y > HEIGHT
                        or spot.x > WIDTH
                        or spot.collision_detection(pieces).color == "white"
                    ):
                        dr_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False
                except AttributeError:
                    if spot.collision_detection(pieces):
                        run = False
            line_num += 1
        run = True
        line_num = 1
        ur_spots = []
        while run:
            ur_spots.append(
                Spot(
                    self.x + SIZE_OF_BOARD_PIECE[0] * line_num,
                    self.y - SIZE_OF_BOARD_PIECE[1] * line_num,
                )
            )
            for spot in ur_spots:
                try:
                    if (
                        spot.y < 0
                        or spot.x > WIDTH
                        or spot.collision_detection(pieces).color == "white"
                    ):
                        ur_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False
                except AttributeError:
                    if spot.collision_detection(pieces):
                        run = False
            line_num += 1
        run = True
        line_num = 1
        dl_spots = []
        while run:
            dl_spots.append(
                Spot(
                    self.x - SIZE_OF_BOARD_PIECE[0] * line_num,
                    self.y + SIZE_OF_BOARD_PIECE[1] * line_num,
                )
            )
            for spot in dl_spots:
                try:
                    if (
                        spot.x > WIDTH
                        or spot.y > HEIGHT
                        or spot.collision_detection(pieces).color == "white"
                    ):
                        dl_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False
                except AttributeError:
                    if spot.collision_detection(pieces):
                        run = False
            line_num += 1
        run = True
        line_num = 1
        ul_spots = []
        while run:
            ul_spots.append(
                Spot(
                    self.x - SIZE_OF_BOARD_PIECE[0] * line_num,
                    self.y - SIZE_OF_BOARD_PIECE[1] * line_num,
                )
            )
            for spot in ul_spots:
                try:
                    if (
                        spot.x < 0
                        or spot.y < 0
                        or spot.collision_detection(pieces).color == "white"
                    ):
                        ul_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False
                except AttributeError:
                    if spot.collision_detection(pieces):
                        run = False
            line_num += 1
        self.spots = ul_spots + dl_spots + ur_spots + dr_spots

    def add_spots_black(self, pieces):
        run = True
        line_num = 1
        dr_spots = []
        while run:
            dr_spots.append(
                Spot(
                    self.x + SIZE_OF_BOARD_PIECE[0] * line_num,
                    self.y + SIZE_OF_BOARD_PIECE[1] * line_num,
                )
            )
            for spot in dr_spots:
                try:
                    if (
                        spot.y > HEIGHT
                        or spot.x > WIDTH
                        or spot.collision_detection(pieces).color == "black"
                    ):
                        dr_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False
                except AttributeError:
                    if spot.collision_detection(pieces):
                        run = False
            line_num += 1
        run = True
        line_num = 1
        ur_spots = []
        while run:
            ur_spots.append(
                Spot(
                    self.x + SIZE_OF_BOARD_PIECE[0] * line_num,
                    self.y - SIZE_OF_BOARD_PIECE[1] * line_num,
                )
            )
            for spot in ur_spots:
                try:
                    if (
                        spot.y < 0
                        or spot.x > WIDTH
                        or spot.collision_detection(pieces).color == "black"
                    ):
                        ur_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False
                except AttributeError:
                    if spot.collision_detection(pieces):
                        run = False
            line_num += 1
        run = True
        line_num = 1
        dl_spots = []
        while run:
            dl_spots.append(
                Spot(
                    self.x - SIZE_OF_BOARD_PIECE[0] * line_num,
                    self.y + SIZE_OF_BOARD_PIECE[1] * line_num,
                )
            )
            for spot in dl_spots:
                try:
                    if (
                        spot.x > WIDTH
                        or spot.y > HEIGHT
                        or spot.collision_detection(pieces).color == "black"
                    ):
                        dl_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False
                except AttributeError:
                    if spot.collision_detection(pieces):
                        run = False
            line_num += 1
        run = True
        line_num = 1
        ul_spots = []
        while run:
            ul_spots.append(
                Spot(
                    self.x - SIZE_OF_BOARD_PIECE[0] * line_num,
                    self.y - SIZE_OF_BOARD_PIECE[1] * line_num,
                )
            )
            for spot in ul_spots:
                try:
                    if (
                        spot.x < 0
                        or spot.y < 0
                        or spot.collision_detection(pieces).color == "black"
                    ):
                        ul_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False
                except AttributeError:
                    if spot.collision_detection(pieces):
                        run = False
            line_num += 1
        self.spots = ul_spots + dl_spots + ur_spots + dr_spots

    def show_positions(self, pieces):
        self.spots = []
        if self.color == "black":
            self.add_spots_black(pieces)

        elif self.color == "white":
            self.add_spots_white(pieces)
        return self.spots


class Queen(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        if color == "black":
            self.piece_img = BLACK_QUEEN
        else:
            self.piece_img = WHITE_QUEEN

    def move(self, pieces, spot_pos):
        if self.color == "black":
            self.y += spot_pos[1] - self.y
            self.x += spot_pos[0] - self.x
            if self.collision_detection(pieces):
                piece = self.collision_detection(pieces)
                return piece
            if self.first_turn:
                self.first_turn = False

        elif self.color == "white":
            self.y -= self.y - spot_pos[1]
            self.x -= self.x - spot_pos[0]
            if self.collision_detection(pieces):
                piece = self.collision_detection(pieces)
                return piece
            if self.first_turn:
                self.first_turn = False

    def add_spots_black(self, pieces):
        run = True
        line_num = 1
        d_spots = []
        while run:
            d_spots.append(Spot(self.x, self.y + SIZE_OF_BOARD_PIECE[1] * line_num))
            for spot in d_spots:
                try:
                    if (
                        spot.y > HEIGHT
                        or spot.collision_detection(pieces).color == "black"
                    ):
                        d_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False

                except AttributeError:
                    if spot.collision_detection(pieces):
                        print("down collision")
                        run = False
            line_num += 1
        run = True
        line_num = 1
        u_spots = []
        while run:
            u_spots.append(Spot(self.x, self.y - SIZE_OF_BOARD_PIECE[1] * line_num))
            for spot in u_spots:
                try:
                    if spot.y < 0 or spot.collision_detection(pieces).color == "black":
                        u_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False

                except AttributeError:
                    if spot.collision_detection(pieces):
                        print("up collision")
                        run = False
            line_num += 1
        run = True
        line_num = 1
        r_spots = []
        while run:
            r_spots.append(Spot(self.x + SIZE_OF_BOARD_PIECE[0] * line_num, self.y))
            for spot in r_spots:
                try:
                    if (
                        spot.x > WIDTH
                        or spot.collision_detection(pieces).color == "black"
                    ):
                        r_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False

                except AttributeError:
                    if spot.collision_detection(pieces):
                        print("right collision")
                        run = False
            line_num += 1
        run = True
        line_num = 1
        l_spots = []
        while run:
            l_spots.append(Spot(self.x - SIZE_OF_BOARD_PIECE[0] * line_num, self.y))
            for spot in l_spots:
                try:
                    if spot.x < 0 or spot.collision_detection(pieces).color == "black":
                        l_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False
                except AttributeError:
                    if spot.collision_detection(pieces):
                        run = False
            line_num += 1

        run = True
        line_num = 1
        dr_spots = []
        while run:
            dr_spots.append(
                Spot(
                    self.x + SIZE_OF_BOARD_PIECE[0] * line_num,
                    self.y + SIZE_OF_BOARD_PIECE[1] * line_num,
                )
            )
            for spot in dr_spots:
                try:
                    if (
                        spot.y > HEIGHT
                        or spot.collision_detection(pieces).color == "black"
                    ):
                        dr_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False

                except AttributeError:
                    if spot.collision_detection(pieces):
                        print("down collision")
                        run = False
            line_num += 1
        run = True
        line_num = 1
        ul_spots = []
        while run:
            ul_spots.append(
                Spot(
                    self.x - SIZE_OF_BOARD_PIECE[0] * line_num,
                    self.y - SIZE_OF_BOARD_PIECE[1] * line_num,
                )
            )
            for spot in ul_spots:
                try:
                    if spot.y < 0 or spot.collision_detection(pieces).color == "black":
                        ul_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False

                except AttributeError:
                    if spot.collision_detection(pieces):
                        print("up collision")
                        run = False
            line_num += 1
        run = True
        line_num = 1
        ur_spots = []
        while run:
            ur_spots.append(
                Spot(
                    self.x + SIZE_OF_BOARD_PIECE[0] * line_num,
                    self.y - SIZE_OF_BOARD_PIECE[1] * line_num,
                )
            )
            for spot in ur_spots:
                try:
                    if (
                        spot.x > WIDTH
                        or spot.collision_detection(pieces).color == "black"
                    ):
                        ur_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False

                except AttributeError:
                    if spot.collision_detection(pieces):
                        print("right collision")
                        run = False
            line_num += 1
        run = True
        line_num = 1
        dl_spots = []
        while run:
            dl_spots.append(
                Spot(
                    self.x - SIZE_OF_BOARD_PIECE[0] * line_num,
                    self.y + SIZE_OF_BOARD_PIECE[1] * line_num,
                )
            )
            for spot in dl_spots:
                try:
                    if spot.x < 0 or spot.collision_detection(pieces).color == "black":
                        dl_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False
                except AttributeError:
                    if spot.collision_detection(pieces):
                        run = False
            line_num += 1
        self.spots = (
            ul_spots
            + dr_spots
            + ur_spots
            + dl_spots
            + u_spots
            + d_spots
            + r_spots
            + l_spots
        )

    def add_spots_white(self, pieces):
        run = True
        line_num = 1
        d_spots = []
        while run:
            d_spots.append(Spot(self.x, self.y + SIZE_OF_BOARD_PIECE[1] * line_num))
            for spot in d_spots:
                try:
                    if (
                        spot.y > HEIGHT
                        or spot.collision_detection(pieces).color == "white"
                    ):
                        d_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False
                except AttributeError:
                    if spot.collision_detection(pieces):
                        run = False
            line_num += 1
        run = True
        line_num = 1
        u_spots = []
        while run:
            u_spots.append(Spot(self.x, self.y - SIZE_OF_BOARD_PIECE[1] * line_num))
            for spot in u_spots:
                try:
                    if spot.y < 0 or spot.collision_detection(pieces).color == "white":
                        u_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False
                except AttributeError:
                    if spot.collision_detection(pieces):
                        run = False
            line_num += 1
        run = True
        line_num = 1
        r_spots = []
        while run:
            r_spots.append(Spot(self.x + SIZE_OF_BOARD_PIECE[0] * line_num, self.y))
            for spot in r_spots:
                try:
                    if (
                        spot.x > WIDTH
                        or spot.collision_detection(pieces).color == "white"
                    ):
                        r_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False
                except AttributeError:
                    if spot.collision_detection(pieces):
                        run = False
            line_num += 1
        run = True
        line_num = 1
        l_spots = []
        while run:
            l_spots.append(Spot(self.x - SIZE_OF_BOARD_PIECE[0] * line_num, self.y))
            for spot in l_spots:
                try:
                    if spot.x < 0 or spot.collision_detection(pieces).color == "white":
                        l_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False
                except AttributeError:
                    if spot.collision_detection(pieces):
                        run = False
            line_num += 1

        run = True
        line_num = 1
        dr_spots = []
        while run:
            dr_spots.append(
                Spot(
                    self.x + SIZE_OF_BOARD_PIECE[0] * line_num,
                    self.y + SIZE_OF_BOARD_PIECE[1] * line_num,
                )
            )
            for spot in dr_spots:
                try:
                    if (
                        spot.y > HEIGHT
                        or spot.collision_detection(pieces).color == "white"
                    ):
                        dr_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False

                except AttributeError:
                    if spot.collision_detection(pieces):
                        print("down collision")
                        run = False
            line_num += 1
        run = True
        line_num = 1
        ul_spots = []
        while run:
            ul_spots.append(
                Spot(
                    self.x - SIZE_OF_BOARD_PIECE[0] * line_num,
                    self.y - SIZE_OF_BOARD_PIECE[1] * line_num,
                )
            )
            for spot in ul_spots:
                try:
                    if spot.y < 0 or spot.collision_detection(pieces).color == "white":
                        ul_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False

                except AttributeError:
                    if spot.collision_detection(pieces):
                        print("up collision")
                        run = False
            line_num += 1
        run = True
        line_num = 1
        ur_spots = []
        while run:
            ur_spots.append(
                Spot(
                    self.x + SIZE_OF_BOARD_PIECE[0] * line_num,
                    self.y - SIZE_OF_BOARD_PIECE[1] * line_num,
                )
            )
            for spot in ur_spots:
                try:
                    if (
                        spot.x > WIDTH
                        or spot.collision_detection(pieces).color == "white"
                    ):
                        ur_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False

                except AttributeError:
                    if spot.collision_detection(pieces):
                        print("right collision")
                        run = False
            line_num += 1
        run = True
        line_num = 1
        dl_spots = []
        while run:
            dl_spots.append(
                Spot(
                    self.x - SIZE_OF_BOARD_PIECE[0] * line_num,
                    self.y + SIZE_OF_BOARD_PIECE[1] * line_num,
                )
            )
            for spot in dl_spots:
                try:
                    if spot.x < 0 or spot.collision_detection(pieces).color == "white":
                        dl_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False
                except AttributeError:
                    if spot.collision_detection(pieces):
                        run = False
            line_num += 1
        self.spots = (
            ul_spots
            + dr_spots
            + ur_spots
            + dl_spots
            + u_spots
            + d_spots
            + r_spots
            + l_spots
        )

    def show_positions(self, pieces):
        self.spots = []
        if self.color == "black":
            self.add_spots_black(pieces)

        elif self.color == "white":
            self.add_spots_white(pieces)
        return self.spots


class Rook(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        if color == "black":
            self.piece_img = BLACK_ROOK
        else:
            self.piece_img = WHITE_ROOK

    def move(self, pieces, spot_pos):
        if self.color == "black":
            self.y += spot_pos[1] - self.y
            self.x += spot_pos[0] - self.x
            if self.collision_detection(pieces):
                piece = self.collision_detection(pieces)
                return piece
            if self.first_turn:
                self.first_turn = False

        elif self.color == "white":
            self.y -= self.y - spot_pos[1]
            self.x -= self.x - spot_pos[0]
            if self.collision_detection(pieces):
                piece = self.collision_detection(pieces)
                return piece
            if self.first_turn:
                self.first_turn = False

    def add_spots_white(self, pieces):
        run = True
        line_num = 1
        d_spots = []
        while run:
            d_spots.append(Spot(self.x, self.y + SIZE_OF_BOARD_PIECE[1] * line_num))
            for spot in d_spots:
                try:
                    if (
                        spot.y > HEIGHT
                        or spot.collision_detection(pieces).color == "white"
                    ):
                        d_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False
                except AttributeError:
                    if spot.collision_detection(pieces):
                        run = False
            line_num += 1
        run = True
        line_num = 1
        u_spots = []
        while run:
            u_spots.append(Spot(self.x, self.y - SIZE_OF_BOARD_PIECE[1] * line_num))
            for spot in u_spots:
                try:
                    if spot.y < 0 or spot.collision_detection(pieces).color == "white":
                        u_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False
                except AttributeError:
                    if spot.collision_detection(pieces):
                        run = False
            line_num += 1
        run = True
        line_num = 1
        r_spots = []
        while run:
            r_spots.append(Spot(self.x + SIZE_OF_BOARD_PIECE[0] * line_num, self.y))
            for spot in r_spots:
                try:
                    if (
                        spot.x > WIDTH
                        or spot.collision_detection(pieces).color == "white"
                    ):
                        r_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False
                except AttributeError:
                    if spot.collision_detection(pieces):
                        run = False
            line_num += 1
        run = True
        line_num = 1
        l_spots = []
        while run:
            l_spots.append(Spot(self.x - SIZE_OF_BOARD_PIECE[0] * line_num, self.y))
            for spot in l_spots:
                try:
                    if spot.x < 0 or spot.collision_detection(pieces).color == "white":
                        l_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False
                except AttributeError:
                    if spot.collision_detection(pieces):
                        run = False
            line_num += 1
        self.spots = u_spots + d_spots + l_spots + r_spots

    def add_spots_black(self, pieces):
        run = True
        line_num = 1
        d_spots = []
        while run:
            d_spots.append(Spot(self.x, self.y + SIZE_OF_BOARD_PIECE[1] * line_num))
            for spot in d_spots:
                try:
                    if (
                        spot.y > HEIGHT
                        or spot.collision_detection(pieces).color == "black"
                    ):
                        d_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False

                except AttributeError:
                    if spot.collision_detection(pieces):
                        print("down collision")
                        run = False
            line_num += 1
        run = True
        line_num = 1
        u_spots = []
        while run:
            u_spots.append(Spot(self.x, self.y - SIZE_OF_BOARD_PIECE[1] * line_num))
            for spot in u_spots:
                try:
                    if spot.y < 0 or spot.collision_detection(pieces).color == "black":
                        u_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False

                except AttributeError:
                    if spot.collision_detection(pieces):
                        print("up collision")
                        run = False
            line_num += 1
        run = True
        line_num = 1
        r_spots = []
        while run:
            r_spots.append(Spot(self.x + SIZE_OF_BOARD_PIECE[0] * line_num, self.y))
            for spot in r_spots:
                try:
                    if (
                        spot.x > WIDTH
                        or spot.collision_detection(pieces).color == "black"
                    ):
                        r_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False

                except AttributeError:
                    if spot.collision_detection(pieces):
                        print("right collision")
                        run = False
            line_num += 1
        run = True
        line_num = 1
        l_spots = []
        while run:
            l_spots.append(Spot(self.x - SIZE_OF_BOARD_PIECE[0] * line_num, self.y))
            for spot in l_spots:
                try:
                    if spot.x < 0 or spot.collision_detection(pieces).color == "black":
                        l_spots.remove(spot)
                        run = False
                    if spot.collision_detection(pieces):
                        run = False
                except AttributeError:
                    if spot.collision_detection(pieces):
                        run = False
            line_num += 1
        self.spots = l_spots + r_spots + u_spots + d_spots

    def show_positions(self, pieces):
        self.spots = []
        if self.color == "black":
            self.add_spots_black(pieces)

        elif self.color == "white":
            self.add_spots_white(pieces)
        return self.spots


class King(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        if color == "black":
            self.piece_img = BLACK_KING
        else:
            self.piece_img = WHITE_KING

    def move(self, pieces, spot_pos):
        if self.color == "black":
            self.y += spot_pos[1] - self.y
            self.x += spot_pos[0] - self.x
            if self.collision_detection(pieces):
                piece = self.collision_detection(pieces)
                if self.first_turn:
                    self.first_turn = False
                return piece
            if self.first_turn:
                self.first_turn = False

        elif self.color == "white":
            self.y -= self.y - spot_pos[1]
            self.x += spot_pos[0] - self.x
            if self.collision_detection(pieces):
                piece = self.collision_detection(pieces)
                if self.first_turn:
                    self.first_turn = False
                return piece
            if self.first_turn:
                self.first_turn = False

    def show_positions(self, pieces):
        self.spots = []
        spots = []
        if self.color == "black":
            spots.append(Spot(self.x, self.y + SIZE_OF_BOARD_PIECE[1]))
            spots.append(Spot(self.x, self.y - SIZE_OF_BOARD_PIECE[1]))
            spots.append(Spot(self.x + SIZE_OF_BOARD_PIECE[0], self.y))
            spots.append(Spot(self.x - SIZE_OF_BOARD_PIECE[0], self.y))
            spots.append(
                Spot(self.x + SIZE_OF_BOARD_PIECE[0], self.y + SIZE_OF_BOARD_PIECE[1])
            )
            spots.append(
                Spot(self.x - SIZE_OF_BOARD_PIECE[0], self.y + SIZE_OF_BOARD_PIECE[1])
            )
            spots.append(
                Spot(self.x + SIZE_OF_BOARD_PIECE[0], self.y - SIZE_OF_BOARD_PIECE[1])
            )
            spots.append(
                Spot(self.x - SIZE_OF_BOARD_PIECE[0], self.y - SIZE_OF_BOARD_PIECE[1])
            )

            self.spots = spots[:]
            for spot in spots:
                if spot.x <= 0 or spot.x >= WIDTH or spot.y <= 0 or spot.y >= HEIGHT:
                    self.spots.remove(spot)
                if not spot.collision_detection(pieces):
                    continue
                if spot.collision_detection(pieces).color == "black":
                    self.spots.remove(spot)

        elif self.color == "white":
            spots.append(Spot(self.x, self.y + SIZE_OF_BOARD_PIECE[1]))
            spots.append(Spot(self.x, self.y - SIZE_OF_BOARD_PIECE[1]))
            spots.append(Spot(self.x + SIZE_OF_BOARD_PIECE[0], self.y))
            spots.append(Spot(self.x - SIZE_OF_BOARD_PIECE[0], self.y))
            spots.append(
                Spot(self.x + SIZE_OF_BOARD_PIECE[0], self.y + SIZE_OF_BOARD_PIECE[1])
            )
            spots.append(
                Spot(self.x - SIZE_OF_BOARD_PIECE[0], self.y + SIZE_OF_BOARD_PIECE[1])
            )
            spots.append(
                Spot(self.x + SIZE_OF_BOARD_PIECE[0], self.y - SIZE_OF_BOARD_PIECE[1])
            )
            spots.append(
                Spot(self.x - SIZE_OF_BOARD_PIECE[0], self.y - SIZE_OF_BOARD_PIECE[1])
            )

            self.spots = spots[:]
            for spot in spots:
                if spot.x <= 0 or spot.x >= WIDTH or spot.y <= 0 or spot.y >= HEIGHT:
                    self.spots.remove(spot)
                if not spot.collision_detection(pieces):
                    continue
                if spot.collision_detection(pieces).color == "white":
                    self.spots.remove(spot)

        return self.spots


class Spot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = SPOT

    def collision_detection(self, pieces):
        for piece in pieces:
            if (
                self.img.get_rect(x=self.x, y=self.y).colliderect(
                    piece.piece_img.get_rect(x=piece.x, y=piece.y)
                )
                and piece is not self
            ):
                return piece
        return False


# FUNCTIONS


def initialize_white_pieces():
    w_bishop1 = Bishop(
        (SIZE_OF_BOARD_PIECE[0] * 5) / 2 - WHITE_BISHOP.get_width() / 2,
        (SIZE_OF_BOARD_PIECE[1] * 15) / 2 - WHITE_BISHOP.get_height() / 2,
        "white",
    )
    w_bishop2 = Bishop(
        (SIZE_OF_BOARD_PIECE[0] * 11) / 2 - WHITE_BISHOP.get_width() / 2,
        (SIZE_OF_BOARD_PIECE[1] * 15) / 2 - WHITE_BISHOP.get_height() / 2,
        "white",
    )
    w_queen = Queen(
        (SIZE_OF_BOARD_PIECE[0] * 7) / 2 - WHITE_QUEEN.get_width() / 2,
        (SIZE_OF_BOARD_PIECE[1] * 15) / 2 - WHITE_QUEEN.get_height() / 2,
        "white",
    )
    w_king = King(
        (SIZE_OF_BOARD_PIECE[0] * 9) / 2 - WHITE_KING.get_width() / 2,
        (SIZE_OF_BOARD_PIECE[1] * 15) / 2 - WHITE_KING.get_height() / 2,
        "white",
    )
    w_knight1 = Knight(
        (SIZE_OF_BOARD_PIECE[0] * 3) / 2 - WHITE_KNIGHT.get_width() / 2,
        (SIZE_OF_BOARD_PIECE[1] * 15) / 2 - WHITE_KNIGHT.get_height() / 2,
        "white",
    )
    w_knight2 = Knight(
        (SIZE_OF_BOARD_PIECE[0] * 13) / 2 - WHITE_KNIGHT.get_width() / 2,
        (SIZE_OF_BOARD_PIECE[1] * 15) / 2 - WHITE_KNIGHT.get_height() / 2,
        "white",
    )
    w_rook1 = Rook(
        (SIZE_OF_BOARD_PIECE[0]) / 2 - WHITE_ROOK.get_width() / 2,
        (SIZE_OF_BOARD_PIECE[1] * 15) / 2 - WHITE_ROOK.get_height() / 2,
        "white",
    )
    w_rook2 = Rook(
        (SIZE_OF_BOARD_PIECE[0] * 15) / 2 - WHITE_ROOK.get_width() / 2,
        (SIZE_OF_BOARD_PIECE[1] * 15) / 2 - WHITE_ROOK.get_height() / 2,
        "white",
    )
    w_pawn1 = Pawn(
        SIZE_OF_BOARD_PIECE[0] / 2 - BLACK_PAWN.get_width() / 2,
        (SIZE_OF_BOARD_PIECE[1] * 13) / 2 - BLACK_PAWN.get_height() / 2,
        "white",
    )
    w_pawn2 = Pawn(
        (SIZE_OF_BOARD_PIECE[0] * 3) / 2 - WHITE_PAWN.get_width() / 2,
        (SIZE_OF_BOARD_PIECE[1] * 13) / 2 - WHITE_PAWN.get_height() / 2,
        "white",
    )
    w_pawn3 = Pawn(
        (SIZE_OF_BOARD_PIECE[0] * 5) / 2 - WHITE_PAWN.get_width() / 2,
        (SIZE_OF_BOARD_PIECE[1] * 13) / 2 - WHITE_PAWN.get_height() / 2,
        "white",
    )
    w_pawn4 = Pawn(
        (SIZE_OF_BOARD_PIECE[0] * 7) / 2 - WHITE_PAWN.get_width() / 2,
        (SIZE_OF_BOARD_PIECE[1] * 13) / 2 - WHITE_PAWN.get_height() / 2,
        "white",
    )
    w_pawn5 = Pawn(
        (SIZE_OF_BOARD_PIECE[0] * 9) / 2 - WHITE_PAWN.get_width() / 2,
        (SIZE_OF_BOARD_PIECE[1] * 13) / 2 - WHITE_PAWN.get_height() / 2,
        "white",
    )
    w_pawn6 = Pawn(
        (SIZE_OF_BOARD_PIECE[0] * 11) / 2 - WHITE_PAWN.get_width() / 2,
        (SIZE_OF_BOARD_PIECE[1] * 13) / 2 - WHITE_PAWN.get_height() / 2,
        "white",
    )
    w_pawn7 = Pawn(
        (SIZE_OF_BOARD_PIECE[0] * 13) / 2 - WHITE_PAWN.get_width() / 2,
        (SIZE_OF_BOARD_PIECE[1] * 13) / 2 - WHITE_PAWN.get_height() / 2,
        "white",
    )
    w_pawn8 = Pawn(
        (SIZE_OF_BOARD_PIECE[0] * 15) / 2 - WHITE_PAWN.get_width() / 2,
        (SIZE_OF_BOARD_PIECE[1] * 13) / 2 - WHITE_PAWN.get_height() / 2,
        "white",
    )
    return [
        w_rook1,
        w_knight1,
        w_bishop1,
        w_queen,
        w_king,
        w_bishop2,
        w_knight2,
        w_rook2,
        w_pawn1,
        w_pawn2,
        w_pawn3,
        w_pawn4,
        w_pawn5,
        w_pawn6,
        w_pawn7,
        w_pawn8,
    ]


def initialize_black_pieces():
    b_bishop1 = Bishop(
        (SIZE_OF_BOARD_PIECE[0] * 5) / 2 - BLACK_BISHOP.get_width() / 2,
        (SIZE_OF_BOARD_PIECE[1]) / 2 - BLACK_BISHOP.get_height() / 2,
        "black",
    )
    b_bishop2 = Bishop(
        (SIZE_OF_BOARD_PIECE[0] * 11) / 2 - BLACK_BISHOP.get_width() / 2,
        (SIZE_OF_BOARD_PIECE[1]) / 2 - BLACK_BISHOP.get_height() / 2,
        "black",
    )
    b_queen = Queen(
        (SIZE_OF_BOARD_PIECE[0] * 7) / 2 - BLACK_QUEEN.get_width() / 2,
        (SIZE_OF_BOARD_PIECE[1]) / 2 - BLACK_QUEEN.get_height() / 2,
        "black",
    )
    b_king = King(
        (SIZE_OF_BOARD_PIECE[0] * 9) / 2 - BLACK_KING.get_width() / 2,
        (SIZE_OF_BOARD_PIECE[1]) / 2 - BLACK_KING.get_height() / 2,
        "black",
    )
    b_knight1 = Knight(
        (SIZE_OF_BOARD_PIECE[0] * 3) / 2 - BLACK_KNIGHT.get_width() / 2,
        (SIZE_OF_BOARD_PIECE[1]) / 2 - BLACK_KNIGHT.get_height() / 2,
        "black",
    )
    b_knight2 = Knight(
        (SIZE_OF_BOARD_PIECE[0] * 13) / 2 - BLACK_KNIGHT.get_width() / 2,
        (SIZE_OF_BOARD_PIECE[1]) / 2 - BLACK_KNIGHT.get_height() / 2,
        "black",
    )
    b_rook1 = Rook(
        (SIZE_OF_BOARD_PIECE[0]) / 2 - BLACK_ROOK.get_width() / 2,
        (SIZE_OF_BOARD_PIECE[1]) / 2 - BLACK_ROOK.get_height() / 2,
        "black",
    )
    b_rook2 = Rook(
        (SIZE_OF_BOARD_PIECE[0] * 15) / 2 - BLACK_ROOK.get_width() / 2,
        (SIZE_OF_BOARD_PIECE[1]) / 2 - BLACK_ROOK.get_height() / 2,
        "black",
    )
    b_pawn1 = Pawn(
        SIZE_OF_BOARD_PIECE[0] / 2 - BLACK_PAWN.get_width() / 2,
        (SIZE_OF_BOARD_PIECE[1] * 3) / 2 - BLACK_PAWN.get_height() / 2,
        "black",
    )
    b_pawn2 = Pawn(
        (SIZE_OF_BOARD_PIECE[0] * 3) / 2 - BLACK_PAWN.get_width() / 2,
        (SIZE_OF_BOARD_PIECE[1] * 3) / 2 - BLACK_PAWN.get_height() / 2,
        "black",
    )
    b_pawn3 = Pawn(
        (SIZE_OF_BOARD_PIECE[0] * 5) / 2 - BLACK_PAWN.get_width() / 2,
        (SIZE_OF_BOARD_PIECE[1] * 3) / 2 - BLACK_PAWN.get_height() / 2,
        "black",
    )
    b_pawn4 = Pawn(
        (SIZE_OF_BOARD_PIECE[0] * 7) / 2 - BLACK_PAWN.get_width() / 2,
        (SIZE_OF_BOARD_PIECE[1] * 3) / 2 - BLACK_PAWN.get_height() / 2,
        "black",
    )
    b_pawn5 = Pawn(
        (SIZE_OF_BOARD_PIECE[0] * 9) / 2 - BLACK_PAWN.get_width() / 2,
        (SIZE_OF_BOARD_PIECE[1] * 3) / 2 - BLACK_PAWN.get_height() / 2,
        "black",
    )
    b_pawn6 = Pawn(
        (SIZE_OF_BOARD_PIECE[0] * 11) / 2 - BLACK_PAWN.get_width() / 2,
        (SIZE_OF_BOARD_PIECE[1] * 3) / 2 - BLACK_PAWN.get_height() / 2,
        "black",
    )
    b_pawn7 = Pawn(
        (SIZE_OF_BOARD_PIECE[0] * 13) / 2 - BLACK_PAWN.get_width() / 2,
        (SIZE_OF_BOARD_PIECE[1] * 3) / 2 - BLACK_PAWN.get_height() / 2,
        "black",
    )
    b_pawn8 = Pawn(
        (SIZE_OF_BOARD_PIECE[0] * 15) / 2 - BLACK_PAWN.get_width() / 2,
        (SIZE_OF_BOARD_PIECE[1] * 3) / 2 - BLACK_PAWN.get_height() / 2,
        "black",
    )
    return [
        b_rook1,
        b_knight1,
        b_bishop1,
        b_queen,
        b_king,
        b_bishop2,
        b_knight2,
        b_rook2,
        b_pawn1,
        b_pawn2,
        b_pawn3,
        b_pawn4,
        b_pawn5,
        b_pawn6,
        b_pawn7,
        b_pawn8,
    ]


def separate_pieces(pieces):
    rooks = []
    king = []
    queen = []
    bishops = []
    knights = []
    pawns = []
    for piece in pieces:
        if type(piece) == Rook:
            rooks.append(piece)
        if type(piece) == King:
            king.append(piece)
        if type(piece) == Queen:
            queen.append(piece)
        if type(piece) == Bishop:
            bishops.append(piece)
        if type(piece) == Knight:
            knights.append(piece)
        if type(piece) == Pawn:
            pawns.append(piece)
    return pawns, rooks, knights, bishops, king, queen
