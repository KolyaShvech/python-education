from tic_tac.board import Board  # from tic_tac.board import Board with functions and parameters.
from tic_tac.logger import Logger  # from tic_tac.logger import Logger with functions and parameters.
from tic_tac.menu import Menu  # from tic_tac.menu import Menu with functions and parameters.


class Game:
    """
    Create class Game. This class consist with parameters: is_menu_running,
_is_game_running, _logger, _menu, _board, _player1, _player2, _is_first_player_turn, count
and _game_statistic.
    """
    def __init__(self):
        self._is_menu_running = False
        self._is_game_running = False
        self._logger = Logger()
        self._menu = Menu()
        self._board = Board()
        self._player1 = None
        self._player2 = None
        self._is_first_player_turn = True
        self._count = 0
        self._game_statistic = {}

    @property
    def _option_action(self):
        """
        Create property method _option_action. Showing action in menu game.
        """
        return {
            1: self._play_game,
            2: self._logger.show_logs,
            3: self._logger.clean_logs,
            4: self._stop
        }

    def start(self):
        """
        Create method start. This method has argument _is_menu_running and _menu.show_options().
        """
        self._is_menu_running = True

        while self._is_menu_running:
            self._menu.show_options()

            option = self._menu.select_option()
            self._process_option(option)

            print()

    def _stop(self):
        """
        Method _stop. This method stopped game.
        """
        print('Thank you! Come again.')
        self._is_menu_running = False

    def _process_option(self, option):
        """
        Method _process_option. In this method doing process option in menu.
        """
        self._option_action[option]()

    def _get_player_name(self, position):
        """
        Method _get_player_name. In this method players is inputing your names.
        """
        player_name = input(f'Type the name of the {position} player: ')
        if position == 'first':
            self._player1 = player_name
        else:
            self._player2 = player_name

    def _get_sign(self):
        """
        Method _get_sigh. Players get sign.
        """
        return 'X' if self._is_first_player_turn else 'O'

    def _play_game(self):
        """
         Method _play_game. In this method described step by step all logic game.
         At first reset board, game info, print board, when game started for player proposes
         to make a move, make move players, refresh board info, game over. If players want
         play again repeat all action again, until the player leaves the game.
        """
        self._reset_board()
        self._get_game_info()

        self._print_board_info()

        self._is_game_running = True
        while self._is_game_running:
            self._print_move_info()

            self._make_move()

            self._print_board_info()

            if self._is_game_over():
                print('Game over!')
                self._update_game_info()

                if self._continue_game():
                    self._reset_board()
                    self._print_board_info()
                else:
                    self._finish_game()
            else:
                self._is_first_player_turn = not self._is_first_player_turn

    def _print_move_info(self):
        """
        Method _print_move_info. In this method offer the player to make a move.
        """
        player_name = f'{self._player1} (X)' if self._is_first_player_turn else f'{self._player2} (O)'
        print(f"It's your turn, {player_name}")

    def _print_board_info(self):
        """
        Method _print_board_info. Print update info game board.
        """
        self._board.print_board()

    def _make_move(self):
        """
        Method _make_move. Players make move his sign on board.
        """
        sign = self._get_sign()
        self._board.process_move(sign)
        self._count += 1

    def _is_game_over(self):
        """
        Method _is_gave_over. If board filled all sign or a player has a winning combination.
        """
        sign = self._get_sign()
        return self._count == 9 or self._board.is_game_over(sign)

    def _get_game_info(self):
        """
        Method _get_game_info. Statistic about games and players.
        """
        self._get_player_name('first')
        self._get_player_name('second')

        self._game_statistic = {
            self._player1: 0,
            self._player2: 0,
            'draw': 0
        }

    def _update_game_info(self):
        """
        Method _update_game_info. In this method write status game, win player,
        lose or draw and add to statistic all games.
        """
        if self._board.is_game_over(self._get_sign()):
            winner = self._player1 if self._is_first_player_turn else self._player2
            self._game_statistic[winner] += 1
        else:
            self._game_statistic['draw'] += 1

    @staticmethod
    def _continue_game():
        """
        Staticmethod _continue_game. If player after game over want play again,
        he must write 'yes'.
        """
        option = input('Do you want to play again? [Yes/no]: ')
        return option.lower() == 'yes'

    def _reset_board(self):
        """
        Method _reset_board. Resets board for new game.
        """
        self._count = 0
        self._is_first_player_turn = True
        self._board.reset_board()

    def _finish_game(self):
        """
        Method _finish_game. When game finish, add statistic to logger.
        """
        self._is_game_running = False
        self._logger.log_statistic(self._game_statistic)
