class Menu:
    """
    Create class Menu. In this class written methods for menu show, select and validate options.
    """
    OPTIONS = [
        'Play',
        'Show logs',
        'Clear logs',
        'Exit'
    ]

    def show_options(self):
        """
        Method show_options. It will print numbers options which can turn.
        """
        print('MENU'.center(16, '-'))
        for idx, option in enumerate(self.OPTIONS, start=1):
            print(f'{idx}. {option}')
        print()

    def select_option(self):
        """
        Method select_option. In this method you can enter number to select option which have menu.
        """
        while True:
            option = input(f'Choose option number from 1 to {len(self.OPTIONS)}: ')
            if self._is_option_valid(option):
                return int(option)
            else:
                print('Wrong input! Please try again.\n')

    def _is_option_valid(self, option):
        """
        Method _is_option_validate. In this method I am doing check for the correctness
        of the selected option.
        """
        try:
            option = int(option)
            if not (1 <= option <= len(self.OPTIONS)):
                return False

            return True
        except ValueError:
            return False
