""""
My first bot
"""
import random
import pyjokes
import emoji
from stories_pool import my_story


def jokes():
    """
    Generator of jokes
    :return: pyjokes.get_joke()
    """
    while True:
        joke_choice = input("Бажаєте жарт! введіть >>> 1\nДля виходу в попереднє меню введіть 0 >>> ")
        if joke_choice == '1':
            print(f"{pyjokes.get_joke()} {emoji.emojize(':face_with_tears_of_joy:') * 3}")
        elif joke_choice == '0':
            break
        else:
            print("Неправильний вибір, спробуйте ще раз ")


def games():
    """
    Game Menu
    :return: game_spr() game_random_number() play_game(word_to_guess)
    """
    while True:
        print("Меню 'Ігри'\nКамінь, Ножиці, Папір >>>  1\nВгадай число! >>> 2\nПоле чудес >>> 3 ")
        game_menu_choice = input("Оберіть гру \nДля виходу в попереднє меню введіть 0 >>> ")
        if game_menu_choice == '1':
            game_spr()
        elif game_menu_choice == '2':
            game_random_number()
        elif game_menu_choice == '3':
            play_game(word_to_guess)
        elif game_menu_choice == '0':
            break
        else:
            print("Невірний вибір, спробуйте ще ")


def display_word(word, guessed_letters):
    """
    Display secret word
    :param word:
    :param guessed_letters:
    :return:
    """
    displayed_word = " "
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word


def play_game(word):
    """
    Starting Game
    :param word:
    :return:
    """
    guessed_letters = []
    attempts = len(word) + 2

    print("Гра 'Поле чудес' розпочалася!")
    print(display_word(word, guessed_letters))

    while "_" in display_word(word, guessed_letters) and attempts > 0:
        guess = input("\nВведіть букву: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Будь ласка, введіть одну букву.")
            continue

        if guess in guessed_letters:
            print("Ви вже вводили цю букву.")
            continue

        guessed_letters.append(guess)
        print(display_word(word, guessed_letters))
        attempts -= 1

    if "_" not in display_word(word, guessed_letters):
        print(f"Ви виграли! Загадане слово: {word}")
    else:
        print(f"Ви програли. Загадане слово було: {word} {emoji.emojize(':loudly_crying_face:')}")


words = 'кіця', 'пес', 'дракон', 'банан', 'пітон'
random_words = random.choice(words)
word_to_guess = random_words


def game_random_number():
    """
    Game random number
    User gues number of random pc move
    :return: pc_random
    """
    while True:
        print(
            f"{emoji.emojize(':grinning_face:')} Ви обрали гру <<< Вгадай число! {emoji.emojize(':grinning_face:')} >>>")
        choice_number = input("Ваш хід!\nОберіть число від 1 до 10! >>>\nДля виходу в попереднє меню введіть 0 >>> ")
        if choice_number.isdigit():
            print()
        else:
            print('Тільки від 1, 10')
            continue
        if choice_number == '0':
            break
        pc_random = random.randint(1, 10)
        if choice_number == pc_random:
            print(f"Ви обрали {pc_random} \nВітаю ви виграли! {emoji.emojize(':grinning_face:')} ")
        else:
            print(f"Нажаль ви не вгадали число {pc_random}{emoji.emojize(':loudly_crying_face:')}")


def game_spr():
    """
    Game scissors, paper, rock
    :return:
    """
    pool = ["Ножиці", "Папір", "Камінь"]
    print("Ви обрали гру <<< Камінь, Ножниці, Папір >>>")
    print("Для виходу натисніть 1 ")
    while True:
        game_choice = input("Ваш хід: Камінь, Ножиці чи Папір:\n Для виходу натисніть 1 >>>  ").capitalize()
        # if game_choice != "Камінь" and game_choice != "Ножиці" and game_choice != "Папір" and game_choice != "1":
        if game_choice not in pool:
            print("Неправильний вибір")
            continue
        if game_choice == '1':
            print("Ви повернулись в меню")
            break
        pc_choice = random.choice(pool)
        print(f"Опонент обрав: {pc_choice}")
        if game_choice == pc_choice:
            print("Нічия!")
        elif game_choice == "Ножиці" and pc_choice == "Папір":
            print(f"Вітаю! Ви виграли {emoji.emojize(':grinning_face:')}")
        elif game_choice == "Камінь" and pc_choice == "Ножиці":
            print(f"Вітаю! Ви виграли {emoji.emojize(':grinning_face:')}")
        elif game_choice == "Папір" and pc_choice == "Камінь":
            print(f"Вітаю! Ви виграли {emoji.emojize(':grinning_face:')}")
        else:
            print(f"Ви програли {emoji.emojize(':disappointed_face:')}")


def recommend():
    """
    Menu of recommendation
    Movies, music and games
    :return:
    """
    print("Ви в меню рекомендацій ")
    print('-' * 50)
    while True:
        choice_recommend = input("Яку саме рекомендацію бажаєте\nФільми - 1\nМузика - 2\nІгри - 3"
                                 "\n Для повернення в попереднє меню натисніть 0\n>>> ")
        if choice_recommend == '0':
            print("         Ви повернулись в основне меню ")
            break
        movies = {"Фантастика": ["Месники", "Темний лицар", "Людина-Павук", "Халк"],
                  "Пригодницькі": ["Індіана Джонс", "Анчартед", "Лара Крофт", "Скарби Нації"],
                  "Жахи": ["Воно", "Джиперс-Кріперс", "Відьма з Блер", "Астрал"]}
        music = {"Рок": ["Linkin Park", "Korn", "Led zeppelin", "Beatles", "Bon Jovi",
                         "Pink Floyd", "Queen", "Guns n Roses"],
                 "Класика": ["Вівальді", "Моцарт", "Бах", "Бетховен"],
                 "Техно": ["Artbat", "Solomun", "Boris brejha", "Monolink"]}
        game_list = {"Шутери": ["Doom Eternal", "Call of Duty", "Far Cry", "Counter-Strike"],
                     " Стратегії": ["Civilization", "Dune", "WarCraft", "Cossacks"],
                     "Гонки": ["Need for Speed", "Grid", "Forza", "Gran Turismo"]}

        if choice_recommend == '1':
            while True:
                for genre in movies.keys():
                    print("Оберіть жанр фільму", genre)
                genre_choice = input("Фантастика --- Пригодницькі ---- Жахи   : ").capitalize()
                if genre_choice in movies:
                    movies_in_genre = movies[genre_choice]
                    random_movie = random.choice(movies_in_genre)
                    print("Рекомендую фільм", random_movie)
                    break
                else:
                    print("Неправильний вибір\n \nСпробуйте ще раз \n")
                    continue
        elif choice_recommend == '2':
            while True:
                for genre in music.keys():
                    print("Оберіть жанр музики", genre)
                genre_choice = input("Рок --- Класика --- Техно:  ").capitalize()
                if genre_choice in music:
                    music_in_genre = music[genre_choice]
                    random_music = random.choice(music_in_genre)
                    print("Рекомендую виконавця", random_music)
                    break
                else:
                    print("Неправильний вибір\n \nСпробуйте ще раз \n")
                    continue
        elif choice_recommend == '3':
            while True:
                for genre in game_list:
                    print("Оберіть жанр гри", genre)
                genre_choice = input("Шутери --- Стратегії --- Гонки:  ").capitalize()
                if genre_choice in game_list:
                    game_in_genre = game_list[genre_choice]
                    random_game = random.choice(game_in_genre)
                    print("Рекомендую пограти", random_game)
                    break
                else:
                    print("Неправильний вибір\n \nСпробуйте ще раз \n")
                    continue
        else:
            print("Неправильний вибір\n спробуйте ще раз ")


def stories():
    """
    Pick random stories from menu Story
    :return:
    """
    print("Ви обрали розділ історії\nЩоб почути історію натисніть 1\nДля повернення в початкове меню натисніть 2")
    while True:
        choose_story = int(input(">>> "))
        if choose_story == 1:
            random_story = random.choice(list(my_story.items()))
            print(random_story)
        elif choose_story == 2:
            break
        else:
            print("Неправильний вибір, спробуйте ще раз")


def menu():
    """
    Main Menu
    User choose
    :return: recommend() jokes() stories() games()
    """
    while True:
        start_text = ("<<<< Вітаю ось що я можу вам запропонувати >>>>"
                      "\n [: Дати рекомендацію 1 :]  [: Розказати анекдот 2 :]  [: Розказати історію 3 :]  [: Ігри 4 :]"
                      "\n [: Вихід 5 :]")
        print(start_text.center(200))
        choice_menu = input("Оберіть пункт з меню >>> ")
        if choice_menu == '1':
            recommend()
        elif choice_menu == '2':
            jokes()
        elif choice_menu == '3':
            stories()
        elif choice_menu == '4':
            games()
        elif choice_menu == '5':
            print("Програму завершено\nГарного дня")
            break


if __name__ == '__main__':
    menu()
