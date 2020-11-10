import copy

class Sudoku():
    def __init__(self, state:[], size:[], sub_column_size:int, sub_row_size:int):

        self.state = state
        self.size = size
        self.sub_column_size = sub_column_size
        self.sub_row_size = sub_row_size
        self.domains = {}
        self.update_domains()

    def update_domains(self):
        self.domains = {}
        numbers = []

        # Loop state
        for y in range(self.size):
            for x in range(self.size):
                # Check if cell is empty
                if (self.state[y][x] == 0):
                    # Loop all possible numbers
                    numbers = []
                    for number in range(1, self.size + 1):
                        # Check if number is consistent
                        if(self.is_consistent(number, y, x) == True):
                            numbers.append(number)
                    # Add numbers to a domain
                    if(len(numbers) > 0):
                        self.domains[(y,x)] = numbers

    # Check if a number can be put in a cell
    def is_consistent(self, number:int, row:int, column:int) -> bool:
        # Check a row
        for x in range(self.size):
            # Return false if the number exists in the row
            if self.state[row][x] == number:
                return False
        # Check a column
        for y in range(self.size):
            # Return false if the number exists in the column
            if self.state[y][column] == number:
                return False
        # Calculate row start and column start
        row_start = (row//self.sub_row_size)*self.sub_row_size
        col_start = (column//self.sub_column_size)*self.sub_column_size
        # Check sub matrix
        for y in range(row_start, row_start+self.sub_row_size):
            for x in range(col_start, col_start+self.sub_column_size):
                # Return false if number exists in the submatrix
                if self.state[y][x] == number:
                    return False
        return True

    # First empty cell --- backtracking search 1
    def get_first_empty_cell(self) -> ():
        # Loop the state
        for y in range(self.size):
            for x in range(self.size):
                # Check if the cell is empty
                if (self.state[y][x] == 0):
                    return (y, x)
        return (None, None)

    # Check if puzzle is solved
    def solved(self) -> bool:
        # Loop the state
        for y in range(self.size):
            for x in range(self.size):
                # check if cell is empty
                if (self.state[y][x] == 0):
                    return False
        return True

    # Solve puzzle
    def backtracking_search(self) -> bool:
        # Get first empty cell
        y, x = self.get_first_empty_cell()
        # check if puzzle is solved
        if(y == None or x==None):
            return True
        # Assign a number
        for number in range(1, self.size+1):
            if(self.is_consistent(number, y, x)):
                self.state[y][x] = number
                if (self.backtracking_search() == True):
                    return True
                self.state[y][x] = 0
        return False

    def print_state(self):
        for y in range(self.size):
            print('| ', end='')
            if y != 0 and y % self.sub_row_size == 0:
                for j in range(self.size):
                    print(' - ', end='')
                    if (j + 1) < self.size and (j + 1) % self.sub_column_size == 0:
                        print(' +', end='')
                print(' |')
                print('| ', end='')
            for x in range(self.size):
                if x != 0 and x % self.sub_column_size == 0:
                    print(' |', end='')
                digit = str(self.state[y][x]) if len(str(self.state[y][x])) > 1 else ' ' + str(self.state[y][x])
                print('{0} '.format(digit), end='')
            print(' |')


def main():
    numbers = [0,2,0,0,0,0,0,0,0,0,0,0,6,0,0,0,0,3,0,7,4,0,8,0,0,0,0,0,0,0,0,0,3,0,0,2,0,8,0,0,4,0,0,1,0,6,0,0,5,0,0,0,0,0,0,0,0,0,1,0,7,8,0,5,0,0,0,0,9,0,0,0,0,0,0,0,0,0,0,4,0]
    size = 9
    sub_column_size = 3
    sub_row_size = 3

    initial_state = []
    row = []
    counter = 0

    for number in numbers:
        counter += 1
        row.append(number)
        if(counter >= size):
            initial_state.append(row)
            row = []
            counter = 0

    sudoku = Sudoku(initial_state, size, sub_column_size, sub_row_size)

    print('Puzzle input: ')
    sudoku.print_state()

    sudoku.backtracking_search()

    print('\nPuzzle solution: ')
    sudoku.print_state()
    print()

if __name__ == "__main__": main()
