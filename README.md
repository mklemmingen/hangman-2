# hanging_man

The game has a D&D like story-aspect to it to make it stand out against simple vanilla hangman games.

It supports both english and german.

Decisions are made by typing in one of the displayed numbers, and as of now, all that is done in the console.

The structure of the game is fairly simple and follows basic control structures.

- You either play yourself and try to solve a secret word, or you can challenge the villain with a word you can individually give him.

### The user can select 3 difficulty options.

  - easy: simply chooses a random letter of the alphabet and acts as if its a toddler who just gained colour sight
  - medium: knows which letters of the alphabet are most used and weights them more than others in his random decision making.
  - hard: here is where the fun begins:
  
      - The computer limits (as of now this has to be added manually) the interchangeable dictionary by length of the word you give him.
      - He then iterates through each element of each word and adds the index values of the whole words into a dictionary of alphabet_at_position (meaning a0, a1, a2...,x30)
      - At the end, these values are measured, summed up by letter and altogether, the biggest letter gets choosen to be guessed.
    
      - if it has guessed correct, it receives positional information, like a real player would, where in the secret word the guessed letter would be. 
      - It then calculates the oppositional elements that cannot be at that position (guessed letter: a2 oppos.: b2,c2,...,x2), collects the index values and deletes those
        from the pool from which it iterates at each loop.
      - if the guess has been incorrect, all index vallues of words where that element has been a part of at whatever position gets yeeted into nothingness. 

the computers "high strategy" is based on how an adult player would make his choices, if he didnt know what words are, and just knows they consist of up to 26 individual letters.
The computer, if the word is in fact in the dictionary, is able to play surprisingly well. 

### See for yourself! 

If you have any tips and tricks on how to improve the code or where to get a big chunk of dictionaries like the one I sneakily forked, feel free to message or create a discussion

TO-DO:
  - Game Interface
  - Fixes of german
  - check if iteration process can be speed-up (late stage tweaking)
  - late-stage: support for spaces?

COMPLETED:
  - Fallback of high strategy to medium difficulty if length of iterated dict == 0 
  - change game-phase layout so the player chooses hard-mode more naturally and has lower difficulty settings as a fallback for more playthroughs
  - split source code inbetween functions, game-run, art and lines
  - easier dictionary support
      - simply put a dictionary list into DICTIONARIES folder
      - make sure words are seperated only by a new line, not ";" etc

Dictionaries already in the program:
  - https://github.com/dwyl/english-words
      - words-alpha.txt   [English!]
  - https://github.com/enz/german-wordlist/blob/master/words
      - german_words 
  - https://github.com/OpenTaal/opentaal-wordlist/blob/master/wordlist.txt
      - dutch_words 
