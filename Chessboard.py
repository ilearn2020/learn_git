from enum import Enum

Enum_piece_type = Enum('piece_type', ['p','r','n','b','q','k'])
Enum_rows  = Enum('row', ['1', '2', '3', '4', '5', '6', '7', '8'])
Enum_Column = Enum('column', ['A',  'B', 'C', 'D', 'E', 'F', 'G', 'H'])
new_chess_board = []

def make_piece_name(piece_type: Enum_piece_type, column: Enum_Column) -> str:
    piece_name : str = piece_type.name +column.name
    return piece_name

def make_pieces() -> list[str]:
    return [
        make_piece_name(Enum_piece_type.p, Enum_Column.A),
        make_piece_name(Enum_piece_type.p, Enum_Column.B),
        make_piece_name(Enum_piece_type.p, Enum_Column.C),
        make_piece_name(Enum_piece_type.p, Enum_Column.D),
        make_piece_name(Enum_piece_type.p, Enum_Column.E),
        make_piece_name(Enum_piece_type.p, Enum_Column.F),
        make_piece_name(Enum_piece_type.p, Enum_Column.G),
        make_piece_name(Enum_piece_type.p, Enum_Column.H),
        make_piece_name(Enum_piece_type.r, Enum_Column.A),
        make_piece_name(Enum_piece_type.n, Enum_Column.B),
        make_piece_name(Enum_piece_type.b, Enum_Column.C),
        make_piece_name(Enum_piece_type.q, Enum_Column.D),
        make_piece_name(Enum_piece_type.k, Enum_Column.E),
        make_piece_name(Enum_piece_type.b, Enum_Column.F),
        make_piece_name(Enum_piece_type.k, Enum_Column.G),
        make_piece_name(Enum_piece_type.r, Enum_Column.H),
        ]
    
my_piece_type = Enum_piece_type.p
print(my_piece_type)
print(my_piece_type.name)

my_piece_name = make_piece_name(Enum_piece_type.p, Enum_Column.C)
print(my_piece_name)

black_piece_name : list[str] = make_pieces()
white_piece_names : list[str] = make_pieces()
print(white_piece_names)

white_piece_y_coords: list[int] = [
    1, 1, 1, 1, 1, 1, 1, 1,
    0, 0, 0, 0, 0, 0, 0, 0,
]

white_piece_x_coords: list[int] = [
    0, 1, 2, 3, 4, 5, 6, 7, 
    0, 1, 2, 3, 4, 5, 6, 7,
]

#for i in range(0,16):
#    print(f'Piece {white_piece_names[i]} is at {white_piece_y_coords[i]},{white_piece_x_coords[i]}')


black_piece_positions: list[tuple] = []
for row in range(6,8):
    for col in range(0,9):
        position: tuple = (row, col)
        black_piece_positions.append(position)

white_piece_positions = list(zip(white_piece_y_coords, white_piece_x_coords))

for i in range(0,16):
    print(f'Piece {white_piece_names[i]} is at {white_piece_positions[i]}')

for i in range(0,16):
    print(f'Piece {white_piece_names[i]} is at column {white_piece_positions[i][0]} row {white_piece_positions[i][1]}')


white_pieces: dict[str, tuple[int,int]] ={}
for i in range(0,16):
    white_pieces[white_piece_names[i]] = white_piece_positions[i]

print(white_pieces)
""""
for row in rows:
    new_row = []
    for column in columns:
        cell_name = f'{column}{row}'
        new_row.append(cell_name)
    print(new_row)
    new_chess_board.append(new_row)

print(new_chess_board)
"""