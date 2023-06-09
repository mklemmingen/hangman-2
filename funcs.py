import random  # used to choose randomly out of lists, see "https://docs.python.org/3/library/random.html"
import time  # used to simulate delays of the npc while choosing a letter and add user-friendliness
import os  # used to exit and reload program at the end and to list files in dict dictionary

# file of lists with sentences, words, alphabets and ascII art
import text_assets

# used for colouring and formatting the output
from rich.console import Console

console = Console()

# for use in the typewriter function to use as this scripts styles
system = "default"
narrator_talks = "italic #fc9b14"
executioner_talks = "bold #996633"
# bool value for highlight
no_highlights = False
highlights = True


# --------------------------
def typewriter(text, style: str, highlight: bool):
    """
    Function to print output with typewriter effect.
    This will print all the elements of the string one by one at a certain rate of an element per second.
    It uses a rich console print statement with console.print().

    modified FORK from pywriter, licence MIT, rights to: Jesse Amarquaye, package: pywrite
    https://github.com/amarquaye/pywriter/blob/master/pywriter/__init__.py

    :param text: The data you would like to print
    :param style: style parameters, see rich documentation
    :param highlight: Bool Value if it should be auto-highlighted
    :return: output of a stylised text to the rich console
    """
    rate: float = 0.02

    for i in range(len(text)):
        console.print(text[i], end="", style=style, highlight=highlight)
        time.sleep(rate)


# --------------------------
# some rules for certain words that should be treated specifically in rich
def give_separators():
    """
    prints out multiple separators.
    :return: output of some symbols to the rich console.
    """
    console.print("\n-----------------------------------------------------------------------\n", style="#739900",
                  )


def clean_window():
    """
    removes all text from the console window
    similar to os.system("clear")
    :return: a clear console window and some empty lines to make the game look better
    """
    console.clear()
    console.print("\n\n")


# --------------------------------------------------
# Select the word function

def select_word(func_words: list) -> str:
    """
    function to select a string from a list.
    it uses the random module to help with the random word pick.
    :param func_words: list of elements/strings, one gets selected.
    :return: element as string.
    """
    return random.choice(func_words)


def select_word_lower(func_words: list) -> str:
    """
    function to select a string from a list.
    it uses the random module to help with the random word pick.
    :param func_words: list of elements/strings, one gets selected.
    :return: element as all lower-letter string.
    """
    return random.choice(func_words).lower()


# test to see if a random word is selected from the lists
# console.print(select_word(presidents), , justify="center")

# -----------------------------------------------------

def are_there_numbers(func_word: str) -> bool:
    """
    # function to check if users' challenge word has a number in it, uses regex to include "-"
    # function is used when challenge_word is created after junction of first_choice
    :param func_word:
    :return:
    """
    return any(char.isdigit() for char in func_word)


# -----------------------------------------------------
# def function to use for the underscores as "unknown" letters

def pri_secret_word(word: str, gues_letters: list):
    """
    this is used to console.print the missing letters with an _ and the known letters fitting
    inspiration found in: https://codefather.tech/blog/hangman-game-python/
    "end" used so the console.print function writes in one line
    :param word:
    :param gues_letters:
    :return:
    """

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
    Function for choosing a letter between two values
    :param value1:
    :param value2:
    :param language_eng:
    :param start_of_game:
    :return:
    """
    erg = -1
    console.bell()
    while erg <= value1 or erg > value2:
        # A while-loop is used to stop the user from ending the game with anything not allowed,
        # except is used to prevent errors
        try:
            console.bell()
            if start_of_game:
                give_separators()
                console.print("--->  ", style="blink bold", end="")
                typewriter("Enter your choices number ... Geb die Nummer deiner Entscheidung ein: ",
                           system, no_highlights)
                erg = int(input())
                start_of_game = False
            elif language_eng:
                # User is presented with the choice to choose between playing the game or choosing the computer word
                give_separators()
                console.print("--->  ", style="blink bold", end="")
                typewriter("Enter your choices number: ",
                           system, no_highlights)
                erg = int(input())
            else:
                # User is presented with the choice to choose between playing the game or choosing the computer word
                give_separators()
                console.print("--->   ", end="", style="blink bold")
                typewriter("Gebe die Zahl deiner Entscheidung ein: ",
                           system, no_highlights)
                erg = int(input())
        except ValueError or TypeError:
            if language_eng:
                typewriter("That is not an option... and you know it!", narrator_talks, no_highlights)
            else:
                typewriter("Das war keine Möglichkeit! Nochmal!", narrator_talks, no_highlights)
    clean_window()
    return erg


# -----------------------------------------
# these functions are either for the player to guess letters or for the
# computer to do so with different difficulty settings

def guess_player_letter(language_eng: bool) -> str:
    """
    reoccurring function for guessing a letter as the PLAYER
    :param language_eng:
    :return:
    """
    while True:
        give_separators()
        console.print("--->   ", end="", style="blink bold")
        if language_eng:
            typewriter(select_word(text_assets.choose), executioner_talks, no_highlights)
        else:
            typewriter(select_word(text_assets.choose_german), executioner_talks, no_highlights)
        guess_func = str(input(":  "))
        give_separators()
        if len(guess_func) > 1 or not guess_func.isalpha():
            if language_eng:
                typewriter("\nYou fool of a tuck, only single letters are to be guessed. Do you want to break"
                           "the simulation?... go again... "
                           "this time remember the rules of only one letter at a time!", narrator_talks,
                           no_highlights)
            else:
                typewriter("\nDu Möchtegern-Hobbit, es darf nur ein einzelner Buchstabe geraten werden.\n "
                           "Möchtest du die Simulation zerstören? Versuche es erneut und denke daran, "
                           "dass nur ein Buchstabe auf einmal geraten werden darf!", narrator_talks,
                           no_highlights)
        else:
            break
    clean_window()
    return guess_func.lower()


def guess_computer_letter(language_eng: bool, alphabet: list) -> str:
    """
    reoccurring function for guessing a letter as the NPC (Executioner) does
    :param language_eng:
    :param alphabet:
    :return:
    """
    in_func_guess: str = select_word_lower(alphabet)
    if language_eng:
        typewriter("\n*The Executioner looks into the distance... thinking hard...*",
                   narrator_talks, no_highlights
                   )
    else:
        typewriter("\nDer Henker schaut nachdenklich in die Ferne...",
                   narrator_talks, no_highlights
                   )
    time.sleep(0)
    give_separators()
    if language_eng:
        typewriter(select_word(text_assets.npc_inner_thoughts), executioner_talks, no_highlights)
    else:
        typewriter(select_word(text_assets.npc_inner_thoughts_german), executioner_talks, no_highlights)
    give_separators()
    time.sleep(0)
    return in_func_guess


def guess_computer_letters_strategy(language_eng: bool, gues_let_func: list) -> str:
    """
    this reoccurring functions uses a simple vowel-first strategy to solve the user input words
    https://pynative.com/python-weighted-random-choices-with-probability/
    used for inspiration for guesses with probability.Links accessed on the 02.04.23
    used for probabilities: https://www.wordcheats.com/blog/most-used-letters-in-english
    :param language_eng:
    :param gues_let_func:
    :return:
    """
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
    if language_eng:
        typewriter("\n*The Executioner looks into the distance... thinking real hard...*",
                   narrator_talks, no_highlights
                   )
    else:
        typewriter("\nDer Henker schaut nachdenklich in die Ferne...",
                   narrator_talks, no_highlights
                   )
    time.sleep(0)
    give_separators()
    if language_eng:
        typewriter(select_word(text_assets.npc_inner_thoughts), executioner_talks, no_highlights)
    else:
        typewriter(select_word(text_assets.npc_inner_thoughts_german), executioner_talks, no_highlights)
    give_separators()
    time.sleep(0)
    in_function_guess = str(in_function_guess[0])
    return in_function_guess


# ----------------------------------------------

def high_strategy_dictionary(pydict: dict, gues_let: list, rem_let: list,
                             alphabet: list, language_eng: bool, mis_weight: int) -> str:
    """
    Function: creates an evaluated guess about secret word, simulates mistake

    Creating a skeleton dict without positional arguments.
    Add onto the length of lists of a corresponding key:value-pairs
    The biggest elements value gets chosen to be the high_guess
    merged list of correctly and wrongly guessed letters
    if the merged list of letters has at least one in it, we remove it by leaving it out of a new list
    gets the key with the highest value
    simulates a chance for mistake

    :param pydict: The big wordlist.
    :param gues_let: List of letters that have been guessed.
    :param rem_let: List of letters that should be removed.
    :param alphabet: Selected alphabet as a list of elements.
    :param language_eng: Bool value if the ui is in english.
    :param mis_weight: Chance for the random letter to be guessed instead of the actual most frequent.
    :return: Returns a guess letter
    """
    if language_eng:
        typewriter("\n*The Executioner looks into the distance... thinking real hard...*",
                   narrator_talks, no_highlights
                   )
    else:
        typewriter("\nDer Henker schaut nachdenklich in die Ferne...",
                   narrator_talks, no_highlights
                   )
    time.sleep(0)
    give_separators()
    if language_eng:
        typewriter(select_word(text_assets.npc_inner_thoughts), executioner_talks, no_highlights)
    else:
        typewriter(select_word(text_assets.npc_inner_thoughts_german), executioner_talks, no_highlights)
    give_separators()
    time.sleep(0)
    time.sleep(0)

    # Creating a skeleton dict without positional arguments.
    empty_in_func_dict: dict = {}
    for letter in alphabet:
        empty_in_func_dict[letter] = 0

    length_dict: dict = {}

    # merged list
    letter_list = list(set(gues_let + rem_let))

    # merged list, leaves out those with length above 1
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

    # makes use of the max function in pair with the get function to use the value
    # specifically of the key:value-pair

    highest_value_elem_unchosen: str = max(length_dict, key=length_dict.get)

    # simulate mistakes, so the computer isn't too good and acts different with the same word each time
    random_letter = select_word_lower(alphabet)
    # creates a list out of a random alphabetic letter and the highest_value_element
    probability_bowl: list = [random_letter, highest_value_elem_unchosen]

    highest_value_elem: str = random.choices(probability_bowl, weights=(mis_weight, 100-mis_weight), k=1)
    highest_value_elem = str(highest_value_elem[0])
    return highest_value_elem  # guess as char


def iterate_dict_to_sol_dict(real_dict: list, ghostly_solv_dict: dict) -> dict:
    """
    I take the "sliced by len(secretword)"-dictionary "short_dict" and iterate over each of its strings.
    I want to add, at each element, the index of its current word to the value list of
    the current element corresponding an empty dict key.
    The empty dict was created using letter_frequency_struct_maker,
    and only holds elements up to the length of the secret word,
    similar to how sliced dict only holds words as a list that are as long as secret word

    If it finds the letter "t" at position "4", put the index of the word in the list into a dictionary
    value where they key corresponds to "t4".
    The solv_struct starts at "a0".
    So the word from the
    example would have to be something like "aaaataa."
    :param real_dict:
    :param ghostly_solv_dict:
    :return:
    """

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
    """
    each time remove_letters gets a new one, which is letters not in the secret word
    this goes and looks at solving_dict,
    gets their index from values,
    removes those indexes from sliced_dct(here eunuch_dict),
    and gives back a better sliced_dict
    https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
    https://stackoverflow.com/questions/11303225/how-to-remove-multiple-indexes-from-a-list-at-the-same-time
    in code: thinner_the_sliced_dict(sliced_dict, solving_dict, guessed_letters)

    :param eunuch_dict:
    :param sol_dict:
    :param already_guessed_let:
    :return:
    """

    """
    Try 1
    for i, j in enumerate(sol_dict.keys()):
        if j in already_guessed_let:
            for x in sol_dict.keys([i]):
                remove_index_list = remove_index_list.append((sol_dict.values([i])))

    Try 2
    for i in range(sol_dict.keys()):
        if re.search("b/d", sol_dict.keys([i])) in already_guessed_let:
            for x in sol_dict.keys([i]):
                remove_index_list = remove_index_list.append(sol_dict.keys([i]).values())

    Try 3
    (Source: https://stackoverflow.com/questions/35786279/adding-dictionary-values-to-a-list, Access: 07.05.23)
    for key, value in sol_dict.items():
        for a letter in already_guessed_let:
            if key.startswith(letter):
                remove_index_list.append(sol_dict[key])
    """

    remove_index_list = []

    for key, value in sol_dict.items():
        for letter in already_guessed_let:
            if key.startswith(letter):
                remove_index_list.append(value)

    # function that cuts it all together
    super_sliced_dict = slice_shine_and_burn(remove_index_list, eunuch_dict)

    return super_sliced_dict  # sliced_dict


def format_the_hidden_word(sec_word: str, gues_letters: list, alphabet: list) -> list:
    """
    coming from the output the user can see like "a_s_h", and make conclusions
    based on the fact that certain words cannot be included,
    this creates a list that holds all keys that are not possible any more

    create lists of both the direct values and opposite values

    :param sec_word:
    :param gues_letters:
    :param alphabet:
    :return:
    """
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
    """
    This checks a specially created list of values created from the info one can get from
    correctly guessed letters.
    Meaning that when a_s_h is displayed, the list used here
    contains elements that are in opposition, like all keys not a0, but at position 0.
    Goes through the sol_dict and gets the keys, then for each key iterates through the remove_key_list
    and checks if they are the same.
    If they are the same, it adds the sol_dict keys values, which are index values,
    to the remove_index_list

    :param sol_dict:
    :param real_dict_list:
    :param remove_key_list:
    :return:
    """
    remove_index_list = []

    for key, value in sol_dict.items():
        for remove_key in remove_key_list:
            if key == remove_key:
                remove_index_list.append(value)

    super_sliced_dict = slice_shine_and_burn(remove_index_list, real_dict_list)

    return super_sliced_dict


def slice_shine_and_burn(list_to_burn: list, real_dict_list: list) -> list:
    """
    slices a list of alphabet_letter-keys with values of lists full of index values
    removes the duplicates
    removes the words for which the index value stand for in the big dictionary

    :param list_to_burn:
    :param real_dict_list:
    :return:
    """
    # using list comprehension to break up the list in list
    popped_remove_index_list = [item for sublist in list_to_burn for item in sublist]

    # sort and reverse
    list_sort_and_turned = sorted(popped_remove_index_list, reverse=True)

    # remove duplicates by creating a new list
    filtered_removal_list = remove_duplicates_in_list(list_sort_and_turned)

    # delete from the list
    for index in filtered_removal_list:
        try:
            del real_dict_list[index]
        except IndexError:
            # couldn't find a solution here, values already reversed
            continue

    return real_dict_list  # new sliced_dict


def remove_duplicates_in_list(func_list: list) -> list:
    """
    remove duplicates by creating a new list

    :param func_list:
    :return:
    """
    # remove duplicates by creating a new list
    filtered_removal_list = list()
    for item in func_list:
        if item not in filtered_removal_list:
            filtered_removal_list.append(item)

    return filtered_removal_list


def slice_dict(language: str, language_eng: bool, secret_word: str, value_if_own_dict: int,
               files_dict: list, value_which_dictionary: int) -> list:
    """
    takes a wordlist, either in-build or user-input (judged by additional parameters) and
    parts it by only taking the words with the length of the secret word

    :param language:
    :param language_eng:
    :param secret_word:
    :param value_if_own_dict:
    :param files_dict:
    :param value_which_dictionary:
    :return:
    """
    global my_dict, chosen_file, full_dict, in_built, output_in_func_dict, pre_sorted

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
        pre_sorted = False
        if language == "croatian":
            my_dict = open(f"DICTIONARIES/in-build-dictionaries/croatian.txt", "r")
            pre_sorted = True
        elif language == "german":
            my_dict = my_dict = open(f"DICTIONARIES/in-build-dictionaries/german.txt", "r")
        elif language == "czech":
            my_dict = open(f"DICTIONARIES/in-build-dictionaries/czech.txt", "r")
            pre_sorted = True
        elif language == "danish":
            my_dict = open(f"DICTIONARIES/in-build-dictionaries/danish.txt", "r")
            pre_sorted = True
        elif language == "dutch":
            my_dict = open(f"DICTIONARIES/in-build-dictionaries/dutch.txt", "r")
            pre_sorted = True
        elif language == "french":
            my_dict = open(f"DICTIONARIES/in-build-dictionaries/french.txt", "r")
            pre_sorted = True
        elif language == "georgian":
            my_dict = open(f"DICTIONARIES/in-build-dictionaries/georgian.txt", "r")
            pre_sorted = True
        elif language == "italian":
            my_dict = open(f"DICTIONARIES/in-build-dictionaries/italian.txt", "r")
            pre_sorted = True
        elif language == "maltese":
            my_dict = open(f"DICTIONARIES/in-build-dictionaries/maltese_words.txt", "r")
            pre_sorted = True
        elif language == "norwegian":
            my_dict = open(f"DICTIONARIES/in-build-dictionaries/norwegian.txt", "r")
            pre_sorted = True
        elif language == "polish":
            my_dict = open(f"DICTIONARIES/in-build-dictionaries/polish.txt", "r")
            pre_sorted = True
        elif language == "portuguese":
            my_dict = open(f"DICTIONARIES/in-build-dictionaries/portuguese.txt", "r")
            pre_sorted = True
        elif language == "serbian":
            my_dict = open(f"DICTIONARIES/in-build-dictionaries/serbian.txt", "r")
            pre_sorted = True
        elif language == "spanish":
            my_dict = open(f"DICTIONARIES/in-build-dictionaries/spanish.txt", "r")
            pre_sorted = True
        elif language == "swedish":
            my_dict = open(f"DICTIONARIES/in-build-dictionaries/swedish.txt", "r")
            pre_sorted = True
        elif language == "turkish":
            my_dict = open(f"DICTIONARIES/in-build-dictionaries/turkish.txt", "r")
            pre_sorted = True
        elif language == "ukranian":
            my_dict = open(f"DICTIONARIES/in-build-dictionaries/ukrainian.txt", "r")
            pre_sorted = True
        elif language == "hebrew":
            my_dict = open(f"DICTIONARIES/in-build-dictionaries/hebrew.txt", "r")
            pre_sorted = True
        elif language == "arabic":
            my_dict = open(f"DICTIONARIES/in-build-dictionaries/arabic.txt", "r")
        elif language == "english medical terms":
            my_dict = open(f"DICTIONARIES/in-build-dictionaries/medical-wordlist.txt", "r")
            pre_sorted = True
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

        in_func_list = []
        if value_if_own_dict == 1 or not pre_sorted:
            """
            turn every element of dictionary into alpha-mode
            slices/chooses only words with the right length, does so with all before selected lists.
            choose words with len(word) = len(secret_word)
            does so if dict is user_input or if it isn't in the list of sorted in-builds
            """
            for word in data_dict_list:
                if len(word) == len(secret_word):
                    low_word = word.lower()
                    in_func_list.append(low_word)
        else:
            # stops once we went through our fitting interval in a sorted list:
            in_interval = False
            for word in data_dict_list:
                if len(word) == len(secret_word):
                    in_interval = True
                    low_word = word.lower()
                    in_func_list.append(low_word)
                else:
                    if in_interval:
                        """
                         breaks if we have passed the interval
                         does so if there was a fit in length to secret word
                        """
                        break

        output_in_func_dict = in_func_list

    return output_in_func_dict


def slice_the_english(language_eng: bool, length_of_secret_word: int) -> list:
    """
    Function to select the part of the english wordlist by predefined values
    to save on time.
    Knows which interval by using the length of the secret word

    :param language_eng:
    :param length_of_secret_word:
    :return:
    """
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
                console.print("mhhh, I do not know any words with 26 letters...", )
                console.print("I will try anyway, but I will take some more time, mortal.", )
                console.print("I hope you have some more left... muahahah\n", )
            else:
                console.print("Hmm, ich kenne keine Wörter mit 26 Buchstaben...", )
                console.print("Dennoch werde ich es versuchen, aber ich werde mir etwas mehr Zeit nehmen, Sterblicher.",
                              )
                console.print("Ich hoffe, du hast noch etwas übrig... Muahahaha\n",
                              )
        elif length_of_secret_word == 27:
            output_dict = fun_dict[370097:370099]
        elif length_of_secret_word == 28:
            output_dict = fun_dict[370100:370101]
        elif length_of_secret_word == 29:
            output_dict = fun_dict[370102:370104]
        elif length_of_secret_word == 30:
            output_dict = fun_dict
            if language_eng:
                console.print("mhhh, I do not know any words with 30 letters...", )
                console.print("I will try anyway, but I will take some more time, mortal.", )
                console.print("I hope you have some more left... muahahah\n", )
            else:
                console.print("Hmm, ich kenne keine Wörter mit 30 Buchstaben...", )
                console.print("Dennoch werde ich es versuchen, aber ich werde mir etwas mehr Zeit nehmen, Sterblicher.",
                              )
                console.print("Ich hoffe, du hast noch etwas übrig... Muahahaha\n", )
        elif length_of_secret_word == 31:
            output_dict = fun_dict[370105:370105]
        else:
            if language_eng:
                console.print("\nthat's a very long word... are you sure it exists?", )
                console.print("\nI will try anyway, cheat.", )
                console.print("\nIf you button-smashed, I will haunt your dreams for eternity and make sure that "
                              "in the after-life you won`t have the chance to dream.... just kidding... unless...",
                              )
            else:
                console.print("\nDas ist ein sehr langes Wort... bist du sicher, dass es existiert?",
                              )
                console.print("\nIch werde es trotzdem versuchen, Schummler.", )
                console.print("\nWenn du wild auf den Tasten hermeneutical hast,\n"
                              "werde ich dich für die Ewigkeit heimsuchen und sicherstellen,\n"
                              "dass du im Jenseits nicht träumen wirst... nur ein Scherz... oder auch nicht...",
                              )
            output_dict = fun_dict

    return output_dict


#          -------------------------------
def letter_frequency_structure_maker(sec_word_for_func: str, alph_in_func: list) -> dict:
    """
    creates an array of keys of the length of secret word with the other axis being the alphabet
    since initializing 806 possible combinations would be unnecessary.
    all the values of the arrays are listed with the index values of the corresponding words
    starts at a0/or whatever is first in the selected alphabet given by parameter

    :param sec_word_for_func:
    :param alph_in_func:
    :return:
    """

    sec_le = len(sec_word_for_func)
    alp_le = len(alph_in_func)
    solvstruct = {}

    for i in range(sec_le):
        for j in range(alp_le):
            solvstruct["{}{}".format(alph_in_func[j], str(i))] = []

    return solvstruct


# -----------------------------------------

def is_guess_in_secret_word(guess_in_func: str, sec_word: str) -> bool:
    """
    function that checks if a letter is in secret word

    :param guess_in_func:
    :param sec_word:
    :return:
    """

    if guess_in_func in sec_word:
        return True
    else:
        return False


# ----------------------------------------
def get_unique_letters(word: str, alph: list) -> list:
    """
    function used to put the secret_word string into a set, so we can remove duplicates and iterate easy

    :param word:
    :param alph:
    :return:
    """
    sec_list: list = []
    word = set(word)
    for element in word:
        if element in alph:
            if element not in sec_list:
                sec_list.append(element)
    return sec_list


# -----------------------------------------

def user_input_word(language_eng: bool) -> str:
    """
    Function handles the user-input for the challenge_word
    :param language_eng:
    :return:
    """

    # variable used for control while a statement
    global user_word
    good_enough_points = False

    while not good_enough_points:
        # while-loop breaks when the challenge_word is good enough
        if language_eng:
            console.print("--->   ", end="", style="blink bold")
            typewriter("... so be it... \n       write your human word on this card and do not tell me: ",
                       executioner_talks, no_highlights)
            user_word = str(input())
        else:
            console.print("--->   ", end="", style="blink bold")
            typewriter("... so sei es... schreib dein menschliches Wort hier drauf und sag es mir nicht:",
                       executioner_talks, no_highlights)
            user_word = str(input())
        # checking the challenge_word for anything bad
        # does it have numbers in it?
        # is challenge word actually multiple words with space between
        if " " not in user_word and not are_there_numbers(user_word):
            if len(user_word) > 0:
                good_enough_points = True
            else:
                if language_eng:
                    typewriter("\n Narrator: Numbers??? Multiple words??? Separators?!\n"
                               "Not in this game! Repeat, Repeat, Repeeeeat!", narrator_talks, no_highlights)
                else:
                    typewriter("\n Narrator: Zahlen??? Mehrere Wörter??? Trennzeichen?! Nicht in diesem Spiel!\n"
                               "Wiederholen, Wiederholen, Wiederholen!",
                               narrator_talks, no_highlights)
        else:
            if language_eng:
                typewriter("\n Narrator: Numbers??? Multiple words??? Separators?! Not in this game!\n"
                           "Repeat, Repeat, Repeeeeat!", narrator_talks, no_highlights)
            else:
                typewriter("\n Narrator: Zahlen??? Mehrere Wörter??? Trennzeichen?! Nicht in diesem Spiel!\n"
                           "Wiederholen, Wiederholen, Wiederholen!", narrator_talks, no_highlights)
    return user_word


# ----------------------------------------

def games_callout(who_won: str, language_eng: bool):
    """
    function that gives out a statement according to who won - perspective player
    :param who_won:
    :param language_eng:
    :return:
    """
    if who_won == "NPC":
        console.print(text_assets.npc_art_win, highlight=True)
        console.print("", )
        time.sleep(0)
        give_separators()
        console.print(select_word(text_assets.npc_wins), )
        console.print("", )
        if language_eng:
            typewriter(
                "Narrator: The Exorcist... or was it Executioner?... has won! pity you!\n",
                narrator_talks, no_highlights)
        else:
            typewriter("Narrator: Der Exorzist... oder war es der Henker?... hat gewonnen! Schade für dich!\n",
                       narrator_talks, no_highlights)
        give_separators()
    if who_won == "Player":
        give_separators()
        if language_eng:
            typewriter(select_word(text_assets.player_wins), executioner_talks, no_highlights)
        else:
            typewriter(select_word(text_assets.player_wins_german), executioner_talks, no_highlights)
        console.print("", )
        if language_eng:
            typewriter("Narrator: Wow! You have actually managed to win! good job you!\n", narrator_talks,
                       no_highlights)
        else:
            typewriter("\nNarrator: Wow! Du hast es tatsächlich geschafft zu gewinnen! Gut gemacht!\n",
                       narrator_talks, no_highlights)
        console.print("")
        console.print(text_assets.player_art_win, highlight=False, style="bold #fc3205")
        console.print("")
        give_separators()


# -----------------------------------------
# function for printing out a cool executioner
def let_it_begin_art():
    """
    prints the hangman logo from text_assets
    :return: the hangman logo as a console.print
    """
    console.print(text_assets.executioner_game_start)


# -----------------------------------------
# Hangman stages as a function corresponding to the remaining_attempts
def get_hangman_stage(attempt_number: int):
    """
    gives out the ascii art of the current hangman stage
    :param attempt_number: current attempt number
    :return: ascii art as string item
    """
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
    """
    function checks if there are any files in a directory
    :param path:
    :return:
    """
    return list(os.listdir(path))
