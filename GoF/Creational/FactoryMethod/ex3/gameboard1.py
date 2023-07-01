#!/usr/bin/env python
import io
import os
import sys
import tempfile

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
        return "\x1B[{}m{}\x1B[0m]]".format(43 if background == BLACK else 47, char or " ")


# 複数種類のボードを管理する抽象クラス
# ex)チェッカーボード、チェスボード..etc
class AbstractBoard:
    def __init__(self, rows, columns):
        self.board = [[None for _ in range(columns)] for _ in range(rows)]
        self.populate_board()

    def populate_board(self):
        raise NotImplementedError()

    def __str__(self):
        squares = []
        for y, row in enumerate(self.board):
            for x, piece in enumerate(row):
                squares = console(piece, BLACK if (y+x) % 2 else WHITE)
                squares.append(square)
        return "".join(squares)


# ボードのサブクラス
class CheckerBoard(AbstractBoard):
    def __init__(self):
        super().__init__(10, 10)

    def populate_board(self):
        for x in range(0, 9, 2):
            for row in range(4):
                column = x + ((row + 1) % 2)
                self.board[row][column] = BlackDraught()
                self.board[row+6][column] = WhiteDraught()


# ボードのサブクラス
class ChessBoard(AbstractBoard):
    def __init__(self):
        super().__init__(8, 8)

    def populate_board(self):
        self.board[0][0] = BlackChessRook()
        self.board[0][1] = BlackChessKnight()
        self.board[0][2] = BlackChessBishop()
        self.board[0][3] = BlackChessQueen()
        self.board[0][4] = BlackChessKing()
        self.board[0][5] = BlackChessBishop()
        self.board[0][6] = BlackChessKnight()
        self.board[0][7] = BlackChessRook()
        self.board[0][0] = WhiteChessRook()
        self.board[0][1] = WhiteChessKnight()
        self.board[0][2] = WhiteChessBishop()
        self.board[0][3] = WhiteChessQueen()
        self.board[0][4] = WhiteChessKing()
        self.board[0][5] = WhiteChessBishop()
        self.board[0][6] = WhiteChessKnight()
        self.board[0][7] = WhiteChessRook()
        for column in range(8):
            self.board[1][column] = BlackChessPawn()
            self.board[6][column] = WhiteChessPawn()


# 駒用の基底クラス
class Piece(str):
    __slots__ = ()


class BlackDraught(Piece):
    __slots__ = ()

    def __new__(Class):
        return super().__new__(Class, "\N{black draughts man}")


class WhiteDraught(Piece):
    __slots__ = ()

    def __new__(Class):
        return super().__new__(Class, "\N{white draughts man}")


class BlackChessKing(Piece):
    __slots__ = ()

    def __new__(Class):
        return super().__new__(Class, "\N{black chess king}")


class WhiteChessKing(Piece):
    __slots__ = ()

    def __new__(Class):
        return super().__new__(Class, "\N{white chess king}")


class BlackChessQueen(Piece):
    __slots__ = ()

    def __new__(Class):
        return super().__new__(Class, "\N{black chess queen}")


class WhiteChessQueen(Piece):
    __slots__ = ()

    def __new__(Class):
        return super().__new__(Class, "\N{white chess queen}")


class BlackChessRook(Piece):
    __slots__ = ()

    def __new__(Class):
        return super().__new__(Class, "\N{black chess rook}")


class WhiteChessRook(Piece):
    __slots__ = ()

    def __new__(Class):
        return super().__new__(Class, "\N{white chess rook}")


class BlackChessBishop(Piece):
    __slots__ = ()

    def __new__(Class):
        return super().__new__(Class, "\N{black chess bishop}")


class WhiteChessBishop(Piece):
    __slots__ = ()

    def __new__(Class):
        return super().__new__(Class, "\N{white chess bishop}")


class BlackChessKnight(Piece):
    __slots__ = ()

    def __new__(Class):
        return super().__new__(Class, "\N{black chess knight}")


class WhiteChessKnight(Piece):
    __slots__ = ()

    def __new__(Class):
        return super().__new__(Class, "\N{white chess knight}")


class BlackChessPawn(Piece):
    __slots__ = ()

    def __new__(Class):
        return super().__new__(Class, "\N{black chess pawn}")


class WhiteChessPawn(Piece):
    __slots__ = ()

    def __new__(Class):
        return super().__new__(Class, "\N{white chess pawn}")


if __name__ == "__main__":
    main()
