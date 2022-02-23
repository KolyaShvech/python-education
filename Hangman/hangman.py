
"""
GAME HANGMAN
"""

import random

ATTEMPTS = 6  #
START_GAME = 1  #
SHOW_PREVIOUS_WORDS = 2  #
EXIT = 3  #
ALPHABET = [chr(ch_code) for ch_code in range(ord("a"), ord("z") + 1)]  # Алфавит который вводим


def show_menu():
    """
    меня игры "Hangman" с опциями: 1- это играть, 2 - увидить прошлые слова, 3 - выход

    """
    print(f'Выберите одну из следующих опций:\n'
          f'1. Начать\n'
          f'2. Посмотреть прошлые слова\n'
          f'3. Выйти')


def get_option():
    """
    фунция проверки, которая проверяет правильность вводы опций.
    Вводим блок исключений.

    """
    while True:  # Вводим бесконечный цикл 'while'
        try:
            option = int(input("Номер опции: "))  #  Вводим номер опции
            if not (1 <= option <= 3):  # если не опция не равна от 1 до 3
                print("Введите номер опции от 1 до 3")  #
                continue
            return option  # Возращаем опцию
        except ValueError:  # Отлавоиваем ошибку 'ValueError', если пользователь введет буквы
            print("Введите номер опции от 1 до 3")


def get_word():
    """

    Функция, которая получет случайное слово из файла

    """
    with open("data/dictionary.txt", "r") as file:  # открывем файл с режимом на чтение 'r'
        return random.choice(file.read().split(",")).lower()  # Ввыбираем случайное слово из файла, нижний регистр


def get_word_by_status(word, word_status):
    """
    Фукнция, которая возращает статус слова. Создает массив секретного слова, если буква есть в этом слове, то занимает
    место в массиве.

    """
    return " ".join([ch.upper() if word_status[i] is True else "_" for i, ch in enumerate(word)])
# Возращаем объединение буквы в верхнем регистре если индекс статуса слова 'True', если нет то ставим '_'


def print_game_info(word, word_status, wrong_chs):
    """
    Функция, которая выводит статус слова, введенные буквы, считает количесиво ошибок и угаданные буквы.

    """
    print(f"Слово: {get_word_by_status(word, word_status)}")  # Ввыводим полученное слово в виде '_ _ _ _'
    print(f"Ошибки ({len(wrong_chs)}/{ATTEMPTS}): {', '.join(wrong_chs).upper()}")
# Ввыводим длину ошибок деленную на попытки и объединяем с буквами, которые не угаданны.

def get_new_ch():
    """
    Функция, которая возращает букву ввода. Далаем проверку, на случай не правильного ввода буквенного символа.

    """
    while True:
        new_ch = input("Введите букву от 'A' до 'Z': ").upper()  # Ввод новой буквы в верхнем регистре.
        if new_ch not in ALPHABET:  # если введенная буква не в 'ALPHABET'
            print("Вы ввели не верный символ.")  # Пишем, что ввели не правильную букву.
            continue
        return new_ch  # Возрашаем введенную букву.


def update_word_status(init_word, word_status, new_ch):
    """

    Функция обновления статуса слова. Если буква слова равна введеной букве пользователя, то статус слова True

    """
    for index, ch in enumerate(init_word):  # итерируем по индексу и букве в указанном слове.
        if ch == new_ch:  # если буква в слове равна введеной букве.
            word_status[index] = True  # индекс слова 'True'


def is_word_guessed(word_status):
    """

    Функция, которая возращает все значания статуса слова.

    """
    return all(word_status)  # С помощью метода 'all' возращаем статус слова.


def update_game_status(init_word, word_status, wrong_chs, new_ch):
    """

    Функция которая показывает статус игра: выиграл или проиграл пользователь.
    если введенные буквы находяться в загадоном слова, то розлзователь выиграл, если нет, то не правильные буквы,
    добавлятся в 'список не праильных букв' и если длина непральных букв равна попыткам, проиграл.

    """
    if new_ch in init_word:  # если введенная буква в угадываемом слове.
        update_word_status(init_word, word_status, new_ch)  # Берем функцию 'update_word_status' с его значениями
        if is_word_guessed(word_status):  # Если все буквы в слове угаданы
            print(f"Вы угодали слово: {init_word.upper()}")  # Выводим: 'Вы угадали слово'.
            return False
    else:
        wrong_chs.append(new_ch)  # если нет, то добавляем букву в словарь не угаданных букв
        if len(wrong_chs) == ATTEMPTS:  # если длина не правильных букв равна попвткам
            print(f"Вы проиграли. Загаданное слово: {init_word.upper()}")  # Проиграли
            return False

    return True  # Возращаем True


def save_word(init_word):
    """

    Созданная функция используется для сохранения слова в файле 'words'. Это слова, которые уже использовались.

    """
    with open("data/words.txt", "a+") as file:  # Открывеам файл 'word.txt' с разширением 'a+'.
        file.write(f"{init_word}\n")  # читаем нужное слово из файла.
    file.close()  # закрываем файл.


def start_game():
    """
    "Эта функция начало игры. Здесь используем все функции, которые мы создали и объединили.

    """
    init_word = get_word()  #  нужное слово приравниваем к функции 'get_word'.
    word_status = [False for _ in range(len(init_word))]  #  статус слова приравниваем к длине загаданного слова.
    wrong_chs = []  #  создаем пустой лист.
    game_status = True  # статус игры True.

    while game_status:  # делаем бесконечный цикл для статуса игры.
        print_game_info(init_word, word_status, wrong_chs)  # пишем все данные 'print_game_info'
        new_ch = get_new_ch()  # новау букву приравниваем к функции 'get_new_ch'.

        game_status = update_game_status(init_word, word_status, wrong_chs, new_ch)  #
        print()

    save_word(init_word)  #  вызываем функцию сохранить слово с полученным словом.


def show_previous_words():
    """

    Эта функция показывает слова, которые использовались ранее в игре.
    Опцией '2' можно вывести слова.
    Используем блок исключений, в случае ошибки.

    """
    words = []  # создаем пустой словарь
    try:
        with open("data/words.txt", "r") as file:  # окрываем текстовый файл 'words.txt' с разширение 'r'.
            for line in file:  # для линии в файле.
                words.append(line.strip())  # добавлем это слово в словарь 'words'.
    except FileNotFoundError:  # ловим ошибку.
        print("Нет прошлых слов.")
    print(f"Прошлые слова: {', '.join(words)}")  # ввыводим прошлые слова в игре.


"""

Главный блок, который отвечет за ввод опции и игровую консоль.

"""

if __name__ == "__main__":
    game_status = True  # статус игры 'True'.
    while game_status:  # Запускаем цикл 'while'.
        show_menu()  # вызываем меню игры.
        option = get_option()  # опции на фукции 'get_option'.

        if option == START_GAME:  # если опция равна START_GAME.
            start_game()  # то запускаем старт игры.
        elif option == SHOW_PREVIOUS_WORDS:  # если же опция равна SHOW_PREVIOUS_WORDS.
            show_previous_words()  # то выводим прошлый слова в игре.
        else:
            print("Возвращайтесь еще!")  # Ввыодим предложение.
            game_status = False  # останавливаем игру.

