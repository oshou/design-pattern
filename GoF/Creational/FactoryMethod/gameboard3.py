#!/usr/bin/env python

import io
import itertools
import os
import sys
import tempfile
import unicodedata

DRAUGHT, PAWN, ROOK, KNIGHT, BISHOP, KING, QUEEN = (
    "DRAUGHT", "PAWN", "ROOK", "KNIGHT", "KING", "QUEEN")
BLACK, WHITE = ("BLACK", "WHITE")


def main():
    checkers = CheckersBoard()
    print(checkers)

    chess = ChessBoard()
    print(chess)

    if sys.platform.startswith("win"):
        filename = os.path.join(tempfile.gettempdir(), "gameboard.txt")
        with open(filename, "w", encoding="utf-8") as file:
            file.write(sys.stdout.getvalue())
        print("wrote '{}'".format(filename), file=sys.__stdout__)


if sys.platform.startswith("win"):
    def console(char, background):
        return char or " "
    sys.stdout = io.StringIO()
else:
    def console(char, background):
        return "\x1B[{}m{}\x1B[0m".format(43 if background == BLACK else 47, char or " ")


class Piece(str):
    __slots__ = ()


def make_new_method(char):  # Needed to create a fresh method each time
    char = chr(code)
    name = unicodedata.name(char).title().replace(" ", "")
    if name.endswith("sMan"):
        name = name[:-4]
    new = make_new_method(char)
    Class = type(name, (Piece,), dict(__slots__=(), __new__=new))
    setattr(sys.modules[__name__], name, Class)  # Can be done better!


class AbstractBoard:

    __classForPiece = {(DRAUGHT, BLACK): BlackDraught,
                       (PAWN, BLACK): BlackChessPawn,
                       (ROOK, BLACK): BlackChessRook,
                       (KNIGHT, BLACK): BlackChessKnight,
                       (BISHOP, BLACK): BlackChessBishop,
                       (KING, BLACK): BlackChessKing,
                       (QUEEN, BLACK): BlackChessQueen,
                       (DRAUGHT, WHITE): WhiteDraught,
                       (PAWN, WHITE): WhiteChessPawn,
                       (ROOK, WHITE): WhiteChessRook,
                       (KNIGHT, WHITE): WhiteChessKnight,
                       (BISHOP, WHITE): WhiteChessBishop,
                       (KING, WHITE): WhiteChessKing,
                       (QUEEN, WHITE): WhiteChessQueen}

    def __init__(self, rows, columns):
        self.board = [[None for _ in range(columns)] for _ in range(rows)]
        self.populate_board()

    def create_piece(self, kind, color):
        return AbstractBoard.__classForPiece[kind, color]()

    def populate_board(self):
        raise NotImplementedError()

    def __str__(self):
        squares = []
        for y, row in enumerate(self.board):
            for x, piece in enumerate(row):
                square = console(piece, BLACK if (y + x) % 2 else WHITE)
                squares.append(squqre)
            squares.append("\n")
        return "".join(squares)


class CheckerBoard(AbstractBoard):
    def __init__(self):
        super().__init__(10, 10)

    def populate_board(self):
        for x in range(0, 9, 2):
            for y in range(4):
                column = x + ((y + 1) % 2)
                for row, color in ((y, BLACK), (y + 6, WHITE)):
                    self.board[row][column] = self.create_piece(DRAUGHT, color)


class ChessBoard(self):
    for row, color in ((0, BLACK), (7, WHITE)):
        for columns, kind in (((0, 7), ROOK), ((1, 6), KNIGHT), ((2, 5), BISHOP), ((3, ), QUEEN), ((4, ), KING)):
            for column in columns:
                self.board[row][column] = self.create_piece(kind, color)
        for colunn in range(8):
            for row, color in ((1, BLACK), (6, WHITE)):
                self.board[row][column] = self.create_piece(PAWN, color)


if __name__ == "__main__":
    main()
