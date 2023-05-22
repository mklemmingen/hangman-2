import random  # used to choose randomly out of lists, see "https://docs.python.org/3/library/random.html"
import time  # used to simulate delays of the npc while choosing a letter and add user-friendliness
import text_assets
import os  # used to exit and reload program at the end and to list files in dict dictionary

# used for colouring and formatting the output
from rich.console import Console

console = Console()


# --------------------------
# some rules for certain words that should be treated specifically in rich
def give_separators():
    # prints out separators
    console.print("\n-----------------------------------------------------------------------\n", style="wheat1",
                  justify="left")


def clean_window():
    # removes all words from the pygame window
    console.clear()
    console.print("-------------- hanging man - the game of dictionaries -----------------\n", style="bold #504a56",
                  justify="left")
    # similar to os.system("clear")


# --------------------------------------------------
# Select the word function


def select_word(func_words: list) -> str:
    # function to select a string from a list.
    # it uses the random module to help with the random word pick
    return random.choice(func_words).lower()


# test to see if a random word is selected from the lists
# console.print(select_word(presidents), , justify="center")

# -----------------------------------------------------
# function to check if users' challenge word has a number in it, uses regex to include "-"
# function is used when challenge_word is created after junction of first_choice

def are_there_numbers(func_word: str) -> bool:
    return any(char.isdigit() for char in func_word)


# -----------------------------------------------------
# def function to use for the underscores as "unknown" letters

def pri_secret_word(word: str, gues_letters: list):
    # this is used to console.print the missing letters with an _ and the known letters fitting
    # inspiration found in: https://codefather.tech/blog/hangman-game-python/
    # "end" used so the console.print function writes in one line
    for letter in word:
        if letter in gues_letters:
            console.print(" {} ".format(letter), end="")
        else:
            console.print(" _ ", end="")
    console.print("\n")


# ------------------------------------------
# used repeating
def give_me_a_value_inbetween(value1: int, value2: int, language_eng: bool, start_of_game: bool) -> int:
    """

    :rtype: object
    """
    # Function for choosing a letter between two values
    erg = -1
    console.bell()
    while erg <= value1 or erg > value2:
        # A while-loop is used to stop the user from ending the game with anything not allowed,
        # except is used to prevent errors
        try:
            console.bell()
            if start_of_game:
                give_separators()
                erg = int(input("Enter your choices number ... Geb die Nummer deiner Entscheidung ein: "))
                console.print("", justify="left")
                start_of_game = False
            elif language_eng:
                # User is presented with the choice to choose between playing the game or choosing the computer word
                give_separators()
                erg = int(input("\nEnter your choices number: "))
                console.print("", justify="left")
            else:
                # User is presented with the choice to choose between playing the game or choosing the computer word
                give_separators()
                erg = int(input("\nGebe die Zahl deiner Entscheidung ein: "))
                console.print("", justify="left")
        except ValueError or TypeError:
            if language_eng:
                console.print("That is not an option... and you know it!", justify="left")
            else:
                console.print("Das war keine Möglichkeit! Nochmal!", justify="left")
    clean_window()
    return erg


# -----------------------------------------
# these functions are either for the player to guess letters or for the
# computer to do so with different difficulty settings

def guess_player_letter(language_eng: bool) -> str:
    # reoccurring function for guessing a letter as the PLAYER
    while True:
        give_separators()
        if language_eng:
            console.print(select_word(text_assets.choose), end="", style="#db6825")
        else:
            console.print(select_word(text_assets.choose_german), end="", style="#db6825")
        guess_func = str(input(":  "))
        give_separators()
        if len(guess_func) > 1 or not guess_func.isalpha():
            if language_eng:
                console.print("\nYou fool of a tuck, only single letters are to be guessed. Do you want to break"
                              "the simulation?... go again... "
                              "this time remember the rules of only one letter at a time!", justify="left")
            else:
                console.print("\nDu Möchtegern-Hobbit, es darf nur ein einzelner Buchstabe geraten werden.\n "
                              "Möchtest du die Simulation zerstören? Versuche es erneut und denke daran, "
                              "dass nur ein Buchstabe auf einmal geraten werden darf!", justify="left")
        else:
            break
    clean_window()
    return guess_func.lower()


def guess_computer_letter(language_eng: bool, alphabet: list) -> str:
    # reoccurring function for guessing a letter as the NPC (Executioner) does
    in_func_guess: str = select_word(alphabet)
    if language_eng:
        console.print("\n*The [bold magenta]Executioner[/bold magenta] looks into the distance... thinking hard...*",
                      style="italic",
                      justify="left")
    else:
        console.print("\nDer Henker schaut nachdenklich in die Ferne...", style="italic",
                      justify="left")
    time.sleep(2)
    give_separators()
    if language_eng:
        console.print(select_word(text_assets.npc_inner_thoughts), style="#19700a", justify="left")
    else:
        console.print(select_word(text_assets.npc_inner_thoughts_german), style="#19700a", justify="left")
    give_separators()
    time.sleep(2)
    return in_func_guess


def guess_computer_letters_strategy(language_eng: bool, gues_let_func: list) -> str:
    # this reoccurring functions uses a simple vowel-first strategy to solve the user input words
    # https://pynative.com/python-weighted-random-choices-with-probability/
    # used for inspiration for guesses with probability.Links accessed on the 02.04.23
    # used for probabilities: https://www.wordcheats.com/blog/most-used-letters-in-english

    while True:
        in_function_guess = random.choices(text_assets.standard_alphabet,
                                           weights=(8.4966, 2.0720, 4.5388, 3.3844, 11.1607,
                                                    1.8121, 2.4705, 3.0034, 7.5448, 0.1965,
                                                    1.1016, 5.4893, 3.0129, 6.6544, 7.1635,
                                                    3.1671, 0.1962, 7.5809, 5.7351, 6.9509,
                                                    3.6308, 1.0074, 1.2899, 0.2902, 1.7779,
                                                    0.2722), k=1)
        if in_function_guess in gues_let_func:
            continue
        if in_function_guess not in gues_let_func:
            break

    console.print("\n*The [bold magenta]Executioner[/bold magenta] looks into the distance... thinking real hard...*",
                  justify="left")
    time.sleep(2)
    give_separators()
    if language_eng:
        console.print(select_word(text_assets.npc_inner_thoughts), style="#19700a", justify="left")
    else:
        console.print(select_word(text_assets.npc_inner_thoughts_german), style="#19700a", justify="left")
    give_separators()
    time.sleep(2)
    in_function_guess = str(in_function_guess[0])
    return in_function_guess


# ----------------------------------------------

def high_strategy_dictionary(pydict: dict, gues_let: list, rem_let: list, alphabet: list, language_eng: bool) -> str:
    console.print("\n*The [bold magenta]Executioner[/bold magenta] looks into the distance... thinking hard...*",
                  justify="left")
    time.sleep(2)
    give_separators()
    if language_eng:
        console.print(select_word(text_assets.npc_inner_thoughts), justify="left")
    else:
        console.print(select_word(text_assets.npc_inner_thoughts_german), justify="left")
    give_separators()
    time.sleep(2)

    # Creating a skeleton dict without positional arguments.
    # Add onto the length of lists of a corresponding key:value-pairs
    # The biggest elements value gets chosen to be the high_guess
    empty_in_func_dict: dict = {}
    for letter in alphabet:
        empty_in_func_dict[letter] = 0

    length_dict: dict = {}

    # merged list of correctly and wrongly guessed letters
    letter_list = list(set(gues_let + rem_let))

    # if the merged list of letters has at least one in it, we remove it by leaving it out of a new list
    if len(letter_list) >= 1:
        for key, lone_letter in empty_in_func_dict.items():
            if key in letter_list:
                continue
            else:
                length_dict[key] = empty_in_func_dict[key]
    elif len(letter_list) == 0:
        for key, lone_letter in empty_in_func_dict.items():
            length_dict[key] = empty_in_func_dict[key]

    for key, value in pydict.items():
        for key2, value2 in length_dict.items():
            if key.startswith(key2):
                length_dict[key2] = length_dict[key2] + (len(value))

    # gets the key with the highest value
    # as seen in:
    # https://stackoverflow.com/questions/20453674/how-to-find-the-largest-value-in-a-dictionary-by-comparing-values
    # Access: 07.05.23
    # makes use of the max function in pair with the get function to use the value
    # specifically of the key:value-pair

    highest_value_elem: str = max(length_dict, key=length_dict.get)

    return highest_value_elem  # guess as char


def iterate_dict_to_sol_dict(real_dict: list, ghostly_solv_dict: dict) -> dict:
    # I take the "sliced by len(secretword)"-dictionary "short_dict" and iterate over each of its strings.
    # I want to add, at each element, the index of its current word to the value list of
    # the current element corresponding an empty dict key.
    # the empty dict was created using letter_frequency_struct_maker,
    # and only holds elements up to the length of the secret word,
    # similar to how sliced dict only holds words as a list that are as long as secret word

    # If it finds the letter "t" at position "4", put the index of the word in the list into a dictionary
    # value where they key corresponds to "t4".
    # The solv_struct starts at "a0".
    # So the word from the
    # example would have to be something like "aaaataa."

    # in the wise words of yoda in a theme park: a lot of loops these are
    for index, word in enumerate(real_dict):
        try:
            # loops through a list (real sliced dictionary)
            for position, letter in enumerate(word):
                # loops through all letters at each position and adds
                # onto values of corr. key:value-pairs
                ghostly_solv_dict["{0}{1}".format(letter, position)].append(index)
                # Vorbild: opposite_keys.append("a{0}".format(number))
        except KeyError:
            # to over-go errors produced by a letter not being existent any more
            continue

    return ghostly_solv_dict  # full solving_dict


def thinner_the_sliced_dict(eunuch_dict: list, sol_dict: dict, already_guessed_let: list) -> list:
    # each time remove_letters gets a new one, which is letters not in the secret word
    # this goes and looks at solving_dict,
    # gets their index from values,
    # removes those indexes from sliced_dct(here eunuch_dict),
    # and gives back a better sliced_dict

    # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
    # https://stackoverflow.com/questions/11303225/how-to-remove-multiple-indexes-from-a-list-at-the-same-time

    # in code: thinner_the_sliced_dict(sliced_dict, solving_dict, guessed_letters)

    remove_index_list = []

    # Try 1
    # for i, j in enumerate(sol_dict.keys()):
    #    if j in already_guessed_let:
    #        for x in sol_dict.keys([i]):
    #            remove_index_list = remove_index_list.append((sol_dict.values([i])))

    # Try 2
    # for i in range(sol_dict.keys()):
    #    if re.search("b/d", sol_dict.keys([i])) in already_guessed_let:
    #        for x in sol_dict.keys([i]):
    #            remove_index_list = remove_index_list.append(sol_dict.keys([i]).values())

    # Try 3
    # (Source: https://stackoverflow.com/questions/35786279/adding-dictionary-values-to-a-list, Access: 07.05.23)
    # for key, value in sol_dict.items():
    #    for a letter in already_guessed_let:
    #        if key.startswith(letter):
    #            remove_index_list.append(sol_dict[key])

    # Try 4
    for key, value in sol_dict.items():
        for letter in already_guessed_let:
            if key.startswith(letter):
                remove_index_list.append(value)

    # function that cuts it all together
    super_sliced_dict = slice_shine_and_burn(remove_index_list, eunuch_dict)

    return super_sliced_dict  # sliced_dict


def format_the_hidden_word(sec_word: str, gues_letters: list, alphabet: list) -> list:
    # coming from the output the user can see like "a_s_h", and make conclusions
    # based on the fact that certain words cannot be included,
    # this creates a list that holds all keys that are not possible any more
    # Question:
    # create lists of both the direct values and opposite values
    non_opposite_keys = []
    opposite_keys = []

    # puts stuff into the non_opposite_key-list
    for position, letter in enumerate(sec_word):
        if letter in gues_letters:
            for element in alphabet:
                non_opposite_keys.append("{0}{1}".format(letter, position))
                # creates a list of positional keys
                number = str(position)
                opposite_keys.append("{0}{1}".format(element, number))

    # takes out the known keys, so their index values persist
    for key in non_opposite_keys:
        try:
            opposite_keys.remove(key)
        except ValueError:
            continue

    return opposite_keys  # list of keys which index should be deleted


def letter_sniper(sol_dict: dict, real_dict_list: list, remove_key_list: list) -> list:
    # This checks a specially created list of values created from the info one can get from
    # correctly guessed letters. Meaning that when a_s_h is displayed, the list used here
    # contains elements that are in opposition, like all keys not a0, but at position 0.

    remove_index_list = []

    # Goes through the sol_dict and gets the keys, then for each key iterates through the remove_key_list
    # and checks if they are the same. If they are the same, it adds the sol_dict keys values, which are index values,
    # to the remove_index_list

    for key, value in sol_dict.items():
        for remove_key in remove_key_list:
            if key == remove_key:
                remove_index_list.append(value)

    super_sliced_dict = slice_shine_and_burn(remove_index_list, real_dict_list)

    return super_sliced_dict


def slice_shine_and_burn(list_to_burn: list, real_dict_list: list) -> list:
    # using list comprehension to break up the list in list
    popped_remove_index_list = [item for sublist in list_to_burn for item in sublist]

    # sort and reverse
    list_sort_and_turned = sorted(popped_remove_index_list, reverse=True)

    # remove duplicates by creating a new list
    filtered_removal_list = list()
    for item in list_sort_and_turned:
        if item not in filtered_removal_list:
            filtered_removal_list.append(item)

    # delete from the list
    for index in filtered_removal_list:
        try:
            del real_dict_list[index]
        except IndexError:
            # the code runs into endless efficiency... i guess, couldn't find a solution here
            continue

    return real_dict_list  # new sliced_dict


def remove_duplicates_in_list(func_list: list) -> list:
    # remove duplicates by creating a new list
    filtered_removal_list = list()
    for item in func_list:
        if item not in filtered_removal_list:
            filtered_removal_list.append(item)

    return filtered_removal_list


def slice_dict(language: str, language_eng: bool, secret_word: str, value_if_own_dict: int,
               files_dict: list, value_which_dictionary: int) -> list:
    global my_dict, chosen_file, full_dict, in_built, output_in_func_dict

    length_of_secret_word = len(secret_word)

    skip_change = False
    change_me = False
    # variables: files_in_dir, value_which_dictionary
    if value_if_own_dict == 1:
        # check if file-names have "sorted" inside
        chosen_file = files_dict[value_which_dictionary]

        for file in files_dict:
            if "changed" in file:
                skip_change = True

        chosen_file = files_dict[value_which_dictionary]
        if skip_change:  # if the file has changed in name and is thereby already changed
            full_dict = open(f"DICTIONARIES/user_input_dicts/{chosen_file}", "r")
        else:  # if it does not have sorted in it and has to be sorted
            # open dictionary with written
            # dict is the one chosen with value_which_dictionary
            my_dict = open(f"DICTIONARIES/user_input_dicts/{chosen_file}", "r+")
            change_me = True
    elif language == "english":
        # make use of already known intervals in the english wordlist
        output_in_func_dict = slice_the_english(language_eng, length_of_secret_word)
    else:
        # open files to my_dict depending on language in hard_mode_lang
        change_me = True
        in_built = True
        if language == "croatian":
            my_dict = open(f"DICTIONARIES/in-build-dictionaries/croatian.txt", "r")
        elif language == "german":
            my_dict = my_dict = open(f"DICTIONARIES/in-build-dictionaries/german.txt", "r")
        elif language == "czech":
            my_dict = open(f"DICTIONARIES/in-build-dictionaries/czech.txt", "r")
        elif language == "danish":
            my_dict = open(f"DICTIONARIES/in-build-dictionaries/danish.txt", "r")
        elif language == "dutch":
            my_dict = open(f"DICTIONARIES/in-build-dictionaries/dutch.txt", "r")
        elif language == "french":
            my_dict = open(f"DICTIONARIES/in-build-dictionaries/french.txt", "r")
        elif language == "georgian":
            my_dict = open(f"DICTIONARIES/in-build-dictionaries/georgian.txt", "r")
        elif language == "italian":
            my_dict = open(f"DICTIONARIES/in-build-dictionaries/italian.txt", "r")
        elif language == "maltese":
            my_dict = open(f"DICTIONARIES/in-build-dictionaries/maltese_words.txt", "r")
        elif language == "norwegian":
            my_dict = open(f"DICTIONARIES/in-build-dictionaries/norwegian.txt", "r")
        elif language == "polish":
            my_dict = open(f"DICTIONARIES/in-build-dictionaries/polish.txt", "r")
        elif language == "portuguese":
            my_dict = open(f"DICTIONARIES/in-build-dictionaries/portuguese.txt", "r")
        elif language == "serbian":
            my_dict = open(f"DICTIONARIES/in-build-dictionaries/serbian.txt", "r")
        elif language == "spanish":
            my_dict = open(f"DICTIONARIES/in-build-dictionaries/spanish.txt", "r")
        elif language == "swedish":
            my_dict = open(f"DICTIONARIES/in-build-dictionaries/swedish.txt", "r")
        elif language == "turkish":
            my_dict = open(f"DICTIONARIES/in-build-dictionaries/turkish.txt", "r")
        elif language == "ukranian":
            my_dict = open(f"DICTIONARIES/in-build-dictionaries/ukrainian.txt", "r")
        elif language == "hebrew":
            my_dict = open(f"DICTIONARIES/in-build-dictionaries/hebrew.txt", "r")
        elif language == "arabic":
            my_dict = open(f"DICTIONARIES/in-build-dictionaries/arabic.txt", "r")
        elif language == "english medical terms":
            my_dict = open(f"DICTIONARIES/in-build-dictionaries/medical-wordlist.txt", "r")
        else:  # if all fails
            my_dict = slice_the_english(language_eng, length_of_secret_word)

    # if it hasn't skipped the change or if we use an in_build_dictionary:
    if change_me:
        # reading the files
        data = my_dict.read()

        # replacing an end splitting the text
        # when newline ('\n') is seen.
        data_dict_list = data.split("\n")

        if not in_built:
            # save into new dict and close dictionary
            for word in data_dict_list:
                my_dict.write(str(word) + "\n")
            my_dict.close()
            os.rename(f"DICTIONARIES/{chosen_file}", f"DICTIONARIES/{chosen_file}_changed")

        # turn every element of dictionary into alpha-mode
        # slices/chooses only words with the right length, does so with all before selected lists.
        # choose words with len(word) = len(secret_word)
        in_func_list = []
        for word in data_dict_list:
            if len(word) == len(secret_word):
                low_word = word.lower()
                in_func_list.append(low_word)
        output_in_func_dict = in_func_list

    return output_in_func_dict


def slice_the_english(language_eng: bool, length_of_secret_word: int) -> list:
    opened_dict = open("DICTIONARIES/in-build-dictionaries/english.txt", "r")

    # reading the files
    data = opened_dict.read()

    # replacing an end splitting the text
    # when newline ('\n') is seen.
    fun_dict = data.split("\n")

    global output_dict
    if length_of_secret_word <= 10:
        if length_of_secret_word == 1:
            output_dict = fun_dict[0:25]
        elif length_of_secret_word == 2:
            output_dict = fun_dict[26:452]
        elif length_of_secret_word == 3:
            output_dict = fun_dict[453:2582]
        elif length_of_secret_word == 4:
            output_dict = fun_dict[2583:9768]
        elif length_of_secret_word == 5:
            output_dict = fun_dict[9769:25688]
        elif length_of_secret_word == 6:
            output_dict = fun_dict[25689:55562]
        elif length_of_secret_word == 7:
            output_dict = fun_dict[55563:97560]
        elif length_of_secret_word == 8:
            output_dict = fun_dict[97561:149187]
        elif length_of_secret_word == 9:
            output_dict = fun_dict[149188:202589]
        elif length_of_secret_word == 10:
            output_dict = fun_dict[202590:248462]
    elif length_of_secret_word <= 20:
        if length_of_secret_word == 11:
            output_dict = fun_dict[248463:286001]
        elif length_of_secret_word == 12:
            output_dict = fun_dict[286001:315125]
        elif length_of_secret_word == 13:
            output_dict = fun_dict[315126:336069]
        elif length_of_secret_word == 14:
            output_dict = fun_dict[336070:350218]
        elif length_of_secret_word == 15:
            output_dict = fun_dict[350219:359064]
        elif length_of_secret_word == 16:
            output_dict = fun_dict[359065:364247]
        elif length_of_secret_word == 17:
            output_dict = fun_dict[364248:367214]
        elif length_of_secret_word == 18:
            output_dict = fun_dict[367215:368684]
        elif length_of_secret_word == 19:
            output_dict = fun_dict[368685:369444]
        elif length_of_secret_word == 20:
            output_dict = fun_dict[369445:369803]
    else:
        if length_of_secret_word == 21:
            output_dict = fun_dict[369804:369971]
        elif length_of_secret_word == 22:
            output_dict = fun_dict[369972:370046]
        elif length_of_secret_word == 23:
            output_dict = fun_dict[370046:370077]
        elif length_of_secret_word == 24:
            output_dict = fun_dict[370078:370088]
        elif length_of_secret_word == 25:
            output_dict = fun_dict[370089:370096]
        elif length_of_secret_word == 26:
            output_dict = fun_dict
            if language_eng:
                console.print("mhhh, I do not know any words with 26 letters...", justify="left")
                console.print("I will try anyway, but I will take some more time, mortal.", justify="left")
                console.print("I hope you have some more left... muahahah\n", justify="left")
            else:
                console.print("Hmm, ich kenne keine Wörter mit 26 Buchstaben...", justify="left")
                console.print("Dennoch werde ich es versuchen, aber ich werde mir etwas mehr Zeit nehmen, Sterblicher.",
                              justify="left")
                console.print("Ich hoffe, du hast noch etwas übrig... Muahahaha\n",
                              justify="left")
        elif length_of_secret_word == 27:
            output_dict = fun_dict[370097:370099]
        elif length_of_secret_word == 28:
            output_dict = fun_dict[370100:370101]
        elif length_of_secret_word == 29:
            output_dict = fun_dict[370102:370104]
        elif length_of_secret_word == 30:
            output_dict = fun_dict
            if language_eng:
                console.print("mhhh, I do not know any words with 30 letters...", justify="left")
                console.print("I will try anyway, but I will take some more time, mortal.", justify="left")
                console.print("I hope you have some more left... muahahah\n", justify="left")
            else:
                console.print("Hmm, ich kenne keine Wörter mit 30 Buchstaben...", justify="left")
                console.print("Dennoch werde ich es versuchen, aber ich werde mir etwas mehr Zeit nehmen, Sterblicher.",
                              justify="left")
                console.print("Ich hoffe, du hast noch etwas übrig... Muahahaha\n", justify="left")
        elif length_of_secret_word == 31:
            output_dict = fun_dict[370105:370105]
        else:
            if language_eng:
                console.print("\nthat's a very long word... are you sure it exists?", justify="left")
                console.print("\nI will try anyway, cheat.", justify="left")
                console.print("\nIf you button-smashed, I will haunt your dreams for eternity and make sure that "
                              "in the after-life you won`t have the chance to dream.... just kidding... unless...",
                              justify="left")
            else:
                console.print("\nDas ist ein sehr langes Wort... bist du sicher, dass es existiert?",
                              justify="left")
                console.print("\nIch werde es trotzdem versuchen, Schummler.", justify="left")
                console.print("\nWenn du wild auf den Tasten hermeneutical hast,\n"
                              "werde ich dich für die Ewigkeit heimsuchen und sicherstellen,\n"
                              "dass du im Jenseits nicht träumen wirst... nur ein Scherz... oder auch nicht...",
                              justify="left")
            output_dict = fun_dict

    return output_dict


#          -------------------------------
def letter_frequency_structure_maker(sec_word_for_func: str, alph_in_func: list) -> dict:
    # creates an array of keys of the length of secret word with the other axis being the alphabet
    # since initializing 806 possible combinations would be unnecessary.
    # all the values of the arrays are listed with the index values of the corresponding words
    # starts at a0

    sec_le = len(sec_word_for_func)
    alp_le = len(alph_in_func)
    solvstruct = {}

    for i in range(sec_le):
        for j in range(alp_le):
            solvstruct["{}{}".format(alph_in_func[j], str(i))] = []

    return solvstruct


# -----------------------------------------

def is_guess_in_secret_word(guess_in_func: str, sec_word: str) -> bool:
    # function that checks if a letter is in secret word
    if guess_in_func in sec_word:
        return True
    else:
        return False


# ----------------------------------------

# function used to put the secret_word string into a set, so we can remove duplicates and iterate easy
def get_unique_letters(word: str) -> str:
    return "".join(set(word))


# -----------------------------------------

def user_input_word(language_eng: bool) -> str:
    # Function handles the user-input for the challenge_word

    # variable used for control while a statement
    global user_word
    good_enough_points = False

    while not good_enough_points:
        # while-loop breaks when the challenge_word is good enough
        if language_eng:
            user_word = str(input("\n... so be it... write your human word on this card and do not tell me: "))
        else:
            user_word = str(
                input("\n... so sei es... schreib dein menschliches Wort hier drauf und sag es mir nicht: "))
        # checking the challenge_word for anything bad
        # does it have numbers in it?
        # is challenge word actually multiple words with space between
        if " " not in user_word and not are_there_numbers(user_word):
            if len(user_word) > 0:
                good_enough_points = True
            else:
                if language_eng:
                    console.print("\n Narrator: Numbers??? Multiple words??? Separators?! "
                                  "Not in this game! Repeat, Repeat, Repeeeeat!", justify="left")
                else:
                    console.print("\n Narrator: Zahlen??? Mehrere Wörter??? Trennzeichen?! Nicht in diesem Spiel! "
                                  "Wiederholen, Wiederholen, Wiederholen!", justify="left")
        else:
            if language_eng:
                console.print("\n Narrator: Numbers??? Multiple words??? Separators?! Not in this game! "
                              "Repeat, Repeat, Repeeeeat!", justify="left")
            else:
                console.print("\n Narrator: Zahlen??? Mehrere Wörter??? Trennzeichen?! Nicht in diesem Spiel! "
                              "Wiederholen, Wiederholen, Wiederholen!", justify="left")
    return user_word


# ----------------------------------------

def games_callout(who_won: str, language_eng: bool):
    # function that gives out a statement according to who won - perspective player
    if who_won == "NPC":
        console.print(text_assets.npc_art_win, highlight=True, justify="left")
        console.print("", justify="left")
        time.sleep(2)
        give_separators()
        console.print(select_word(text_assets.npc_wins), justify="left")
        console.print("", justify="left")
        if language_eng:
            console.print(
                "Narrator: The Exorcist... or was it [bold magenta]Executioner[/bold magenta]?... has won! pity you!\n",
                justify="left")
        else:
            console.print("Narrator: Der Exorzist... oder war es der Henker?... hat gewonnen! Schade für dich!\n",
                          justify="left")
        give_separators()
    if who_won == "Player":
        give_separators()
        console.print(select_word(text_assets.player_wins), highlight=False, justify="left")
        console.print("", justify="left")
        if language_eng:
            console.print("Narrator: Wow! You have actually managed to win! good job you!\n", justify="left")
        else:
            console.print("Narrator: Wow! Du hast es tatsächlich geschafft zu gewinnen! Gut gemacht!\n", justify="left")
        console.print("", justify="left")
        console.print(text_assets.player_art_win, justify="left")
        console.print("", justify="left")
        give_separators()


# -----------------------------------------
# function for printing out a cool executioner
def let_it_begin_art():
    console.print(text_assets.executioner_game_start)


# -----------------------------------------
# Hangman stages as a function corresponding to the remaining_attempts
def get_hangman_stage(attempt_number: int):
    max_attempts = 6
    stages = ["""
        ------
        |    |
        |
        |
        |
        |
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |
        |
        |
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |    |
        |    |
        |
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |    |
        |    |
        |   /
        |
    ------------ 
    """, """
        ------
        |    |
        |    O
        |    |
        |    |
        |   / \\
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |  --|
        |    |
        |   / \\
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |  --|--
        |    |
        |   / \\
        |
    ------------
    """]
    return stages[max_attempts - attempt_number]


def files_in_dir(path: str) -> list:
    # function checks if there are any files in a directory
    # source 15.05.23: https://stackoverflow.com/questions/33463325/python-check-if-any-file-exists-in-a-given-directory
    return list(os.listdir(path))
