

# Python: Why import Dict, List, Tuple?
from typing import Dict, List, Tuple

# Python: Define a class
# Python: Know the difference between class and object
class SnakeInAGrid:

    # Python: Classes should have __init__ function for initialising
    # Initialise
    # Python: int is a type hint
    # Python: = 4 is default value when you don't pass an argument
    # Python: functions associated with objects have self as the first parameter. self is the object
    def __init__(self, grid_size: int = 4):
        # Python: in __init__ you declare and initialise properties for your class
        # Python: self. refers to these properties
        # Python: convention is to use caps for constants, but Python doesn't stop you from changing its value
        self.calls:int = 0
        self.GRID_SIZE: int = grid_size

        # Python: Why is _calculate_starting_cells_and_multiplicicy called with SnakeInAGrid._calculate_starting_cells_and_multiplicicy
        # rather than self._calculate_starting_cells_and_multiplicicy
        self.START_CELLS_AND_SYMMETRY_MULTIPLICITY: List[Tuple[int, int]] = \
            SnakeInAGrid._calculate_starting_cells_and_multiplicicy(grid_size)

        # Python: : Dict[int, List[int]] is a type hint saying that neighbours is a dict,
        # its key is int, its valie is a list of int
        # Python: = dict() initialises neighbours to an empty dict
        # The neighbours of each cell. The key is the cell number, the value is the list of its neighbours
        self.neighbours: Dict[int, List[int]] = dict()

        # The list of cells filled by parts of the snake. Maybe this does not need to be a property
        self.filled: List[int] = list()
        self.dead_end_routes_found: List[List[int]] = list()
        self.successful_routes_found: List[List[int]] = list()

        for cell in range (self.GRID_SIZE * self.GRID_SIZE):
            self._calculate_neighbours(cell)


    # Python: functions associated with objects have self as the first parameter. self is the object
    # Python: _ prefix mark function as private, it can only be called from inside the class, not outside
    # Setting up grid
    def _calculate_neighbours(self, cell: int):
        self.neighbours[cell] = list()

        neighbour = self._get_north_neighbour(cell)
        if neighbour is not None:
            self.neighbours[cell].append(neighbour)
        
        neighbour = self._get_east_neighbour(cell)
        if neighbour is not None:
            self.neighbours[cell].append(neighbour)

        neighbour = self._get_south_neighbour(cell)
        if neighbour is not None:
            self.neighbours[cell].append(neighbour)

        neighbour = self._get_west_neighbour(cell)
        if neighbour is not None:
            self.neighbours[cell].append(neighbour)


    # Python: -> int|None means this function returns int or None
    # Setting up grid
    def _get_north_neighbour(self, cell: int) -> int|None:
        # Top row has no north neighnour
        candidate_neighbour = cell - self.GRID_SIZE
        if candidate_neighbour >= 0:
            return candidate_neighbour
        # Python: it is pythonic not to use an else here
        return None


    # Setting up grid
    def _get_south_neighbour(self, cell: int) -> int|None:
        # Bottom row has no south neighbour
        candidate_neighbour = cell + self.GRID_SIZE
        if candidate_neighbour < self.GRID_SIZE * self.GRID_SIZE:
            return candidate_neighbour
        return None


    # Setting up grid
    def _get_east_neighbour(self, cell: int) -> int|None:
        # Rightmost column has no east neighbour
        candidate_neighbour = cell + 1
        if candidate_neighbour%self.GRID_SIZE != 0 and \
            candidate_neighbour < self.GRID_SIZE * self.GRID_SIZE:
            return candidate_neighbour
        return None


    # Setting up grid
    def _get_west_neighbour(self, cell: int) -> int|None:
        # Leftmost column has no west neighbour
        candidate_neighbour = cell - 1
        if candidate_neighbour%self.GRID_SIZE != self.GRID_SIZE - 1 and \
            candidate_neighbour >= 0:
            return candidate_neighbour
        return None


    # Python: Why doesn't this function have a self parameter?
    # To calculate the total number of fits, we could calculate the number of fits for starting at each cell then add them up.
    # However, it is more efficient to make use of symmetry. Eg, with a 2x2 grid, instead of starting at all 4 cells, we can
    # start at 1 cell and multiply the number of fits by 4, which we call the multiplicity.
    # This function returns a list of the starting cells for a given grid size and the multiplicities.
    # Each cell and its multiplicity is store in a tuple.
    def _calculate_starting_cells_and_multiplicicy(grid_size: int) -> List[Tuple[int, int]]:
        configs: Dict[int, List[Tuple[int, int]]] = {
            1: [(0, 1)],
            2: [(0, 4)],
            # This tests starting from every cell
            #3: [(0, 1), (1, 1), (2, 1),
            #    (3, 1), (4, 1), (5, 1),
            #    (6, 1), (7, 1), (8, 1)],
            3: [(0, 4), (1, 4), (4, 1)],
            # This tests starting from every cell
            #4: [(0, 1), (1, 1), (2, 1), (3, 1),
            #    (4, 1), (5, 1), (6, 1), (7, 1),
            #    (8, 1), (9, 1), (10, 1), (11, 1),
            #    (12, 1), (13, 1), (14, 1), (15, 1)],
            4: [(0, 4), (1, 8), (5, 4)],
            # This tests starting from every cell
            #5: [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
            #    (5, 1), (6, 1), (7, 1), (8, 1), (9, 1),
            #    (10, 1), (11, 1), (12, 1), (13, 1), (14, 1),
            #    (15, 1), (16, 1), (17, 1), (18, 1), (19, 1),
            #    (20, 1), (21, 1), (22, 1), (23, 1), (24, 1),]
            5: [(0, 4), (6, 4), (2, 4), (7, 4), (1, 8), (12, 1)],
            6: [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1),
                (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), 
                (12, 1), (13, 1), (14, 1), (15, 1), (16, 1), (17, 1),
                (18, 1), (19, 1), (20, 1), (21, 1), (22, 1), (23, 1),
                (24, 1), (25, 1), (26, 1), (27, 1), (28, 1), (29, 1),
                (30, 1), (31, 1), (32, 1), (33, 1), (34, 1), (35, 1)]
            #6: [(0, 4), (7, 4), (14, 4), (1, 8), (2, 8), (8, 8)] 
        }
        return configs[grid_size]


    def calculate_number_of_fits(self) -> int:
        total_fits: int = 0
        for start_config in self.START_CELLS_AND_SYMMETRY_MULTIPLICITY:
            start_cell: int = start_config[0]
            multiplicity: int = start_config[1]

            grid.find_fits_from_start(start_cell)

            #print(f'Number of fits starting from {start_cell}: {len(grid.successful_routes_found)}')
            #print(f'Times multiplicity {multiplicity}: {len(grid.successful_routes_found) * multiplicity}')
            total_fits += len(grid.successful_routes_found) * multiplicity
        return total_fits


    # Python: this function does not have a _ prefix. It can be called from outside the class
    # Call this to find the fits for a given start cell
    def find_fits_from_start(self, start_cell: int = 0):
        # Initialise, clear data from previous run
        self.filled.clear()
        self.dead_end_routes_found.clear()
        self.successful_routes_found.clear()

        # Python: Use of formattted print
        #print (f'===> Start from {start_cell}')
        self.filled.append(start_cell)
        self._fill_recursively_from_cell_minimal(start_cell)

        #print(f'Fits found starting from {start_cell}: {self.successful_routes}')
        #print(f'Number of fits starting from {start_cell}: {len(self.successful_routes_found)}')


    # This function fills the cells from a given cell one cell at a time using recursion:
    # Works out the cells accessible from it.
    # For each accessible cell, fill it, then call the function itself recursively.
    # The terminating condition is there is no accessible cell.
    def _fill_recursively_from_cell(self, cell: int):
        self.calls += 1
        # Find the cells accessible from the given cell.
        # Accessible cells are its neighbours minus cells that have been filled.
        # Python: Familiarise with the data structures tuple, list, set, dict
        accessible_cells: list = list(set(self.neighbours[cell]).difference(self.filled))
        #print(f'Explore from cell {cell}, filled {self.filled}, accessible {accessible_cells}')
    
        # A recursive function must return when there are termicating cases, aka base cases,
        # otherwise it will run until it runs out of memory. When a recursive function returns,
        # the return can cascade upward.
        # Normally there is one terminating case, eg, when calculating factorial, the factorial
        # of 1 is 1.

        # However, for this problem there are 2 terminating cases:
        # 1. One is that the cell we're looking at has no accessible cell.
        # - if no accessible cell and we haven't filled the grid then we have reached a dead end.
        #   Record this dead end route, which is not necessary but useful for seeing what is going on.
        # - if no accessible cell and we have filled the grid then we have a successful fit.
        # 2. The other is that we have processed every accessible cells from the cell we're looking at. In
        # this case we simply return

        # Check for first terminating case: the cell we're looking at has no accessible cell
        # Python: to check that a list is empty, can do check len(my_list) == 0, but
        # the pythonic way is check not my_list. This works because empty lists are falsy
        if not accessible_cells:
            # If we have filled the grid then it's a successful route
            if len(self.filled) == self.GRID_SIZE * self.GRID_SIZE:
                # Need to take a snapshot of filled as the successful route because it will be modified later
                self.successful_routes_found.append(self.filled.copy())
                #self.print_snake(self.filled)
                #print(f'Fitted snake {self.filled}, returning')
            else:
                # Need to take a snapshot of filled as the dead end route because it will be modified later
                self.dead_end_routes_found.append(self.filled.copy())
                #print(f'Got dead end {self.filled}, returning')
            # Don't have to return here because if there is no accessible cell the rest of
            # the function is not excecuted and the function will return anyway, but it is clearer
            return
        
        # If there are accessible cells then for each one fill it and call _fill_from_cell recursively
        for accessible_cell in accessible_cells:
            #print (f'Fill {accessible_cell}')
            self.filled.append(accessible_cell)
            # This is the recursive call
            self._fill_recursively_from_cell(accessible_cell)
            # Coming out of the recursion means we have explored all routes from accessible_cell.
            # So we clear accessible_cell so we can try exploring from another accessible_cell
            #print(f'Return from _fill_recursively_from_cell({accessible_cell}), clear {self.filled[-1]}')
            del self.filled[-1]

        # When the code reaches this point, it has returned from _fill_recursively_from_cell(accessible_cell)
        # for every accessible cell, which is a terminating case, and the function returns.
        #print(f'Explored all cells accessible from {cell}, returning with filled = {self.filled}')


    def _fill_recursively_from_cell_minimal(self, cell: int):
        accessible_cells: list = list(set(self.neighbours[cell]).difference(self.filled))
        if not accessible_cells:
            if len(self.filled) == self.GRID_SIZE * self.GRID_SIZE:
                self.successful_routes_found.append(self.filled.copy())
            return
        
        for accessible_cell in accessible_cells:
            self.filled.append(accessible_cell)
            self._fill_recursively_from_cell_minimal(accessible_cell)
            del self.filled[-1]


    # This converts a cell number to the x and y co-ords in a grid of a given size
    # We don't actually use it
    def cell_to_x_y(self, cell: int) -> Tuple[int, int]:
        quotient_remainder = divmod(cell, self.GRID_SIZE)
        x: int = quotient_remainder[1]
        y: int = quotient_remainder[0]
        return (x, y)
    

    # This converts the x and y co-ords in a grid of a given size to a cell number
    def x_y_to_cell(self, x: int, y: int) -> int:
        return (y) * self.GRID_SIZE + x


    # This convert a list like [10, 7, 15] to a dict {10: 0, 7: 1, 15: 2}
    # ie, the keys are the list values and orders in the list.
    # So id the snake is [10, 7, 15], the dict tells us that cell 10 is the first part,
    # cell 7 is the second part, cell 15 is the third part
    def dict_of_cell_orders(cells: List[int]) -> Dict[int, int]:
        return {key: value for value, key in enumerate(cells)}


    # This prints a snake in the grid in the form
    # ----------
    # |04|05|06|
    # ----------
    # |03|00|07|
    # ----------
    # |02|01|08|
    # ----------
    def print_snake(self, snake: List[int]):
        snake_dict: Dict[int, int] = SnakeInAGrid.dict_of_cell_orders(snake)
        row_separator: str = '-' * (grid.GRID_SIZE * 3 + 1)
        print (row_separator)
        for y in range(grid.GRID_SIZE):
            row_string: str = '|'
            for x in range(grid.GRID_SIZE):
                cell = self.x_y_to_cell(x, y)
                if cell in snake_dict:
                    cell_string = str(snake_dict[cell]).zfill(2) + '|'
                else:
                    cell_string = '  |'
                row_string += cell_string
            print(row_string)
            print (row_separator)


#=====================================================================================
# This is the main program
grid: SnakeInAGrid = SnakeInAGrid(4)
# 1: 1
# 2: 8
# 3: 40
# 4: 552
# 5: 8648
# 6: 458696
total_fits: int = grid.calculate_number_of_fits()
print(f'Total fits with all starting points and symmetry: {total_fits}')


