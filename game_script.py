import time  # used to simulate delays of the npc while choosing a letter and add user-friendliness
import os  # used to exit and reload program at the end
import sys  # "

# used for colouring and formatting the output
from rich.console import Console

# other files including functions and assets respectively
import funcs
import text_assets

# for quick word wrapping
console = Console()

# (head + body + arms + legs are 6 pieces)
remaining_attempts = 6
# string that contains all guessed letters by user or computer
guessed_letters = []
# variables used in the story choices
# this variable is used in creating the junction of play word or give word
first_choice: int
# this variable is used in choosing the category of word
second_choice: int = 0
# Variable that is the current guess / chosen word
guess: str
# letter of the current guess
guess_player: str
# variable value used to distinguish between difficulty level
strategy_value = int
# string used for language_identification
hard_mode_lang = str
# path to dictionaries folder
path_to_dict = "DICTIONARIES"
# standard value in value which dictionary
value_which_dictionary = -1
value_if_own_dict = -1
files_in_dir = -1

# Story/Game-Opening ----------------------------

# console.prints the hangman logo
funcs.clean_window()
console.print(text_assets.hangman_art, highlight=False, style="bold red")

console.print("Willkommen zu Galgenmännchen!   Welcome to Hangman!\n")
console.print("Choose your language / Wähle deine Sprache:\n", highlight=False)
console.print(" --- 1. English/Englisch --- 2. German/Deutsch --- ")

# call just for this one function
is_english = True
lang_decide = language = funcs.give_me_a_value_inbetween(0, 2, is_english, True)

if lang_decide == 2:
    is_english = False

# game menu for initial setup
in_game_menu = True
while in_game_menu:
    if is_english:
        funcs.give_separators()

        console.print("This is the Hangman starting menu\n")

        console.print("  1. Start the Game   ")
        console.print("  2. Manual   ")
        console.print("  3. Check Dictionary directory  ")
        console.print("  4. Credits   ")
        console.print("  5. Quit Game  ")

        menu_choice = funcs.give_me_a_value_inbetween(0, 5, True, False)

        if menu_choice == 1:
            in_game_menu = False
        if menu_choice == 2:
            funcs.give_separators()
            console.print("Manual:"
                          "\n")
            console.print(
                "Hanging man is based on the idea of having to guess a word, from which you only know the number\n"
                "of letters at first and can only guess a letter at a time. Once you have guessed wrong, it slowly\n"
                "draws a person being hanged, hence the name. If the word is guessed in under 6 wrong attempts,\n"
                "the person guessing has won.\n"
                "  \n")
            console.print("Once the game starts, you will be given the opportunity to select to either\n"
                          "challenge the computer with a word or to be challenged with a word yourself.\n"
                          " \n"
                          "The word that you can guess, you can select the category of when you decide to play this "
                          "way.\n"
                          " \n"
                          "If you choose to challenge the computer, you will be able to select one of three "
                          "difficulties.\n"
                          "    1. Easy mode. The computer guesses letters randomly\n"
                          "    2. Medium mode. The computer guesses letters from a weighted alphabet.\n"
                          "    3. Hard mode. The computer guesses letters by using a specific algorithm "
                          "with a given dictionary.\n"
                          " \n"
                          "If you choose to challenge the computer, the game automatically checks if there are any "
                          "files\n"
                          "in the game files directory 'DICTIONARIES'. \n"
                          " \n"
                          "If yes, it will ask you if you wish for the computer to use any of these.\n"
                          " \n"
                          "Beware: all letters in file will be made lowercase and words sorted. Filename changed.\n"
                          " \n"
                          "If no, you will be asked if your word is from either english or german. \n"
                          "The computer will then use the in-build dictionaries.\n")
            funcs.give_separators()
            # wait for user input
            input("Press Enter to continue...\n")
            funcs.clean_window()
        if menu_choice == 3:
            # display files in directory with for loop
            console.print("These are, if any, the files in Dir DICTIONARIES:\n")
            files_in_DICTIONARIES = funcs.files_in_dir(path_to_dict)
            for file in files_in_DICTIONARIES:
                console.print(file)
            # wait for user input
            console.print("")
            input("Press Enter to continue...\n")
            funcs.clean_window()
        if menu_choice == 4:
            # display the credits
            funcs.give_separators()
            console.print("Created by Marty Lauterbach as a project for a class in the months of March-June 2023\n"
                          "See github for extended documentaries.\n"
                          "Sources for inspiration in the code are to be found with links in the code itself.\n"
                          "Have fun!\n")
            funcs.give_separators()
            # wait for user input
            input("Press Enter to continue...\n")
            funcs.clean_window()
        if menu_choice == 5:
            sys.exit()

    else:
        funcs.give_separators()
        console.print("Hauptmenü von \"Galgenmännchen : Der Henker und sein Wörterbuch\" \n")

        console.print("  1. Starte das Spiel  ")
        console.print("  2. Anleitung   ")
        console.print("  3. Zeige das DICTIONARIES (Wörterbuch) Verzeichnis  ")
        console.print("  4. Credits   ")
        console.print("  5. Beende das Spiel   ")

        menu_choice = funcs.give_me_a_value_inbetween(0, 5, True, False)

        if menu_choice == 1:
            in_game_menu = False
        if menu_choice == 2:
            console.print("")
            console.print("Anleitung:")
            console.print(
                "Galgenmännchen basiert auf der Idee, ein Wort erraten zu müssen, von dem du anfangs nur die Anzahl\n"
                "der Buchstaben kennst und nur einen Buchstaben auf einmal raten kannst. \n"
                "Sobald du falsch geraten hast, wird langsam das Bild gemalt, wie eine Person"
                " gehängt wird (daher der Name).\n"
                "Wenn das Wort in weniger als 6 falschen Versuchen geraten wird, hat die Person, die rät, gewonnen.\n"
                " \n")
            console.print("Sobald das Spiel beginnt, erhältst du die Möglichkeit, entweder\n"
                          "den Computer mit einem Wort herauszufordern oder selbst mit einem Wort herausgefordert zu "
                          "werden.\n"
                          " \n"
                          "Das Wort, das du erraten kannst, kannst du durch seine Kategorie auswählen.\n"
                          " \n"
                          "Wenn du dich dafür entscheidest, den Computer herauszufordern, kannst du "
                          "eine von drei Schwierigkeiten auswählen.\n"
                          "   1. Einfacher Modus. Der Computer wählt Buchstaben zufällig aus.\n"
                          "   2. Mittlerer Modus. Der Computer wählt Buchstaben aus einem gewichteten Alphabet aus.\n"
                          "   3. Schwerer Modus. Der Computer wählt Buchstaben anhand eines spezifischen Algorithmus "
                          "mit einem gegebenen Wörterbuch aus.\n"
                          " \n"
                          "Wenn du dich dafür entscheidest, den Computer herauszufordern, überprüft das Spiel "
                          "automatisch,"
                          "ob es Dateien im Spielordner 'DICTIONARIES' gibt. \n"
                          "Wenn ja, wird es dich fragen, ob du möchtest, dass der Computer eine davon verwendet.\n"
                          "\n"
                          "     Achtung: Alle Buchstaben in der ausgewählten Datei werden in Kleinbuchstaben "
                          "umgewandelt und Wörter sortiert.\n "
                          "              Dateiname geändert.\n"
                          "\n"
                          "Wenn nein, wirst du gefragt, ob dein Wort entweder Englisch oder Deutsch ist. \n"
                          "Der Computer verwendet dann die integrierten Wörterbücher.\n")
            funcs.give_separators()
            # wait for user input
            input("Drücke Enter um weiterzufahren...\n")
            funcs.clean_window()
        if menu_choice == 3:
            # display files in directory with for loop
            console.print("Dies sind, wenn überhaupt, die Dateien im Dir DICTIONARIES:\n")
            files_in_DICTIONARIES = funcs.files_in_dir(path_to_dict)
            for file in files_in_DICTIONARIES:
                console.print(file)
            # wait for user input
            console.print("")
            input("Drücke Enter um weiterzufahren...\n")
            funcs.clean_window()
        if menu_choice == 4:
            # display the credits
            console.print(
                "Erstellt von Marty Lauterbach als ein Projekt für eine Vorlesung in den Monaten Maerz-Juni 2023\n"
                "Sehe github für extended documentaries.\n"
                "Quellen für Inspiration im Code sind als Kommentare im Code selbst zu finden.\n"
                "Viel Spaß!\n")
            # wait for user input
            input("Drücke Enter um weiterzufahren...\n")
            funcs.clean_window()
        if menu_choice == 5:
            sys.exit()

if is_english:
    funcs.give_separators()
    console.print("\nYou wake up and find a tall shadowy giant towering above you."
                  " He points to a sad, small and thin man in chains, tied to a high beam.\n")
    console.print("The Executioner: Harharhar. Welcome to my wicked game.")
    console.print("Tell me, you dwarf wrangler, to safe this unspoiled being, do you challenge me or do you challenge "
                  "yourself?\n")

    # choice inbetween being challenged or challenging
    console.print("1. Tell a word to the Executioner that he has to guess\n"
                  "2. Be given a word, so you can take guesses and be challenged yourself.\n")
else:
    console.print(
        "Du wachst auf und findest einen riesigen, schattenhaften Riesen vor dir stehen, der über dir aufragt.\n"
        "Er zeigt auf einen traurigen, kleinen und dünnen Mann in Ketten, "
        "der an einem hohen Balken festgebunden ist.\n")
    console.print("Der Henker: Harharhar. Willkommen in meinem verzwickten Spiel.\n")
    console.print("Sag mir, du Zwerganfänger, willst du dieses unschuldige Wesen retten, \n"
                  "indem du mich herausforderst oder dich selbst herausforderst?\n")
    console.print(" ")
    console.print("1. Nenne dem Henker ein Wort, das er erraten muss\n"
                  "2. Erhalte ein Wort, so dass du erraten musst.\n")

first_choice = funcs.give_me_a_value_inbetween(0, 2, is_english, False)

if first_choice == 2:  # the route of being challenged with a word
    if is_english:
        funcs.give_separators()
        console.print("Executioner: So you have chosen to be challenged by one of my words. An interesting choice."
                      "\nYou will be able to mis-guess 6 times, before this human will be hanged by my rope.")
        console.print("\nFrom which of these categories should the word of your challenge be from?\n")

        console.print("\nThese are the choices that lay before you:"
                      "\n1. animals"
                      "\n2. cities"
                      "\n3. food"
                      "\n4. presidents"
                      "\n5. cartoon characters "
                      "\n6. hard words (mixed language)"
                      "\n7. Tiere des deutschen Waldes (german)")

    else:
        funcs.give_separators()
        console.print("Henker: Du hast dich also dafür entschieden, von einem meiner Worte herausgefordert zu werden. "
                      "Eine interessante Wahl."
                      "\nDu darfst 6 Mal falsch raten, bevor dieser Mensch von meinem Seil gehängt wird.")
        console.print("\nAus welcher dieser Kategorien soll das Wort deiner Herausforderung stammen?\n")

        console.print("\nDas sind die Möglichkeiten, die dir zur Verfügung stehen:"
                      "\n1. Tiere (englisch)"
                      "\n2. Städte (englisch)"
                      "\n3. Essen (englisch)"
                      "\n4. Präsidenten (englisch)"
                      "\n5. Cartoon-Charaktere"
                      "\n6. Schwierige Wörter (gemischt)"
                      "\n7. Tiere des deutschen Waldes (deutsch)")

    second_choice = funcs.give_me_a_value_inbetween(0, 7, is_english, False)

    # nested if statements for choosing the right secret word
    if second_choice == 1:
        secret_word = funcs.select_word(text_assets.animals)
    elif second_choice == 2:
        secret_word = funcs.select_word(text_assets.cities)
    elif second_choice == 3:
        secret_word = funcs.select_word(text_assets.food)
    elif second_choice == 4:
        secret_word = funcs.select_word(text_assets.presidents)
    elif second_choice == 5:
        secret_word = funcs.select_word(text_assets.cartoon_characters)
    elif second_choice == 6:
        secret_word = funcs.select_word(text_assets.hard_words)
    elif second_choice == 7:
        secret_word = funcs.select_word(text_assets.animals_german)
        funcs.give_separators()
        console.print("\nah.... deutsche Tiere... jaja, guten Tag Herr Osterhase.")
        funcs.give_separators()
    else:
        secret_word = "errorviernullvier"

    funcs.clean_window()
    # testing
    # console.print(secret_word)
    if is_english:
        funcs.give_separators()
        console.print("Very well, let it BEGIN!")
        funcs.give_separators()
    else:
        funcs.give_separators()
        console.print("Nun gut, möge deine Folter beginnen.")
        funcs.give_separators()
    time.sleep(2)
    funcs.clean_window()
    # used for controlling who gets to play / which part of the code is used
    who_plays: str = "Player"

else:  # The route of challenging with a word
    if is_english:
        funcs.give_separators()
        console.print("YOU DARE TO CHALLENGE ME?")
        funcs.give_separators()

        console.print('I will use my infinitely finite knowledge of the world to cause your destruction.\n'
                      'Although I could crush you, I want to give you a chance... to play with my prey\n'
                      'Would you like me to go easier on you?\n')

        console.print("   1. Yes, please. I am still confused! (easy)\n"
                      "   2. I do not want your pity, but I do want a chance. (medium)\n"
                      "\n   3. Give me the best that you got. You will be my prey. (hard)\n")

        console.print("\n1 , 2 or 3\n")
    else:
        funcs.give_separators()
        console.print("DU WAGST ES, MICH HERAUSZUFORDERN?")
        funcs.give_separators()

        console.print(
            "\nIch werde mein unendlich endliches Wissen gegen dich verwenden, um dein Untergang hervorzurufen.\n"
            "Obwohl ich dich zerstören könnte mit dem Schnipse meines Fingers, möchte ich dir eine Chance geben...\n"
            "... damit es ür mich noch Spaß macht...\n")

        console.print("   1. Ja, bitte. Ich bin immer noch verwirrt! (leicht)\n"
                      "   2. Ich möchte dein Mitleid nicht, aber ich möchte eine Chance. (mittel)\n"

                      "\n    3. Geb mir das Beste was du hast. ICH werde dein Untergang sein. (schweeer)\n")

        console.print("1, 2 oder 3")

    # used for controlling who gets to play / which part of the code is used
    who_plays = "NPC"

    strategy_value = funcs.give_me_a_value_inbetween(0, 3, is_english, False)

    if strategy_value == 3:
        # asks if the user wants to use an in-build dictionary for the computer or if he
        # has provided an own one in the DICTIONARY folder
        # if he has not, go to ask about language:
        # creates a list of the files in the dir
        files_in_dir = funcs.files_in_dir(path_to_dict)
        # length of the former mentioned list
        own_dictionaries = len(files_in_dir)

        # activated if anything in dir
        if own_dictionaries >= 1:
            funcs.give_separators()
            if is_english:
                console.print("Tell me, have you put a dictionary for me into my DICTIONARY box,\n"
                              "that you would like me to use? \n")
                console.print("  1.Yes  2. No \n")
            else:
                console.print("Sag mir, hast du ein Wörterbuch in meine Wörterbuch-Kiste getan,\n"
                              "welches du willst, dass ich benutze? \n")
                console.print("  1.Ja   2. Nein \n")

            value_if_own_dict = funcs.give_me_a_value_inbetween(0, 2, is_english, False)

            # activated if player decided to use a user-input dict
            if value_if_own_dict == 1:
                if is_english:
                    funcs.give_separators()
                    console.print("Which of these dictionaries do you wish to use? \n")
                else:
                    funcs.give_separators()
                    console.print("Welches dieser Wörterbücher wählst du?\n")

                # formats a list of all dictionaries in ~/DICTIONARIES
                zaehler = -1
                for i in files_in_dir:
                    zaehler = zaehler + 1
                    console.print(f" {zaehler}  {i} \n")

                # value for later selection
                value_which_dictionary = funcs.give_me_a_value_inbetween(-1, own_dictionaries, is_english, False)

        # if there are no files in dir, or if user doesn't want to use them
        if own_dictionaries == 0 or value_if_own_dict == 2:
            funcs.give_separators()
            if is_english:
                console.print("Which language will you write your word in?:\n"
                              "\nenglish (1) or german (2)")
            else:
                console.print(
                    "In welcher Sprache wirst du dein Wort schreiben? :\n"
                    "\nEnglisch (1) oder Deutsch (2)")

            lang_value = funcs.give_me_a_value_inbetween(0, 2, is_english, False)

            if lang_value == 2:
                hard_mode_lang = "german"
            else:
                hard_mode_lang = "english"

    funcs.give_separators()
    challenge_word = funcs.user_input_word(is_english)
    secret_word = challenge_word.lower()

    funcs.clean_window()
    if is_english:
        funcs.give_separators()
        console.print("Very well, let it BEGIN!")
        funcs.give_separators()
    else:
        funcs.give_separators()
        console.print("Nun gut, möge deine Folter beginnen.")
        funcs.give_separators()
    time.sleep(2)
    funcs.clean_window()

# ------------------------------------------------------------
# THE GAME
# ------------------------------------------------------------

# The Player is in charge:

length_of_secret_word = int(len(funcs.get_unique_letters(secret_word)))

if who_plays == "Player":

    if is_english:
        console.print(
            "The letter you wish to guess has {} letter´s... do with this Information what you like.\n".format(
                len(secret_word)))
    else:
        console.print(
            "Der gesuchte Buchstabe hat {} Buchstaben... mache mit dieser Information, was du willst.\n".format(
                len(secret_word)))

    while remaining_attempts > 0 and len(guessed_letters) < length_of_secret_word:
        # the while-loop runs while the attempts haven't run out and the player hasn't won

        guess = funcs.guess_player_letter(is_english)  # player takes a guess

        guess_in_secret_word = funcs.is_guess_in_secret_word(guess, secret_word)
        # gives out a True or False value which we store in the variable and use in the following if statements

        if guess_in_secret_word:
            if guess in guessed_letters:
                if is_english:
                    console.print("\nYou have already guessed the letter {}\n".format(guess))
                else:
                    console.print("\nDu hast bereits den Buchstaben {} geraten.\n".format(guess))
            else:
                if is_english:
                    console.print(
                        "\nDamn. You have been right! The letter {} is part of the secret word\n".format(guess))
                else:
                    console.print(
                        "\nVerdammt. Du hast recht! Der Buchstabe {} ist Teil des geheimen Wortes\n".format(guess))
                console.print(funcs.select_word(text_assets.point_player))
                guessed_letters += guess
        else:
            if is_english:
                console.print("\nNo! The letter {} is not part of the secret word\n".format(guess))
            else:
                console.print("\nNein! Der Buchstabe {} ist nicht Teil des geheimen Wortes\n".format(guess))

            console.print(funcs.select_word(text_assets.point_computer))
            remaining_attempts -= 1

        console.print(funcs.get_hangman_stage(remaining_attempts), highlight=False, style="bold")
        funcs.pri_secret_word(secret_word, guessed_letters)

        if is_english:
            console.print("\n You can make {} more mistakes... I would say be careful, but I hope you lose.\n"
                          .format(remaining_attempts))
        else:
            console.print("\nDu hast noch {} Fehler übrig... Ich würde sagen, sei vorsichtig, "
                          "aber ich hoffe, dass du verlierst.\n".format(remaining_attempts))

    if len(guessed_letters) == len(funcs.get_unique_letters(secret_word)):
        funcs.games_callout("Player", is_english)
    else:
        funcs.games_callout("NPC", is_english)

# The Computer is in charge of guessing: ---------------------------------------------------

if who_plays == "NPC":

    if strategy_value == 3:
        # here the version for the high-strategy computer-way, separated for better overview

        if not value_if_own_dict == 1:
            # chosen if user wants to use an inbuilt-dict
            # implemented variable outside of loop, so it doesn't load each time
            dict_before_slice = funcs.open_dictionary(hard_mode_lang)
            sliced_dict = funcs.slice_dict(dict_before_slice, hard_mode_lang, is_english,
                                           secret_word, value_if_own_dict, files_in_dir,
                                           value_which_dictionary)
        else:
            # uses the user-input-dictionary
            # we don't need the open dict function, since it is implemented in the slice_dict function
            empty_list: list = []
            sliced_dict = funcs.slice_dict(empty_list, hard_mode_lang, is_english, secret_word,
                                           value_if_own_dict, files_in_dir,
                                           value_which_dictionary)

        remove_letters = []

        while remaining_attempts > 0 and len(guessed_letters) < length_of_secret_word:
            # the while-loop runs while the attempts haven't run out and the computer hasn't won

            empty_solv_dict = funcs.letter_frequency_structure_maker(secret_word, text_assets.alphabet)

            # creates a dict where the frequency of elements at letter positions
            # is measured for remaining words in sliced_dict
            solving_dict = funcs.iterate_dict_to_sol_dict(sliced_dict, empty_solv_dict)

            # computer takes a guess based on the highest amount of an element it found in solving_dict
            # if sliced_dict empty, meaning no known words fit parameters of secret word, use medium strategy
            if len(sliced_dict) == 0:
                guess = funcs.guess_computer_letters_strategy(is_english, guessed_letters)
            else:
                guess = funcs.high_strategy_dictionary(solving_dict, guessed_letters, remove_letters, is_english)

            # gives out a True or False value which we store in the variable and use in the following if statements
            guess_in_secret_word = funcs.is_guess_in_secret_word(guess, secret_word)

            if guess_in_secret_word:

                if guess in guessed_letters:  # meaning the computer has guessed the same thing again
                    # mostly used in case there is a bug somewhere and letters can get chosen more often
                    if is_english:
                        console.print(
                            "\nI have already guessed this letter '{}'... fool me and my old mind\n".format(guess))
                        console.print(
                            "Someone contact the matrix-creator please... I dont feel so good repeating myself.\n")
                    else:
                        console.print("\nIch habe diesen Buchstaben '{}' bereits geraten... "
                                      "täusche mich nicht und meinen alten Verstand.\n".format(guess))
                        console.print("Jemand kontaktiere bitte den Matrix-Schöpfer..."
                                      "Ich fühle mich nicht gut dabei, mich zu wiederholen.\n")
                    console.print(funcs.get_hangman_stage(remaining_attempts), highlight=False, style="bold")
                    guessed_letters.append(guess)
                    funcs.pri_secret_word(secret_word, guessed_letters)

                else:  # meaning that the guess is in secret word, but hasn't been guessed yet
                    if is_english:
                        console.print(
                            "\nI have been right! The letter {} is part of your secret filthy word\n".format(guess))
                    else:
                        console.print("\nIch habe recht gehabt! Der Buchstabe {} ist "
                                      "Teil deines geheimen Wortes.\n".format(guess))
                    time.sleep(2)
                    console.print(funcs.select_word(text_assets.point_computer))
                    console.print(funcs.get_hangman_stage(remaining_attempts), highlight=False, style="bold")
                    guessed_letters.append(guess)
                    funcs.pri_secret_word(secret_word, guessed_letters)
                    # creates a list that is used in understanding where a known element is in the secret word
                    half_hidden_word_list = funcs.format_the_hidden_word(secret_word, guessed_letters)
                    # the just created list and its opposite are used in eliminating
                    # the words that contradict known positional letters
                    sliced_dict = funcs.letter_sniper(solving_dict, sliced_dict, half_hidden_word_list)

            else:  # meaning that the letter is not part of the word.
                if is_english:
                    console.print("\n Nooooo.... The letter {} is not part of your word...\n".format(guess))
                else:
                    "\n Nein! Der Buchstabe {} ist nicht Teil deines Wortes ...\n".format(guess)
                time.sleep(2)
                console.print(funcs.select_word(text_assets.point_player))
                remaining_attempts -= 1
                remove_letters.append(guess)
                sliced_dict = funcs.thinner_the_sliced_dict(sliced_dict, solving_dict, remove_letters)
                console.print(funcs.get_hangman_stage(remaining_attempts), highlight=False, style="bold")
                funcs.pri_secret_word(secret_word, guessed_letters)

            # prevents duplicates in the guessed letters list,
            # in case smth goes wrong, as to not create more systematic bugs
            guessed_letters = funcs.remove_duplicates_in_list(guessed_letters)

            if remaining_attempts > 0:
                # A simple enter anything input that changes nothing, but creates a simple break for
                # the player, so that the computer doesn't run through the skript too quickly.
                # In case, the user likes to read the canon of the Executioner.
                if is_english:
                    console.print("\n I have another {} attempts to go.\n".format(remaining_attempts))
                    time.sleep(1)
                    input("Press Enter to continue...")
                    funcs.clean_window()
                else:
                    console.print("\n Ich habe noch {} Versuche übrig.\n".format(remaining_attempts))
                    time.sleep(1)
                    input("Drücke Enter, um fortzufahren...")
                    funcs.clean_window()
            else:
                if is_english:
                    console.print(
                        "Jeff, with last breath: Why....Please... u should have use a harder woooooordddd.....")
                else:
                    console.print("Jeff, mit seinem letzten Atemzug:\n"
                                  " Warum... Bitte... du hättest... besser ein Wörterbuch selbst nutzen sollen...")
                time.sleep(2)

    else:
        while remaining_attempts > 0 and len(guessed_letters) < length_of_secret_word:
            # the while-loop runs while the attempts haven't run out and the computer hasn't won

            if strategy_value == 1:
                guess = funcs.guess_computer_letter(is_english)  # computer takes a guess
            else:
                guess = funcs.guess_computer_letters_strategy(is_english, guessed_letters)
                # computer takes a structured guess with a higher success chance

            guess_in_secret_word = funcs.is_guess_in_secret_word(guess, secret_word)
            # gives out a True or False value which we store in the variable and use in the following if statements

            if guess_in_secret_word:
                if guess in guessed_letters:
                    if is_english:
                        console.print(
                            "\nI have already guessed this letter '{}'... fool me and my old mind\n".format(guess))
                    else:
                        console.print("\nIch habe diesen Buchstaben '{}' bereits geraten... "
                                      "täusche mich nicht und meinen alten Verstand.\n".format(guess))
                else:
                    if is_english:
                        console.print(
                            "\nI have been right! The letter {} is part of your secret filthy word\n".format(guess))
                    else:
                        console.print("\nIch habe recht gehabt! Der Buchstabe {} ist "
                                      "Teil deines geheimen Wortes.\n".format(guess))
                    console.print(funcs.select_word(text_assets.point_computer))
                    guessed_letters += guess
            else:
                if is_english:
                    console.print("\n Nooooo.... The letter {} is not part of your word...\n".format(guess))
                else:
                    "\n Nein! Der Buchstabe {} ist nicht Teil deines Wortes ...\n".format(guess)
                console.print(funcs.select_word(text_assets.point_player))
                remaining_attempts -= 1

            console.print(funcs.get_hangman_stage(remaining_attempts), highlight=False, style="bold")

            funcs.pri_secret_word(secret_word, guessed_letters)

            if remaining_attempts >= 1:
                # A simple enter anything input that changes nothing, but creates a simple break for
                # the player, so that the computer doesn't run through the skript too quickly.
                # In case, the user likes to read the canon of the Executioner.
                if is_english:
                    console.print("\n I have another {} attempts to go.\n".format(remaining_attempts))
                    input("Press Enter to continue...")
                    funcs.clean_window()
                else:
                    console.print("\n Ich habe noch {} Versuche übrig.\n".format(remaining_attempts))
                    input("Drücke Enter, um fortzufahren...")
                    funcs.clean_window()

    if len(guessed_letters) == len(funcs.get_unique_letters(secret_word)):
        # Function that celebrates the victory of whoever has won
        funcs.games_callout("NPC", is_english)
    else:
        funcs.games_callout("Player", is_english)

if is_english:
    console.print("The secret word was {}\n".format(secret_word))
    funcs.give_separators()

    console.print("*the executioner drags jeff behind him, neither dead or alive, "
                  "trapped in a eternal state of being used as a joke in a video game*\n")

    funcs.give_separators()

    console.print("Narrator: Would you like to face him again? I can always send you back in time\n")
    console.print("1. Go again\n"
                  "2. End this, please!\n")
else:
    console.print("Das geheime Wort war {}\n".format(secret_word))

    funcs.give_separators()

    console.print("der Henker zieht Jeff hinter sich her, weder tot noch lebendig, gefangen in einem ewigen Zustand, "
                  "als Witz in einem Videospiel verwendet zu werden\n")

    funcs.give_separators()

    console.print("Erzähler: Möchtest du dich ihm erneut stellen? Ich kann dich jederzeit zurück "
                  "in die Vergangenheit schicken.\n")
    console.print("1. Nochmal spielen\n"
                  "2. Beende dies bitte!\n")

restart = funcs.give_me_a_value_inbetween(0, 2, is_english, False)

if restart == "1":
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
elif restart == "2":
    console.print("\nThe matrix will be closed...")
    # Done! Time to quit.
    sys.exit(0)
