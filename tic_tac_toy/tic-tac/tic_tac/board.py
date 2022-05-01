class Board:
    """
    Create class Board. This class need for print, refresh and get status info about board.
    """

    def __init__(self):
        self._board = [[' ', ' ', ' '] for _ in range(3)]

    def print_board(self):
        """
        Method print_board. This method print board.
        """
        print('    1   2   3')
        line = '-' * 13
        print(f'  {line}')
        for row_id, row in enumerate(self._board):
            print(f'{row_id + 1} |', end='')
            for col_id, item in enumerate(row):
                end = '\n' if col_id == 2 else ''
                print(f' {item} |', end=end)
            print(f'  {line}')
        print()

    def is_game_over(self, sign):
        """
        Method is_game_over. In this method find all winning combinations.
        """
        # Check rows
        for row in self._board:
            if all([item == sign for item in row]):
                return True

        # Check columns
        for i in range(3):
            if all([row[i] == sign for row in self._board]):
                return True

        # Check diagonals
        if all([self._board[i][i] == sign for i in range(3)]) or all([self._board[i][2 - i] == sign for i in range(3)]):
            return True

        return False

    def process_move(self, sign):
        """
        Method process_move. In this method entered coordinates to move, doing make
        sure that the coordinates are correct, that the cell is empty.
        """
        while True:
            try:
                row_id, col_id = map(int, input('Enter row id and column id separated by comma: ').split(','))
                row_id -= 1
                col_id -= 1

                if not (0 <= row_id <= 2) or not (0 <= col_id <= 2):
                    print('Row id or/and col id must be in range from 1 to 3.\n'
                          'Please, enter a valid row id or/and col id.\n')
                    continue
                elif self._board[row_id][col_id] != ' ':
                    print('This cell is already filled. Please, choose another one.\n')
                    continue
                else:
                    self._board[row_id][col_id] = sign
                    break
            except ValueError:
                print('Wrong input!\n')
                continue

    def reset_board(self):
        """
        Method reset_board. This method refresh board for new game.
        """
        self._board = [[' ', ' ', ' '] for _ in range(3)]
