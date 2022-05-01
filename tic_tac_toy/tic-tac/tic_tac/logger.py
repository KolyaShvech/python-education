from datetime import datetime # From module datetime import datatime.


class Logger:
    """
    Create class Logger. In this class I am doing all action this logger in current time:
    show log, clear log, add log and writing all statistic about game and players.
    """
    @staticmethod
    def _get_current_time():
        """
        Staticmethod _get_current_time. This method returned current time, when game were stopping.
        """
        return datetime.now().strftime("%m/%d/%Y, %H:%M")

    @staticmethod
    def show_logs():
        """
        Staticmethod show_logs. This method are doing to write logging in file
        and show info about games.
        """
        with open('tic_tac/logs/game_logs.txt', 'r') as reader:
            print('LOGS'.center(16, '-'))
            for line in reader.readlines():
                print(line.strip())

    @staticmethod
    def clean_logs():
        """
        Staticmethod clear_logs. This method are doing to clear logging in file
        and clear info about last games.
        """
        print('Clearing logs...')
        with open('tic_tac/logs/game_logs.txt', 'r+') as cleaner:
            cleaner.truncate(0)
        print('Logs cleared.')

    @staticmethod
    def add_log(log_message):
        """
        Staticmethod add_log. This method are adding new info about games in file
        and you will show in termital.
        """
        print(log_message)
        with open('tic_tac/logs/game_logs.txt', 'a') as writer:
            writer.write(log_message)

    def log_statistic(self, game_statistic):
        """
        Create method log_statistic with parameter game_statistic. This method determines
        the type of past game: single or multiple.
        """
        number_of_games = self._get_number_of_games(game_statistic)
        if number_of_games == 1:
            self._log_single_game_statistic(game_statistic)
        else:
            self._log_multiple_game_statistic(game_statistic)

    @staticmethod
    def _get_number_of_games(game_statistic):
        """
        Staticmethod _get_number_of_game this parameters game_statistic.
        """
        return sum(game_statistic.values())

    def _log_single_game_statistic(self, game_statistic):
        """
        Method _log_single_game_statistic with parameter game_statistic. This method
        showing with what result ended up single game.
        """
        if game_statistic['draw'] == 1:
            message = self._get_draw_message(game_statistic)
        else:
            message = self._get_win_message(game_statistic)

        self.add_log(message)

    def _get_draw_message(self, game_statistic):
        """
        Method _get_draw_message with parameters game_statistic.
        """
        player1, player2 = self._get_players_name(game_statistic)
        time = self._get_current_time()

        return f'{time} – {player1} and {player2} – Draw.\n'

    @staticmethod
    def _get_players_name(game_statistic):
        """
        Method _get_players_name with parameters game_statistic. Get name player who
        does not equal 'draw'.
        """
        return [key for key in game_statistic.keys() if key != 'draw']

    def _get_win_message(self, game_statistic):
        winner_name = self._get_winner_name(game_statistic)
        time = self._get_current_time()

        return f'{time} – Player {winner_name} won.\n'

    @staticmethod
    def _get_winner_name(game_statistic):
        """
        Staticmethod _get_name_winner with parameter game_statistic. In this method
        we get name player who win in game.
        """
        for key, value in game_statistic.items():
            if value == 1:
                return key

    def _log_multiple_game_statistic(self, game_statistic):
        """
        Method _log_multiple_game_statistic with parameters game_statistic. Display the
        message about multiple game with the result of each player's game.
        """
        player1, player2 = self._get_players_name(game_statistic)
        time = self._get_current_time()

        message = f'{time} – Player {player1} won {game_statistic[player1]} times. ' \
                  f'Player {player2} won {game_statistic[player2]} times. ' \
                  f'Draw – {game_statistic["draw"]} times\n'

        self.add_log(message)
