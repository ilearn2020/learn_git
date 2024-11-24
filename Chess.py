from enum import Enum
Piece_type = Enum('chess', ['K', 'Q', 'r', 'b', 'n', 'p' ])

black_pieces = [Piece_type.KING, Piece_type.QUEEN, Piece_type.ROOK, Piece_type.ROOK,
                 Piece_type.KNIGHT, Piece_type.KNIGHT, Piece_type.BISHOP, Piece_type.BISHOP,
                   Piece_type.PAWN, Piece_type.PAWN, Piece_type.PAWN, Piece_type.PAWN,
                     Piece_type.PAWN, Piece_type.PAWN, Piece_type.PAWN, Piece_type.PAWN]

white_pieces = [Piece_type.KING, Piece_type.QUEEN, Piece_type.ROOK, Piece_type.ROOK,
                 Piece_type.KNIGHT, Piece_type.KNIGHT, Piece_type.BISHOP, Piece_type.BISHOP,
                   Piece_type.PAWN, Piece_type.PAWN, Piece_type.PAWN, Piece_type.PAWN,
                     Piece_type.PAWN, Piece_type.PAWN, Piece_type.PAWN, Piece_type.PAWN]
