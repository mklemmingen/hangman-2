import time  # used to simulate delays of the npc while choosing a letter and add user-friendliness
import os  # used to exit and reload programm at end
import sys  # "
import funcs
import RPG_assets

# (head + body + arms + legs are 6 pieces)
remaining_attempts = 6
# string that contains all guessed letters by user or computer
guessed_letters = []
# variables used in the story choices
# this variable is used in creating the junction of play word or give word
first_choice: int
# this variable is used in choosing the category of word
second_choice: int = 0
# the word first used when challenging the executioner
# challenge_word = "ErrorNotGivenOther"
# the secret word, to guess or to e guessed
# secret_word = "ErrorSecretWordWasntChosen"
# Variable that is the current guess / chosen word
guess: str
# letter of the current guess
guess_player: str
# variable value used to distinguish between difficulty level
strategy_value = int
# string used for language_identification
hard_mode_lang = str

# Story/Game-Opening ----------------------------

# prints the hangman logo
print(RPG_assets.hangman_art)

print("Willkommen zu Galgenmännchen!   Welcome to Hangman!\n")
print("Choose your language / Wähle deine Sprache:\n")
print(" --- 1. English/Englisch --- 2. German/Deutsch --- ")

# call just for this one function
is_english = True
lang_decide = language = funcs.give_me_a_value_inbetween(0, 2, is_english, True)

if lang_decide == 2:
    is_english = False

if is_english:
    print("\nYou wake up and find a tall shadowy giant towering above you."
          " He points to a sad, small and thin man in chains, tied to a high beam.\n")
    print("The Executioner: Harharhar. Welcome to my wicked game.")
    print("Tell me, you dwarv wrangler, to safe this unspoiled being, do you challenge me or do you challenge "
          "yourself?\n")

    # choice inbetween being challenged or challenging
    print("1. Tell a word to the Executioner that he has to guess\n"
          "2. Be given a word, so you can take guesses and be challenged yourself.\n")
else:
    print("Du wachst auf und findest einen riesigen, schattenhaften Riesen vor dir stehen, der über dir aufragt.\n"
          "Er zeigt auf einen traurigen, kleinen und dünnen Mann in Ketten, "
          "der an einem hohen Balken festgebunden ist.\n")
    print("Der Henker: Harharhar. Willkommen in meinem verzwickten Spiel.\n")
    print("Sag mir, du Zwergenfänger, willst du dieses unschuldige Wesen retten, \n"
          "indem du mich herausforderst oder dich selbst herausforderst?\n")
    print(" ")
    print("1. Nenne dem Henker ein Wort, das er erraten muss\n"
          "2. Erhalte ein Wort, so dass du erraten musst.\n")

first_choice = funcs.give_me_a_value_inbetween(0, 2, is_english, False)

if first_choice == 2:  # the route of being challenged with a word
    if is_english:
        print("\n--------------------------------------------------------------------------------\n")
        print("Executioner: So you have chosen to be challenged by one of my words. An interesting choice."
              "\nYou will be able to mis-guess 6 times, before this human will be hanged by my rope.")
        print("\nFrom which of these categories should the word of your challenge be from?\n")

        print("\nThese are the choices that lay before you:"
              "\n1. animals"
              "\n2. cities"
              "\n3. food"
              "\n4. presidents"
              "\n5. cartoon characters "
              "\n6. hard words (mixed language)"
              "\n7. Tiere des deutschen Waldes (german)")

    else:
        print("\n--------------------------------------------------------------------------------\n")
        print("Henker: Du hast dich also dafür entschieden, von einem meiner Worte herausgefordert zu werden. "
              "Eine interessante Wahl."
              "\nDu darfst 6 Mal falsch raten, bevor dieser Mensch von meinem Seil gehängt wird.")
        print("\nAus welcher dieser Kategorien soll das Wort deiner Herausforderung stammen?\n")

        print("\nDas sind die Möglichkeiten, die dir zur Verfügung stehen:"
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
        secret_word = funcs.select_word(RPG_assets.animals)
    elif second_choice == 2:
        secret_word = funcs.select_word(RPG_assets.cities)
    elif second_choice == 3:
        secret_word = funcs.select_word(RPG_assets.food)
    elif second_choice == 4:
        secret_word = funcs.select_word(RPG_assets.presidents)
    elif second_choice == 5:
        secret_word = funcs.select_word(RPG_assets.cartoon_characters)
    elif second_choice == 6:
        secret_word = funcs.select_word(RPG_assets.hard_words)
    elif second_choice == 7:
        secret_word = funcs.select_word(RPG_assets.animals_german)
        print("\n-----------"
              "\nah.... deutsche Tiere... jaja, guten Tag Herr Osterhase."
              "\n----------")
    else:
        secret_word = "errorviernullvier"

    # testing
    # print(secret_word)
    if is_english:
        print("\n---------------------------")
        print("Very well, let it BEGIN!")
        print("---------------------------\n")
    else:
        print("\n---------------------------")
        print("Nun gut, möge deine Folter beginnen.")
        print("---------------------------\n")

    # used for controlling who gets to play / which part of the code is used
    who_plays: str = "Player"

else:  # The route of challenging with a word
    if is_english:
        print("\n--------------------------")
        print("YOU DARE TO CHALLENGE ME?")
        print("----------------------------\n")

        print('I will use my infinitely finite knowledge of the world to cause your destruction.\n'
              'Although I could crush you, I want to give you a chance... to play with my prey\n'
              'Would you like me to go easier on you?\n')

        print("   1. Yes, please. I am still confused! (easy)\n"
              "   2. I do not want your pity, but I do want a chance. medium\n"
              "\n   3. Give me the best that you got. You will be my prey.\n")

        print("\n1 , 2 or 3\n")
    else:
        print("\n--------------------------")
        print("DU WAGST ES, MICH HERAUSZUFORDERN?")
        print("----------------------------")

        print("\nIch werde mein unendlich endliches Wissen gegen dich verwenden, um dein Untergang hervorzurufen.\n"
              "Obwohl ich dich zerstören könnte mit dem Schnips meines Fingers, mmöchte ich dir eine Chance geben...\n"
              "... damit es ür mich noch Spaß macht...\n")

        print("   1. Ja, bitte. Ich bin immer noch verwirrt! (leicht)\n"
              "   2. Ich möchte dein Mitleid nicht, aber ich möchte eine Chance. (mittel)\n"
              
              "\n    3. Geb mir das Beste was du hast. ICH werde dein Untergang sein. (schweeer)\n")

        print("1, 2 oder 3")

    # used for controlling who gets to play / which part of the code is used
    who_plays = "NPC"

    strategy_value = funcs.give_me_a_value_inbetween(0, 3, is_english, False)

    if strategy_value == 3:
        print("")

        # asks if the user wants to use an in-build dictionary for the computer or if he
        # has provided an own one in the DICTIONARY folder
        # if he has not, go to ask about language:

        own_dictionary = 0

        print("-----\n")
        if is_english:
            print("Tell me, have you put a dictionary for me into my DICTIONARY box? \n")
            print("1.Yes 2.No\n")
        else:
            print("Sag mir, hast du ein Wörterbuch in meine Wörterbuch-Kiste getan? \n")
            print("1.Ja 2.Nein\n")

        lang_value = funcs.give_me_a_value_inbetween(0, 2, is_english, False)

        if own_dictionary == 2:
            print("--------------------------------------------------")
            if is_english:
                print("If you fly high, you fall deep, foolish Ikarus.\n")
                print("I am a villain, and yet I like to play fair. Which language will you write your "
                      "word in? This is my hellish landscape, so these are my rules:\n"
                      "english (1) or german (2)")
            else:
                print("Wenn du hoch fliegst, fällst du tief, törichter Ikarus.\n")
                print("Ich bin ein Bösewicht, aber ich spiele gerne fair. In welcher Sprache wirst du dein Wort schreiben? "
                      "Dies ist meine höllische Landschaft, also gelten meine Regeln:\n"
                      "Englisch (1) oder Deutsch (2)")

            lang_value = funcs.give_me_a_value_inbetween(0, 2, is_english, False)

            if lang_value == 2:
                hard_mode_lang = "german"
            else:
                hard_mode_lang = "english"
        else:
            # TODO build display of files in dir DICTIONARIES that are choosen by variable input,
            # maybe use hard_mode_lang for that?

    print("--------------------------------")
    challenge_word = funcs.user_input_word(is_english)
    secret_word = challenge_word.lower()

    if is_english:
        print("\n---------------------------")
        print("Very well, let it BEGIN!")
        print("---------------------------\n")
    else:
        print("\n---------------------------")
        print("Nun gut, möge deine Folter beginnen.")
        print("---------------------------\n")

# ------------------------------------------------------------
# THE GAME
# ------------------------------------------------------------


# The Player is in charge:

length_of_secret_word = int(len(funcs.get_unique_letters(secret_word)))

if who_plays == "Player":

    if is_english:
        print("The letter you wish to guess has {} letter´s... do with this Information what you like.\n".format(
            len(secret_word)))
    else:
        print("Der gesuchte Buchstabe hat {} Buchstaben... mache mit dieser Information, was du willst.\n".format(
            len(secret_word)))

    while remaining_attempts > 0 and len(guessed_letters) < length_of_secret_word:
        # the while-loop runs while the attempts haven't run out and the player hasn't won

        guess = funcs.guess_player_letter(is_english)  # player takes a guess

        guess_in_secret_word = funcs.is_guess_in_secret_word(guess, secret_word)
        # gives out a True or False value which we store in the variable and use in the following if statements

        if guess_in_secret_word:
            if guess in guessed_letters:
                if is_english:
                    print("\nYou have already guessed the letter {}\n".format(guess))
                else:
                    print("\nDu hast bereits den Buchstaben {} geraten.\n".format(guess))
            else:
                if is_english:
                    print("\nDamn. You have been right! The letter {} is part of the secret word\n".format(guess))
                else:
                    print("\nVerdammt. Du hast recht! Der Buchstabe {} ist Teil des geheimen Wortes\n".format(guess))
                print(funcs.select_word(RPG_assets.point_player))
                guessed_letters += guess
        else:
            if is_english:
                print("\nNo! The letter {} is not part of the secret word\n".format(guess))
            else:
                print("\nNein! Der Buchstabe {} ist nicht Teil des geheimen Wortes\n".format(guess))

            print(funcs.select_word(RPG_assets.point_computer))
            remaining_attempts -= 1

        print(funcs.get_hangman_stage(remaining_attempts))
        funcs.pri_secret_word(secret_word, guessed_letters)

        if is_english:
            print("\n You can make {} more mistakes... I would say be careful, but I hope you lose.\n"
                  .format(remaining_attempts))
        else:
            print("\nDu hast noch {} Fehler übrig... Ich würde sagen, sei vorsichtig, "
                  "aber ich hoffe, dass du verlierst.\n".format(remaining_attempts))

    if len(guessed_letters) == len(funcs.get_unique_letters(secret_word)):
        funcs.games_callout("Player", is_english)
    else:
        funcs.games_callout("NPC", is_english)

# The Computer is in charge of guessing: ---------------------------------------------------

if who_plays == "NPC":

    if strategy_value == 3:
        # here the version for the high-strategy computer-way, seperated for better overview

        # implemented variable outside of loop, so it doesn't load each time
        dict_before_slice = funcs.open_dictionary(hard_mode_lang)
        sliced_dict = funcs.slice_dict(dict_before_slice, hard_mode_lang, is_english, secret_word)
        remove_letters = []

        while remaining_attempts > 0 and len(guessed_letters) < length_of_secret_word:
            # the while-loop runs while the attempts haven't run out and the computer hasn't won

            empty_solv_dict = funcs.letter_frequency_structure_maker(secret_word, RPG_assets.alphabet)

            # creates a dict where frequency of elements at letter positions
            # are measured for remaining words in sliced_dict
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
                        print("\nI have already guessed this letter '{}'... fool me and my old mind\n".format(guess))
                        print("Someone contact the matrix-creator please... I dont feel so good repeating myself.\n")
                    else:
                        print("\nIch habe diesen Buchstaben '{}' bereits geraten... "
                              "täusche mich nicht und meinen alten Verstand.\n".format(guess))
                        print("Jemand kontaktiere bitte den Matrix-Schöpfer..."
                              "Ich fühle mich nicht gut dabei, mich zu wiederholen.\n")
                    print(funcs.get_hangman_stage(remaining_attempts))
                    guessed_letters.append(guess)
                    funcs.pri_secret_word(secret_word, guessed_letters)

                else:  # meaning that the guess is in secret word, but hasn't been guessed yet
                    if is_english:
                        print("\nI have been right! The letter {} is part of your secret filthy word\n".format(guess))
                    else:
                        print("\nIch habe recht gehabt! Der Buchstabe {} ist "
                              "Teil deines geheimen Wortes.\n".format(guess))
                    print(funcs.select_word(RPG_assets.point_computer))
                    print(funcs.get_hangman_stage(remaining_attempts))
                    guessed_letters.append(guess)
                    funcs.pri_secret_word(secret_word, guessed_letters)
                    # creates list that is used in understanding where a known element is in the secret word
                    half_hidden_word_list = funcs.format_the_hidden_word(secret_word, guessed_letters)
                    # the just created list and its opposite are used in eliminating
                    # the words that contradict known positional letters
                    sliced_dict = funcs.letter_sniper(solving_dict, sliced_dict, half_hidden_word_list)

            else:  # meaning that the letter is not part of the word.
                if is_english:
                    print("\n Nooooo.... The letter {} is not part of your word...\n".format(guess))
                else:
                    "\n Nein! Der Buchstabe {} ist nicht Teil deines Wortes ...\n".format(guess)
                print(funcs.select_word(RPG_assets.point_player))
                remaining_attempts -= 1
                remove_letters.append(guess)
                sliced_dict = funcs.thinner_the_sliced_dict(sliced_dict, solving_dict, remove_letters)
                print(funcs.get_hangman_stage(remaining_attempts))
                funcs.pri_secret_word(secret_word, guessed_letters)

            # prevents duplicates in the guessed letters list,
            # in case smth goes wrong, as to not create more systematic bugs
            guessed_letters = funcs.remove_duplicates_in_list(guessed_letters)

            if remaining_attempts > 0:
                # a simple enter anything input that changes nothing, but creates a simple break for
                # the player, so that the computer doesn't run through the skript too quickly.
                # In case the user likes to read the canon of the Executioner.
                if is_english:
                    print("\n I have another {} attempts to go.\n".format(remaining_attempts))
                    input("Press Enter to continue...")
                else:
                    print("\n Ich habe noch {} Versuche übrig.\n".format(remaining_attempts))
                    input("Drücke Enter, um fortzufahren...")
            else:
                if is_english:
                    print("Jeff, with last breath: Why....Please... u should have use a harder woooooordddd.....")
                else:
                    print("Jeff, mit seinem letzten Atemzug:\n"
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
                        print("\nI have already guessed this letter '{}'... fool me and my old mind\n".format(guess))
                    else:
                        print("\nIch habe diesen Buchstaben '{}' bereits geraten... "
                              "täusche mich nicht und meinen alten Verstand.\n".format(guess))
                else:
                    if is_english:
                        print("\nI have been right! The letter {} is part of your secret filthy word\n".format(guess))
                    else:
                        print("\nIch habe recht gehabt! Der Buchstabe {} ist "
                              "Teil deines geheimen Wortes.\n".format(guess))
                    print(funcs.select_word(RPG_assets.point_computer))
                    guessed_letters += guess
            else:
                if is_english:
                    print("\n Nooooo.... The letter {} is not part of your word...\n".format(guess))
                else:
                    "\n Nein! Der Buchstabe {} ist nicht Teil deines Wortes ...\n".format(guess)
                print(funcs.select_word(RPG_assets.point_player))
                remaining_attempts -= 1

            print(funcs.get_hangman_stage(remaining_attempts))
            funcs.pri_secret_word(secret_word, guessed_letters)

            if remaining_attempts >= 1:
                # a simple enter anything input that changes nothing, but creates a simple break for
                # the player, so that the computer doesn't run through the skript too quickly.
                # In case the user likes to read the canon of the Executioner.
                if is_english:
                    print("\n I have another {} attempts to go.\n".format(remaining_attempts))
                    input("Press Enter to continue...")
                else:
                    print("\n Ich habe noch {} Versuche übrig.\n".format(remaining_attempts))
                    input("Drücke Enter, um fortzufahren...")

    if len(guessed_letters) == len(funcs.get_unique_letters(secret_word)):
        # Function that celebrates the victory of whoever has won
        funcs.games_callout("NPC", is_english)
    else:
        funcs.games_callout("Player", is_english)

if is_english:
    print("The secret word was {}\n".format(secret_word))
    print("------------------------------------------\n")

    print("*the executioner drags jeff behind him, neither dead or alive, "
          "trapped in a eternal state of being used as a joke in a video game*\n")

    print("------------------------------------------\n")

    print("Narrator: Would you like to face him again? I can always send you back in time\n")
    print("1. Go again\n"
          "2. End this, please!\n")
else:
    print("Das geheime Wort war {}\n".format(secret_word))

    print("------------------------------------------\n")

    print("der Henker zieht Jeff hinter sich her, weder tot noch lebendig, gefangen in einem ewigen Zustand, "
          "als Witz in einem Videospiel verwendet zu werden\n")

    print("------------------------------------------\n")

    print("Erzähler: Möchtest du dich ihm erneut stellen? Ich kann dich jederzeit zurück "
          "in die Vergangenheit schicken.\n")
    print("1. Nochmal spielen\n"
          "2. Beende dies bitte!\n")

restart = funcs.give_me_a_value_inbetween(0, 2, is_english, False)

if restart == "1":
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
elif restart == "2":
    print("\nThe matrix will be closed...")
    sys.exit(0)
