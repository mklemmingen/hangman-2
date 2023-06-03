# hangman 2 - the dictionaries strike back

terminal-optimised hanging man game. simply clone and python run the game_script to start.

![til](https://raw.githubusercontent.com/mklemmingen/hangman-2/master/hangman2_intro.gif)

(best played in a 90x40 terminal)

It supports both english and german in the UI and many more languages through language/dictionary selection [see manual in game]
  - supported languages: english, german, ukranian, arabic, croatian, czech, danish, french, 
                         georgian, hebrew, italian, norwegian, polish, portugese, serbian, 
                         spanish, swedish, maltese, turkish
                         
The game has characterizations and dialoque in it to make it more lively and fun.

Decisions are made by typing in one of the displayed numbers or by input of words and letters.

If you want the computer to use another wordlist for guessing your words, simply put one of the dictonaries
into the user_input_dictionaries folder. You can then choose it in game the next time you start it.

supports a colourblind-mode, set to True in the Options Menu.

### You either play yourself and try to solve a secret word, or you can challenge the villain with a word you can individually give him.
### The user can select 3 difficulty options.

  - easy: simply chooses a random letter of the alphabet and acts as if its a toddler who just gained colour sight
  
  - medium: hard mode but with a higher chance for mistakes if not changed prior in the option menus mistake scale.
  
  - hard: here is where the fun begins:
  
      - takes either an in-build or a dictionary in the user_input_dict dir to use for guessing. Sorts it the first time it runs a new one. 
      - The computer limits the interchangeable dictionary it reads by length of the word you give him.
      - He then iterates through each element of each word and adds the index values of the whole words into a dictionary of alphabet_at_position (meaning a0, a1, a2...,x30)
      - At the end, these values are measured, summed up by letter and altogether, the biggest letter (90%) or a random letter (10%) gets choosen to be guessed.
    
      - if it has guessed correct, it receives positional information, like a real player would, where in the secret word the guessed letter would be. 
      - It then calculates the oppositional elements that cannot be at that position (guessed letter: a2 oppos.: b2,c2,...,x2), collects the index values and deletes those from right to left
        from the pool from which it iterates at each loop.
      - if the guess has been incorrect, all index vallues of words where that guess-element has been a part of at whatever position gets yeeted into nothingness. 

The computers "high strategy" is based on how an adult player would make his choices, if he didnt know what words are, and just knows they consist of up to an individual numbers of funny looking letters.
The computer, if the word is in fact in the dictionary, is able to play surprisingly well, since the usage of a random letter being able to be guessed to increase replayability and chance for the player.

## See for yourself! 

If you have any tips and tricks on how to improve the code, feel free to message or create a discussion

Dependencies
```python
# iibuilt in py>3
import random
import time
import sys
import os
# needs to be gathered - use IDLE package manager, pip or else.
import rich
```

## FUTURE of the Game

TO-DO:
  - nothing and wait for bugs

COMPLETED:
  - Fallback of high strategy to medium difficulty if length of iterated dict == 0 
  - change game-phase layout so the player chooses hard-mode more naturally and has lower difficulty settings as a fallback for more playthroughs
  - split source code inbetween functions, game-run, art and lines
  - easier dictionary support
      - simply put a dictionary list into user-input-dictionary folder (code has to run atleast once before for the dir to be created)
      - make sure words are seperated only by a new line, not ";" etc
  - update already existing dictionaries
  - added game start menu
  - layout for terminal execution
  - add multiple alphabets for easy and medium difficulty, as well as more word categories with less restrictive letter guessing
    that include non-standard-english letters 
  - Fixes of german
  - add the possibility for mistake into the computer guessing, so that the player always has a chance and doesnt have to resort to using ultra-long words,
    and so there is replayability
  - typewriter effect
  - implemented rich for nice looking colours, bold, blink and italic formatting. Hangman - now in Colour!
  - added good documentation for the functions
  - added colourblind mode
  - added choosable scale in probability for mistake in the computer

EXCLUDED AND TERMINATED:
  - Game Interface
      - using pygame and pygame_gui, or pysimplegui, or renpy... 
      - after laying out the UI, the script has proven too complicated for easy beginner implimentation. Classes and threading needed.
      -> interface-idea thrown out. instead used rich for a nice and efficient terminal layout without any bugs!


## DICTIONARY SOURCES:

  - https://github.com/dwyl/english-words
      - words-alpha.txt   [English!] as english_words.txt in the repo
  - https://github.com/enz/german-wordlist/blob/master/words
      - german_words 
  - https://github.com/OpenTaal/opentaal-wordlist/blob/master/wordlist.txt
      - dutch_words 
  - https://github.com/shaunazzopardi/maltese-dictionary/blob/master/wordlist.txt
      - maltese words
  - https://github.com/kkrypt0nn/wordlists/tree/main/languages
      - ukranian 
      - arabic
      - croatian
      - czech
      - danish
      - french
      - georgian
      - hebrew
      - italian
      - norwegian
      - polish
      - portugese
      - serbian
      - spanish
      - swedish
      - turkish
- https://github.com/glutanimate/wordlist-medicalterms-en/blob/master/wordlist.txt
      - medical terms
- https://github.com/xajkep/wordlists
