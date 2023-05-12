import random  # used to choose randomly out of lists, see "https://docs.python.org/3/library/random.html"
import time  # used to simulate delays of the npc while choosing a letter and add user-friendliness
import os  # used to exit and reload programm at end
import sys  # "

# **LISTS**  -------------------------------------------

# test-list
words_scrambled = ["tiger", "tree", "underground",
                   "giraffe", "coconut", "chair",
                   "lipstick", "sugar"]

# list for the topic of "Animals"
animals = ["Dog", "Cat", "Fish", "Bird", "Frog", "Mouse", "Rat",
           "Horse", "Cow", "Pig", "Sheep", "Goat", "Deer", "Rabbit",
           "Bat", "Fox", "Wolf", "Bear", "Lion", "Tiger", "Elephant",
           "Giraffe", "Rhino", "Hippo", "Gorilla", "Chimpanzee", "Koala",
           "Kangaroo", "Platypus", "Crocodile", "Alligator", "Turtle",
           "Snake", "Lizard", "Shark", "Octopus", "Jellyfish", "Crab",
           "Lobster", "Shrimp", "Squid", "Scorpion", "Spider", "Bee",
           "Butterfly", "Ant", "Grasshopper", "Ladybug", "Mosquito", "Firefly"]

animals_german = ["Fuchs", "Dachs", "Reh", "Hirsch", "Wildschwein", "Wolf", "Biber",
                  "Igel", "Eichhörnchen", "Marder", "Feldhase", "Dachs", "Eule",
                  "Fasan", "Specht", "Maus", "Maulwurf", "Wiesel", "Eidechse",
                  "Ringelnatter", "Schlange", "Fledermaus", "Buntspecht", "Blaumeise",
                  "Rotkehlchen", "Elster", "Rabe", "Amsel", "Schwan", "Graugans",
                  "Habicht", "Maeusebussard", "Wanderfalke", "Bussard", "Sperber",
                  "Waldkauz", "Uhu", "Grauhoernchen", "Dohle", "Steinmarder",
                  "Baummarder", "Waldmaus", "Spitzmaus", "Feldmaus", "Roetelmaus",
                  "Siebenschlaefer", "Wuehlmaus", "Haselmaus", "Waldschnepfe", "Buntspecht"]

# list of the topic of "cities"
cities = ["New York", "London", "Paris", "Tokyo", "Los Angeles",
          "Hong Kong", "Singapore", "Dubai", "Sydney", "Toronto",
          "Shanghai", "Miami", "Berlin", "Amsterdam", "Barcelona",
          "Rome", "Abu Dhabi", "San Francisco", "Istanbul", "Moscow",
          "Bangkok", "Vienna", "Beijing", "Stockholm", "Munich", "Zurich",
          "Melbourne", "Copenhagen", "Oslo", "Brussels", "Helsinki", "Seoul",
          "Madrid", "Milan", "Dublin", "Budapest", "Prague", "Warsaw", "Athens",
          "Lisbon", "Edinburgh", "Bucharest", "Bratislava", "Sofia", "Reykjavik",
          "Cape Town", "Marrakesh", "Rio de Janeiro", "Vancouver"]

# list of the topic of "food"
food = ["Pizza", "Sushi", "Taco", "Kebab", "Curry", "Pho", "Gyros", "Pad Thai", "Biryani",
        "Fajita", "Ramen", "Falafel", "Ceviche", "Samosa", "Pierogi", "Paella", "Risotto",
        "Goulash", "Hummus", "Tabbouleh", "Chimichanga", "Dumplings", "Empanada", "Bruschetta",
        "Baklava", "Couscous", "Kimchi", "Shawarma", "Laksa", "Poutine", "Katsu", "FishandChips",
        "Bangers and Mash", "WienerSchnitzel", "Haggis", "Fondue", "Peking Duck", "Tzatziki",
        "Tandoori", "Jambalaya", "Feijoada", "Borscht", "Frikadeller", "Pierogi", "Koettbullar",
        "Chakalaka", "Baozi", "Churros"]

# list of the topic of "presidents"
presidents = ["Obama", "Trump", "Clinton", "Washington", "Adams", "Jefferson",
              "Madison", "Monroe", "Jackson", "Buren", "Harrison", "Tyler",
              "Polk", "Taylor", "Fillmore", "Pierce", "Buchanan", "Lincoln",
              "Johnson", "Grant", "Hayes", "Garfield", "Arthur", "Cleveland",
              "Harrison", "Cleveland", "McKinley", "Roosevelt", "Taft", "Wilson",
              "Harding", "Coolidge", "Hoover", "Roosevelt", "Truman", "Eisenhower",
              "Kennedy", "johnson", "Nixon", "Ford", "Carter", "Reagan", "Bush",
              "clinton", "bush", "biden"]

# list of the topic of "cartoon-characters"
cartoon_characters = ["Mickey", "SpongeBob", "Bugs", "Homer", "Tom", "Pikachu", "Bart", "Daffy",
                      "Minnie", "Scooby", "Fred", "Donald", "Popeye", "Charlie", "Tweety", "Dexter",
                      "Blossom", "Yogi", "Marge", "Spider-Man", "Batman", "Superman", "Ironman",
                      "Captain", "Hulk", "Thor", "Wonder", "Catwoman", "Robin", "Mermaid", "Aladdin",
                      "Buzz", "Woody", "Nemo", "Dory", "Mike", "Sulley", "Shrek", "Fiona", "Donkey",
                      "Puss", "Goofy", "Chip", "Phineas", "Snoopy", "Tintin", "Sailor", "Leonardo",
                      "Michelangelo"]

# list of hard words
hard_words = ["Supercalifragilistic", "ketoacidosis", "Dephosphorylation", "Deoxyribonucleic",
              "Personalstaerkeuntergrenzengesetz", "dichlorodiphenyltrichloroethane"]

# ---------------------------------------------------
# words for the computer to say when he gives a wrong answer and for when player gets it right

point_player = ["I damn you and your tricky wordplays",
                "I should have stayed at home today",
                "With my luck, I hope I turned off the oven this morning",
                "If god had given me jurisdiction, I would ban this game...",
                "HOW DO YOU COME UP WITH THIS?!",
                "... I need a drink... like a strong bubbly soda",
                "How in the name of my bloody axe???",
                "I think I need to stop letting people challenge me.",
                "I should have listened to my second grade teacher and become a gardner",
                "Do you think I do this for fun? The IRS wants 400$ in payback from me.",
                "Damn, I wish this was a simulation",
                "Do you know how hard it is for me to focus on torture while wearing this itchy black robe??",
                "You should be honored to be playing this game with me. I usually reserve it for my enemies.",
                "I'm glad you're so eager to play. I was starting to think you didn't have the guts.",
                "Hangman is like life: one mistake and it's game over. Except in your case, it's literally game over.",
                "I see you, trying to cheat me in this game of Hangman. You think you can outsmart me,\n"
                "but you can't. You're nothing but a lowly cheat, and you'll never win against me.",
                "I know your kind. You try to play the innocent, but you're just biding your time, \n"
                "waiting to strike. Well, I'm onto you. I won't let you get away with it.",
                "I've seen all kinds of cheaters in my time, and you're no different. \n"
                "You think you can pull a fast one on me, but I'm too smart for that.\n"
                " I know every trick in the book.",
                "I've made a vow not to attack you during the game, \n"
                "but that doesn't mean I won't call you out on your cheating ways. \n"
                "You'll never beat me, not with your underhanded tactics.",
                "You may think you're one step ahead of me, but you're not.\n"
                " I'm always watching, always waiting for you to slip up. \n"
                "And when you do, I'll be ready to pounce."]

point_player_german = ["Ich verfluche dich und deine trickreichen Wortspiele",
                       "Ich hätte heute lieber zuhause bleiben sollen",
                       "Mit meinem Glück hoffe ich, dass ich den Ofen heute Morgen ausgeschaltet habe",
                       "Wenn Gott mir Zuständigkeit gegeben hätte, würde ich dieses Spiel verbieten...",
                       "WIE KOMMST DU AUF DIESE IDEE?!",
                       "... Ich brauche einen Drink... wie ein starkes, sprudelndes Soda",
                       "Wie zum Teufel soll das funktionieren???",
                       "Ich glaube, ich sollte aufhören, mich von Leuten herausfordern zu lassen.",
                       "Ich hätte auf meine Lehrerin aus der zweiten Klasse hören und Gärtner werden sollen",
                       "Denkst du, ich mache das hier zum Spaß? Das Finanzamt will 400$ von mir zurück.",
                       "Verdammt, ich wünschte, das wäre eine Simulation",
                       "Weißt du, wie schwer es für mich ist, mich auf Folter zu konzentrieren, "
                       "während ich dieses juckende schwarze Gewand trage??",
                       "Du solltest geehrt sein, dass du dieses Spiel mit mir spielst. "
                       "Ich behalte es normalerweise für meine Feinde.",
                       "Ich freue mich, dass du so scharf darauf bist zu spielen. "
                       "Ich dachte schon, du hast nicht das Zeug dazu.",
                       "Hangman ist wie das Leben: Ein Fehler und das Spiel ist vorbei. \n"
                       "Aber in deinem Fall ist es buchstäblich Spiel vorbei.",
                       "Ich sehe dich, wie du versuchst, mich in diesem Spiel von Hangman zu betrügen. "
                       "Du denkst, du kannst mich überlisten,\n"
                       "aber das kannst du nicht. Du bist nichts als ein erbärmlicher Betrüger,"
                       " und du wirst niemals gegen mich gewinnen.",
                       "Ich kenne deine Sorte. Du versuchst, unschuldig zu spielen,"
                       " aber du wartest nur darauf, zuzuschlagen. \n"
                       "Nun, ich bin auf dich aufmerksam geworden. Ich werde es dir nicht durchgehen lassen.",
                       "Ich habe in meiner Zeit schon alle Arten von Betrügern gesehen, und du bist nicht anders. \n"
                       "Du denkst, du kannst mich hinters Licht führen, aber dafür bin ich zu schlau.\n"
                       " Ich kenne jedes Trickbuch.",
                       "Ich habe geschworen, dich während des Spiels nicht anzugreifen, \n"
                       "aber das bedeutet nicht, dass ich dich nicht wegen "
                       "deiner betrügerischen Methoden zur Rede stellen werde. \n"
                       "Du wirst mich niemals schlagen, nicht mit deinen hinterhältigen Taktiken.",
                       "Du magst denken, dass du mir einen Schritt voraus bist, aber das bist du nicht. \n"
                       "Ich beobachte dich immer, warte immer darauf, dass du einen Fehler machst. \n"
                       "Und wenn du das tust, werde ich bereit sein, zuzuschlagen."]

# words for the computer to say when he gives the right answers or when player has it wrong

point_computer = ["Hah, I pity the fool that you are!",
                  "If you win, I'll let the innocent man go free. If I win, well...\n"
                  " let's just say there's a vacancy at the end of the rope.",
                  "No man can kill me!!!... so I do hope you are not a women",
                  "This is too easy. Do you even want Jeff to survive this?",
                  "Next time, try to think of more vowels, muahahahahahah",
                  "And you call yourself a gamer? Have you heard of going outside?",
                  "Why do I always wake up those unworthy of my challenge?",
                  "*the executioner dances* *shakes his bloody axe in the air like he dont care*",
                  "The Narrator *whispers*: Are you sure that that was a good choice?",
                  "The Executioner is canonically a ... and the programmer got tired of narrating *seals off 4th wall*",
                  "Looks like I've got you in a tight noose, my friend!",
                  "I hope you're good at spelling 'guilty' because that's where you're headed!",
                  "You're the perfect contestant for my game show: 'Hangman: Live or Die!'",
                  "I'm going to make you swing from the gallows like a piñata at a children's party!",
                  "I learned how to spell 'vengeance' after my dog ran away with my family to Las Vegas.\n"
                  " You don't stand a chance."
                  ]

point_computer_german = ["Hah, ich bedaure dich, du Dummkopf!",
                         "Wenn du gewinnst, lasse ich den unschuldigen Mann frei. "
                         "Wenn ich gewinne, nun ja... \n"
                         "lassen wir es einfach sagen, es gibt eine freie Stelle am Ende des Seils.",
                         "Kein Mann kann mich töten!!!... also hoffe ich, dass du keine Frau bist",
                         "Das ist zu einfach. Willst du, dass Jeff das überlebt?",
                         "Versuche beim nächsten Mal, an mehr Vokale zu denken, muahahahahahah",
                         "Und du nennst dich ein Gamer? Hast du schon mal was von 'Draußen sein' gehört?",
                         "Warum wecke ich immer diejenigen auf, die meiner Herausforderung unwürdig sind?",
                         "der Henker tanzt schwingt seine blutige Axt wie ein Profi",
                         "Der Erzähler flüstert: Bist du sicher, dass das eine gute Wahl war?",
                         "Sieht aus, als hätte ich dich in eine enge Schlinge gebracht, mein Freund!",
                         "Ich hoffe, du kannst 'schuldig' richtig schreiben, denn dort geht es hin!",
                         "Du bist der perfekte Kandidat für meine Spielshow: 'Hangman: Leben oder Sterben!'",
                         "Ich werde dich an der Galgen schwingen lassen wie eine Piñata auf einer Kinderparty!",
                         "Ich habe gelernt, wie man 'Rache' buchstabiert, "
                         "nachdem mein Hund mit meiner Familie nach Las Vegas weggelaufen ist.\n"
                         "Du hast keine Chance."
                         ]

# words for when the computer wins

npc_wins = ["My father used to say, 'Cheaters never prosper,' but he obviously never played Hangman with me.",
            "I have won and Jeff will die. He shall hang for eternity for the crimes he has not committed",
            "MUAHAHAHAHHAHAHAHAHA you have lost the challenge and are now forced to rejoin reality",
            "I hope you suffered, you foolish ghoul! Let the power of vowels burn! I have won!",
            "MUUHAHAHAHAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHA",
            "This was harder than expected, but you still lost, you worm",
            "Whoever reads this is forced to give me an extra point",
            "Do you dare go again, you foolish hobbit?"]

npc_wins_german = ["Mein Vater pflegte zu sagen: 'Schummler haben niemals Erfolg', "
                   "aber er hat offensichtlich nie Hangman mit mir gespielt.",
                   "Ich habe gewonnen und Jeff wird sterben. "
                   "Er wird für die Verbrechen, die er nicht begangen hat, für immer hängen.",
                   "MUAHAHAHAHHAHAHAHAHA Sie haben die Herausforderung verloren "
                   "und sind jetzt gezwungen, zur Realität zurückzukehren.",
                   "Ich hoffe, du hast gelitten, du törichter Ghul! "
                   "Lass die Kraft der Vokale brennen! Ich habe gewonnen!",
                   "MUUHAHAHAHAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHA",
                   "Das war schwieriger als erwartet, aber du hast trotzdem verloren, du Wurm.",
                   "Wer das liest, ist gezwungen, mir einen Extrapunkt zu geben.",
                   "Wagst du es, noch einmal zu spielen, du törichter Hobbit?"]

# words for when the computer loses

player_wins = ["I knew I should have added Umlaut!", "Congrats, i guess, you and Jeff can go now",
               "You used Umlaute, didnt you? Damn germans"]

player_wins_german = ["Ich wusste, ich hätte Umlaute hinzufügen sollen!",
                      "Herzlichen Glückwunsch, nehme ich an, du und Jeff könnt jetzt gehen",
                      "Du hast Umlaute benutzt, oder? Verdammt, Deutsche!"]

# words for when the player has to choose

choose = ["Choose wisely, or Thor will strike you hard. CHOOSE!", "Choose another letter... try... tryyyy. NOW!",
          "Are you in fear yet? Guess a letter!", "What is taking you so long? Choose one!",
          "How on earth did you make it till here? Choose a letter! now!",
          "What are you waiting for! choose!",
          "I may be the immortal hangman's executioner, but I dont have all day! Guess!",
          "Have you heard the tale of Beetle the Bard? No? ok. CHOOSE A LETTER!"]

choose_german = ["Wähle weise, oder Thor wird dich hart treffen. WÄHLE!",
                 "Wähle einen anderen Buchstaben ... versuch es ... versuch es jetzt!",
                 "Hast du schon Angst? Rate einen Buchstaben!", "Was dauert so lange? Wähle einen!",
                 "Wie zum Teufel hast du es bis hierher geschafft? Wähle einen Buchstaben! Jetzt!",
                 "Worauf wartest du? wähle!",
                 "Ich bin zwar der Henker des unsterblichen Galgens, aber ich habe nicht den ganzen Tag Zeit! Rate!",
                 "Hast du die Geschichte von Beetle dem Barde gehört? Nein? OK. WÄHLE EINEN BUCHSTABEN!"]

# letters for the computer to choose

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]

# words that the npc is thinking  # some of these were created by chatgpt after an appropriate input

npc_inner_thoughts = ["I have an idea... but it may be risky!",
                      "My mother always said, 'Don't gamble with your life,' but she clearly never met me.",
                      "I've always been a man of words, but this hangman game is getting the best of me.\n "
                      "Maybe I should stick to my usual hobby of devising diabolical plans to conquer the world.\n "
                      "Ha ha ha! Just kidding...or am I?",
                      "I've never been one to play fair, "
                      "so I'm using my evil intellect to crack this hangman puzzle.\n "
                      "And once I do,"
                      "I'll have the perfect revenge against those do-gooders who thwarted my last scheme.",
                      "I had a crush on Shakespeare, but now I have a crush on crushing my opponents in Hangman.",
                      "My family tree is twisted like a noose, but at least I'm the one holding the rope.",
                      "I may be a villain, but I still have a way with words. Let's see...\n "
                      "'E' is a good bet... and 'O'... come on, think, you twisted genius, think!",
                      "I've faced off against superheroes, but this hangman game is my biggest challenge yet.\n "
                      "Curse you, alphabet! Why must you be so tricky?",
                      "Hangman? More like hang-villain!"
                      "I'm going to solve this puzzle and then plot my next dastardly deed.\n "
                      "Nothing can stop me now!",
                      "Ah, the sweet anticipation of the hangman's noose. "
                      "But there's something different about Jeff.\n "
                      "He's not like the others. I almost hate to see him go...almost.",
                      "I've been executing mortals for centuries, but there's something intriguing about Jeff. Maybe\n "
                      "it's his wit, or his cunning, or... well, never mind. Let's just get this over with, shall we?",
                      "As an immortal executioner, I've seen it all. And frankly, I'm tired of it.\n "
                      "All I want now is someone to talk to, instead of constantly being stuck in my own head.\n"
                      "I mean, what's the point of being a godly being if you can't even enjoy life?",
                      "I used to revel in the screams of the damned, but now it just feels like a chore.\n"
                      "If only I had someone to share my thoughts with,"
                      "instead of always having to silence them with my blade.",
                      "I've been around for centuries, and I've seen it all. \n"
                      "But nothing gives me more pleasure than watching my victims swing from the noose.",
                      "They say the Hangman's noose is a symbol of justice, but to me, it's a symbol of power.",
                      "I've haunted the dreams of many, but now it's time to haunt the reality of my next victim.",
                      "They say that death is the great equalizer,\n"
                      " but I prefer to think of myself as the great differentiator.",
                      "I don't discriminate when it comes to my victims. Rich, poor, guilty, innocent... \n"
                      "they all end up swinging from the Hangman's noose."
                      "As an immortal godly executioner, I've seen it all. The pain, the suffering, the screams.\n "
                      "But what I wouldn't give for just a moment of peace,"
                      "a chance to talk to someone who understands\n "
                      "the burden of my existence. But seeing as tho what you choosed... you are not it.",
                      "I once had a dog that could spell better than most people. \n"
                      "Too bad he ran off with my ex-wife and kids.",
                      "I don't need a reason to claim another victim. It's just what I do. And I do it well.",
                      "My therapist says I have a compulsive need for control, \n"
                      "but she's not the one holding the power in this game.",
                      "I'm like a character straight out of Shakespeare's tragedy, \n"
                      "but this time I'm the one writing the ending.\n"]

npc_inner_thoughts_german = ["Ich habe eine Idee... aber es könnte riskant sein!",
                             "Meine Mutter hat immer gesagt: 'Spiele nicht mit deinem Leben', aber sie hat mich "
                             "offensichtlich nie getroffen.",
                             "Ich war schon immer ein Mann der Worte, aber dieses Hangman-Spiel "
                             "bringt mich an meine Grenzen.\n "
                             "Vielleicht sollte ich mich lieber meinem üblichen Hobby widmen, d"
                             "iabolische Pläne zu schmieden, um die Welt zu erobern.\n "
                             "Ha ha ha! Nur ein Scherz... oder auch nicht?",
                             "Ich war noch nie jemand, der fair spielt, \n"
                             "also benutze ich meine böse Intelligenz, um dieses Hangman-Rätsel zu knacken.\n "
                             "Und sobald ich es geschafft habe, werde ich die perfekte Rache gegen "
                             "die Gutgläubigen haben, die meinen letzten Plan vereitelt haben.",
                             "Ich hatte einen Schwarm für Shakespeare, aber jetzt habe ich einen Schwarm dafür, "
                             "meine Gegner in Hangman zu vernichten.",
                             "Mein Familienstammbaum ist verdreht wie ein Strick, aber wenigstens bin ich derjenige, "
                             "der das Seil hält.",
                             "Ich bin vielleicht ein Bösewicht, aber ich habe immer noch ein gutes Gespür für Worte. "
                             "Schauen wir mal...\n"
                             "'E' ist eine gute Wahl... und 'O'... komm schon, denk nach, du verdrehtes Genie, "
                             "denk nach!",
                             "Ich habe mich Superhelden gegenübergestellt, aber dieses Hangman-Spiel ist meine "
                             "bisher größte Herausforderung.\n "
                             "Verflucht sei das Alphabet! Warum musst du so knifflig sein?",
                             "Hangman? Eher Hang-Bösewicht!"
                             "Ich werde dieses Puzzle lösen und dann meinen nächsten teuflischen Plan aushecken.\n "
                             "Nichts kann mich jetzt aufhalten!",
                             "Ah, die süße Vorfreude auf das Schafott des Henkers. \n"
                             "Aber da ist etwas anders an Jeff.\n "
                             "Er ist nicht wie die anderen. Ich hasse es fast, ihn gehen zu sehen...fast.",
                             "Ich habe Sterbliche seit Jahrhunderten hingerichtet, "
                             "aber bei Jeff ist etwas faszinierendes.\n "
                             "Vielleicht ist es sein Witz, oder seine Listigkeit, oder... na ja, egal."
                             " Lass uns das hier einfach hinter uns bringen, sollen wir?",
                             "Als unsterblicher Henker habe ich alles gesehen. "
                             "Und ehrlich gesagt, ich habe genug davon.\n "
                             "Ich möchte jetzt jemanden zum Reden haben, anstatt ständig "
                             "in meinem eigenen Kopf festzustecken.\n "
                             "Ich meine, was bringt es, ein göttliches Wesen zu sein, "
                             "wenn man das Leben nicht einmal genießen kann?",
                             "Früher habe ich mich über die Schreie der Verdammten gefreut, "
                             "aber jetzt fühlt es sich nur noch wie eine Pflicht an.\n "
                             "Wenn ich nur jemanden hätte, mit dem ich meine Gedanken teilen könnte, "
                             "anstatt sie immer mit meiner Klinge zu ersticken.",
                             "Ich bin seit Jahrhunderten hier und habe alles gesehen. \n",
                             "Sie sagen, dass der Strick des Henkers ein Symbol für Gerechtigkeit ist, "
                             "aber für mich ist er ein Symbol für Macht.",
                             "Ich habe die Träume vieler heimgesucht, aber jetzt ist es an der Zeit, "
                             "die Realität meines nächsten Opfers zu heimsuchen.",
                             "Man sagt, dass der Tod der große Ausgleicher ist,\n"
                             "aber ich sehe mich lieber als den großen Unterscheider.",
                             "Ich diskriminiere nicht bei meinen Opfern. Reich, arm, schuldig, unschuldig...\n"
                             "alle enden am Strick des Henkers."
                             "Als unsterblicher göttlicher Henker habe ich alles gesehen. Den Schmerz, "
                             "das Leiden, die Schreie.\n"
                             "Aber was würde ich nicht geben für nur einen Moment des Friedens,\n"
                             "eine Chance, mit jemandem zu sprechen, der die Last meines Daseins versteht. "
                             "Aber da Sie das gewählt haben... sind Sie es nicht.",
                             "Ich hatte einmal einen Hund, der besser buchstabieren konnte als die meisten Menschen. \n"
                             "Schade, dass er mit meiner Ex-Frau und den Kindern weggelaufen ist.",
                             "Ich brauche keinen Grund, ein weiteres Opfer zu fordern. Es ist einfach das, "
                             "was ich tue. Und ich mache es gut.",
                             "Mein Therapeut sagt, ich habe ein zwanghaftes Bedürfnis nach Kontrolle, \n"
                             "aber sie ist nicht diejenige, die die Macht in diesem Spiel hat.",
                             "Ich bin wie eine Figur direkt aus Shakespeares Tragödie, \n"
                             "aber dieses Mal schreibe ich das Ende.",
                             "Ich habe die Träume vieler heimgesucht, aber jetzt ist es an der Zeit, "
                             "die Realität meines nächsten Opfers zu heimsuchen.",
                             "Man sagt, dass der Tod der große Ausgleicher ist,\n"
                             "aber ich sehe mich lieber als den großen Unterscheider.",
                             "Ich diskriminiere nicht bei meinen Opfern. Reich, arm, schuldig, unschuldig...\n"
                             "alle enden am Strick des Henkers."
                             "Als unsterblicher göttlicher Henker habe ich alles gesehen. Den Schmerz, "
                             "das Leiden, die Schreie.\n"
                             "Aber was würde ich nicht geben für nur einen Moment des Friedens,\n"
                             "eine Chance, mit jemandem zu sprechen, der die Last meines Daseins versteht. "
                             "Aber da Sie das gewählt haben... sind Sie es nicht.",
                             "Ich hatte einmal einen Hund, der besser buchstabieren konnte als die meisten Menschen. \n"
                             "Schade, dass er mit meiner Ex-Frau und den Kindern weggelaufen ist.",
                             "Ich brauche keinen Grund, ein weiteres Opfer zu fordern. "
                             "Es ist einfach das, was ich tue. Und ich mache es gut.",
                             "Mein Therapeut sagt, ich habe ein zwanghaftes Bedürfnis nach Kontrolle, \n"
                             "aber sie ist nicht diejenige, die die Macht in diesem Spiel hat.",
                             "Ich bin wie eine Figur direkt aus Shakespeares Tragödie, \n"
                             "aber dieses Mal schreibe ich das Ende."]

# thoughts of the computer when a strategy is used

npc_general = ["Hmm, a challenging word you have chosen. \n"
               "But do you have the guts to face the consequences if I guess it correctly? \n"
               "Think carefully before you answer, for your life is at stake here. Remember, \n"
               "the game of hanging man is not for the faint of heart.",
               "Interesting choice of letters. But I see you have left some crucial ones out. \n"
               "Perhaps you are trying to outsmart me? But I assure you, I am not easily fooled.\n"
               "I have played this game with many before you, and I have yet to lose.",
               "You think you have me stumped, don't you? But I am a master of deduction.\n "
               "I can see the patterns in your word, the subtle hints that you have left for me to follow.\n"
               "You may think you have the upper hand, but I assure you, the tables will turn soon enough.",
               "A valiant effort, but alas, not good enough. \n"
               "You should have chosen a simpler word, one that would not have tested my skills to the limit. \n"
               "But I suppose it is too late for regrets now. The noose is waiting, "
               "and you have no choice but to accept your fate.",
               "Ah, I see what you were trying to do there. \n"
               "A clever attempt to mislead me, but ultimately unsuccessful.\n"
               "You should have known better than to challenge me, for I am the executioner,\n"
               "and I always get my way. Now, let us proceed to the hanging, shall we?",
               "I'll have you know, I have a PhD in Hangmanology. You don't stand a chance.",
               "I've always been bad at using a dictionary, "
               "but that just gives me more time to think of clever ways to end this game.",
               "I may have lost my family, but I still have my trusty dictionary. You're in trouble now.",
               ]

npc_general_german = ["Hmm, ein herausforderndes Wort hast du gewählt. \n"
                      "Aber hast du den Mut, die Konsequenzen zu tragen, wenn ich es richtig errate? \n"
                      "Überlege dir sorgfältig, bevor du antwortest, denn hier steht dein Leben auf dem Spiel. Denk "
                      "daran, \n"
                      "das Spiel Galgenmännchen ist nichts für schwache Nerven.",
                      "Interessante Wahl der Buchstaben. Aber ich sehe, dass du einige entscheidende ausgelassen "
                      "hast. \n"
                      "Vielleicht versuchst du, mich zu übertreffen? Aber ich versichere dir, "
                      "ich bin nicht leicht zu täuschen.\n"
                      "Ich habe dieses Spiel mit vielen vor dir gespielt und noch nie verloren.",
                      "Du denkst, du hast mich festgenagelt, oder? Aber ich bin ein Meister der Deduktion.\n "
                      "Ich kann die Muster in deinem Wort sehen, die subtilen Hinweise, "
                      "die du für mich hinterlassen hast, um zu folgen.\n"
                      "Du magst denken, dass du die Oberhand hast, aber ich versichere dir, d"
                      "ie Karten werden sich bald genug wenden.",
                      "Ein tapferer Versuch, aber leider nicht gut genug. \n"
                      "Du hättest ein einfacheres Wort wählen sollen, eins, "
                      "das meine Fähigkeiten nicht bis zum Äußersten getestet hätte. \n"
                      "Aber ich nehme an, es ist jetzt zu spät für Reue. Der Strick wartet, "
                      "und du hast keine Wahl, als dein Schicksal zu akzeptieren.",
                      "Ah, ich sehe, was du da versucht hast. \n"
                      "Ein cleverer Versuch, mich in die Irre zu führen, aber letztendlich erfolglos.\n"
                      "Du hättest besser wissen müssen, als mich herauszufordern, denn ich bin der Henker,\n"
                      "und ich bekomme immer, was ich will. Nun lasst uns zum Aufhängen übergehen, sollen wir?",
                      "Ich habe einen Doktortitel in Galgenmännchenologie. Du hast keine Chance.",
                      "Ich war schon immer schlecht darin, ein Wörterbuch zu benutzen, "
                      "aber das gibt mir nur mehr Zeit, um clevere Möglichkeiten zu überlegen, dieses Spiel zu beenden.",
                      "Ich habe zwar meine Familie verloren, "
                      "aber ich habe immer noch mein treues Wörterbuch. Du bist jetzt in Schwierigkeiten.", ]

# ------------------------------------------------------
# Variables needed for the game

# hangman art (Source: https://ascii.co.uk/art/hangman , Access: 07.05.23)
hangman_art = " _\n| |\n| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __\n" \
              "| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ \n| | | | (_" \
              "| | | | | (_| | | | | | | (_| | | | |\n|_| |_|\__,_|_| |_|\__," \
              " |_| |_| |_|\__,_|_| |_|\n                    __/ |\n            " \
              "       |___/\n"

# player win art (Source: created with: https://www.patorjk.com/software/taag/ , Access: 07.05.23)
player_art_win = "_____.___.              .__                                                ._. \n" \
                 "\__  |   | ____  __ __  |  |__ _____ ___  __ ____   __  _  ______   ____   | | \n" \
                 " /   |   |/  _ \|  |  \ |  |  \\__  \\  \/ // __ \  \ \/ \/ /  _ \ /    \  | | \n" \
                 " \____   (  <_> )  |  / |   Y  \/ __ \\   /\  ___/   \     (  <_> )   |  \  \| \n" \
                 " / ______|\____/|____/  |___|  (____  /\_/  \___  >   \/\_/ \____/|___|  /  __ \n" \
                 " \/                          \/     \/          \/                     \/   \/ \n"

# art for when the player has lost, (Source: https://www.asciiart.eu/mythology/grim-reapers,
# Access: 11.05.23, removed penis)
npc_art_win = "                                         \n" \
              "              ...                    You \n" \
              "             ;::::;                  have\n" \
              "           ;::::; :;                 lost.\n" \
              "         ;:::::'   :;                       \n" \
              "        ;:::::;     ;.                   I will now fulfill\n" \
              "       ,:::::'       ;           OOO\    my duty as hangman.\n" \
              "       ::::::;       ;          OOOOO\ \n" \
              "       ;:::::;       ;         OOOOOOOO \n" \
              "      ,;::::::;     ;'         / OOOOOOO \n" \
              "    ;:::::::::`. ,,,;.        /  / DOOOOOO \n" \
              "  .';:::::::::::::::::;,     /  /     DOOOO \n" \
              " ,::::::;::::::;;;;::::;,   /  /        DOOO \n" \
              ";`::::::`'::::::;;;::::: ,#/  /          DOOO \n" \
              ":`:::::::`;::::::;;::: ;::#  /            DOOO\n" \
              "::`:::::::`;:::::::: ;::::# /              DOO\n" \
              "`:`:::::::`;:::::: ;::::::#/               DOO\n" \
              " :::`:::::::`;; ;:::::::::##                OO\n" \
              " ::::`:::::::`;::::::::;:::#                OO\n"

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
challenge_word = "ErrorNotGivenOther"
# the secret word, to guess or to e guessed
secret_word = "ErrorSecretWordWasntChosen"
# Variable that is the current guess / chosen word
guess: str
# letter of the current guess
guess_player: str
# variable value used to distinguish between difficulty level
strategy_value = int
# string used for language_identification
hard_mode_lang = str

# --------------------------------------------------
# Select the word function


def select_word(words):
    # function to select a word from a list.
    # it uses the random module to help with the random word pick
    return random.choice(words).lower()


# test to see if a random word is selected from the lists
# print(select_word(presidents))

# -----------------------------------------------------
# function to check if users challenge word has a number in it, uses regex to include "-"
# function is used when challenge_word is created after junction of first_choice

def are_there_numbers(word):
    return any(char.isdigit() for char in word)


# -----------------------------------------------------
# def function to use for the underscores as "unknown" letters

def pri_secret_word(word, gues_letters):
    # this is used to print the missing letters with an _ and the known letters fittingly
    # inspiration found in: https://codefather.tech/blog/hangman-game-python/
    # "end" used so the print function writes in one line
    for letter in word:
        if letter in gues_letters:
            print(" {} ".format(letter), end="")
        else:
            print(" _ ", end="")
    print("\n")


# ------------------------------------------
# used repeating
def give_me_a_value_inbetween(value1: int, value2: int, language_eng: bool, start_of_game: bool) -> int:
    # Function for choosing a letter between two values
    erg = -1
    while erg <= value1 or erg > value2:
        # A while-loop is used to stop the user from ending the game with anything not allowed,
        # except is used to prevent errors
        try:
            if start_of_game:
                erg = int(input("\nEnter your choices number ... Geb die Nummer deiner Entscheidung ein: "))
                print("")
                start_of_game = False
            elif language_eng:
                # User is presented with the choice to choose between playing the game or choosing the computers word
                erg = int(input("\nEnter your choices number: "))
                print("")
            else:
                # User is presented with the choice to choose between playing the game or choosing the computers word
                erg = int(input("\nGebe die Zahl deiner Entscheidung ein: "))
                print("")
        except:
            if language_eng:
                print("That is not an option... and you know it!")
            else:
                print("Das war keine Möglichkeit! Nochmal!")
    return erg


# -----------------------------------------
# these functions are either for the player to guess letters or for the
# computer to do so with different difficulty settings

def guess_player_letter(language_eng):
    # reoccurring function for guessing a letter as the PLAYER
    while True:
        print("-----------------------------------")
        if language_eng:
            print(select_word(choose), end="")
        else:
            print(select_word(choose_german), end="")
        guess_func = str(input(": "))
        print("-----------------------------------")
        if len(guess) > 1 or not guess.isalpha():
            if language_eng:
                print("\nYou fool of a tuck, only single letters are to be guessed. Do you want to break"
                      "the simulation?... go again... this time remember the rules of only one letter at a time!")
            else:
                print("\nDu Möchtegern-Hobbit, es darf nur ein einzelner Buchstabe geraten werden.\n "
                      "Möchtest du die Simulation zerstören? Versuche es erneut und denke daran, "
                      "dass nur ein Buchstabe auf einmal geraten werden darf!")

        if len(guess) == 1 & guess.isalpha():
            break
    return guess_func.lower()


def guess_computer_letter(language_eng):
    # reoccurring function for guessing a letter as the NPC (Executioner) does
    guess = select_word(alphabet)
    if language_eng:
        print("\n*The Executioner looks into the distance... thinking hard...*")
    else:
        print("\nDer Henker schaut nachdenklich in die Ferne...")
    time.sleep(2)
    print("-----------------------------------------\n")
    if language_eng:
        print(select_word(npc_inner_thoughts))
    else:
        print(select_word(npc_inner_thoughts_german))
    print("\n-----------------------------------------")
    time.sleep(2)
    return guess


def guess_computer_letters_strategy(language_eng, gues_let_func: list):
    # this reoccurring functions uses a simple vowel-first strategy to solve the user input words
    # https://pynative.com/python-weighted-random-choices-with-probability/
    # used for inspiration for guesses with probability
    # used for probabilities: https://www.wordcheats.com/blog/most-used-letters-in-english
    while True:
        in_function_guess = random.choices(alphabet, weights=(8.4966, 2.0720, 4.5388, 3.3844, 11.1607,
                                                              1.8121, 2.4705, 3.0034, 7.5448, 0.1965,
                                                              1.1016, 5.4893, 3.0129, 6.6544, 7.1635,
                                                              3.1671, 0.1962, 7.5809, 5.7351, 6.9509,
                                                              3.6308, 1.0074, 1.2899, 0.2902, 1.7779,
                                                              0.2722), k=1)
        if in_function_guess in guessed_letters:
            continue
        if in_function_guess != secret_word:
            break

    print("\n*The Executioner looks into the distance... thinking real hard...*")
    time.sleep(2)
    print("-----------------------------------------\n")
    if language_eng:
        print(select_word(npc_general))
    else:
        print(select_word(npc_general_german))
    print("\n-----------------------------------------")
    time.sleep(2)
    in_function_guess = str(in_function_guess[0])
    return in_function_guess


# ----------------------------------------------

def open_dictionary(language):
    # opening the dictionary in read mode
    if language == "german":
        my_dict = open("words_german_excel.txt", "r")
    else:
        my_dict = open("words_alpha_excel.txt", "r")

    # reading the files
    data = my_dict.read()

    # replacing end splitting the text
    # when newline ('\n') is seen.

    data_dict_list = data.split("\n")

    return data_dict_list


# ----------------------------------------------

def high_strategy_dictionary(pydict: dict, gues_let: list, rem_let: list, language_eng):
    print("\n*The Executioner looks into the distance... thinking hard...*")
    time.sleep(2)
    print("-----------------------------------------\n")
    if language_eng:
        print(select_word(npc_general))
    else:
        print(select_word(npc_general_german))
    print("\n-----------------------------------------")
    time.sleep(2)

    # Creating a skeleton dict without positional arguments.
    # Add onto the length of lists of corresponding key:value-pairs
    # The biggest elements value gets chosen to be the high_guess

    # Variables

    empty_in_func_dict = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }

    length_dict = dict()

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


def iterate_dict_to_sol_dict(real_dict: list, ghostly_solv_dict: dict):
    # I take the "sliced by len(secretword)"-dictionary "short_dict" and iterate over each of its strings.
    # I want to add, at each element, the index of its current word to the value list of
    # the current element corresponding empty dict key.
    # the empty dict was created using letter_frequency_struct_maker,
    # and only holds elements up to the length of the secret word,
    # similar to how sliced dict only holds words as a list that are as long as secret word

    # Question/Steps:
    # I want to go through a list of words with identical length and iterate over each string in it.
    # If it finds the letter "t" at position "4", I want to put the index of the word in the list into a dictionary
    # value where they key corresponds to "t4". the solv_struct starts at "a0". so the word from the
    # example would have to be smth like "aaaataa"

    # Good to know Info and where I got it:
    # https://stackoverflow.com/questions/538346/iterating-each-character-in-a-string-using-python
    # Access on the fifth of May 2023
    # If you need access to the index as you iterate through the string, use enumerate():
    # >>> for i, c in enumerate('test'):
    # ...     print i, c
    # ...
    # 0 t
    # 1 e
    # 2 s
    # 3 t

    # in the wise words of yoda in a theme park: a lot of loops these are
    for index, word in enumerate(real_dict):
        try:
            # loops through list (real sliced dictionary)
            for position, letter in enumerate(word):
                # loops through all letters at each position and adds
                # onto values of corr. key:value-pairs
                ghostly_solv_dict["{0}{1}".format(letter, position)].append(index)
                # Vorbild: opposite_keys.append("a{0}".format(number))
        except KeyError:
            # to over-go errors produced by a letter not being existent anymore
            continue

    return ghostly_solv_dict  # full solving_dict


def thinner_the_sliced_dict(eunuch_dict: list, sol_dict: dict, already_guessed_let: list):
    # each time remove_letters gets a new one, which is letters not in the secret word
    # this goes and looks at solving_dict,
    # gets their index from values,
    # removes those index from sliced_dct(here eunuch_dict),
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
    #    for letter in already_guessed_let:
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


def format_the_hidden_word(sec_word, gues_letters):
    # coming from the output the user can see like "a_s_h", and make conclusions
    # based on the fact that certain words cannot be included
    # this creates a list that holds all keys that are not possible anymore
    # Question:
    # create lists of both the direct values and opposite values
    non_opposite_keys = []
    opposite_keys = []

    # puts stuff into the non_opposite_key-list
    for position, letter in enumerate(sec_word):
        if letter in gues_letters:
            non_opposite_keys.append("{0}{1}".format(letter, position))
            # creates a list of positional keys
            number = str(position)
            opposite_keys.append("a{0}".format(number))
            opposite_keys.append("b{0}".format(number))
            opposite_keys.append("c{0}".format(number))
            opposite_keys.append("d{0}".format(number))
            opposite_keys.append("e{0}".format(number))
            opposite_keys.append("f{0}".format(number))
            opposite_keys.append("g{0}".format(number))
            opposite_keys.append("h{0}".format(number))
            opposite_keys.append("i{0}".format(number))
            opposite_keys.append("j{0}".format(number))
            opposite_keys.append("k{0}".format(number))
            opposite_keys.append("l{0}".format(number))
            opposite_keys.append("m{0}".format(number))
            opposite_keys.append("n{0}".format(number))
            opposite_keys.append("o{0}".format(number))
            opposite_keys.append("p{0}".format(number))
            opposite_keys.append("q{0}".format(number))
            opposite_keys.append("r{0}".format(number))
            opposite_keys.append("s{0}".format(number))
            opposite_keys.append("t{0}".format(number))
            opposite_keys.append("u{0}".format(number))
            opposite_keys.append("v{0}".format(number))
            opposite_keys.append("w{0}".format(number))
            opposite_keys.append("x{0}".format(number))
            opposite_keys.append("y{0}".format(number))
            opposite_keys.append("z{0}".format(number))

    # takes out the known keys, so their index values persist
    for key in non_opposite_keys:
        opposite_keys.remove(key)

    return opposite_keys  # list of keys which index should be deleted


def letter_sniper(sol_dict, real_dict_list, remove_key_list):
    # this checks a specially created list of values created from the info one can get from
    # correctly guessed letters. Meaning that when a_s_h is displayed, the list used here
    # contains elements that are in opposition, like all keys not a0, but at position 0.

    remove_index_list = []

    # goes through the sol_dict and gets the keys, then for each key iterates through the remove_key_list
    # and checks if they are the same. If they are the same, it adds the sol_dict keys values, which are index values,
    # to the remove_index_list

    for key, value in sol_dict.items():
        for remove_key in remove_key_list:
            if key == remove_key:
                remove_index_list.append(value)

    super_sliced_dict = slice_shine_and_burn(remove_index_list, real_dict_list)

    return super_sliced_dict


def slice_shine_and_burn(list_to_burn, real_dict_list):
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


def remove_duplicates_in_list(func_list: list):
    # remove duplicates by creating a new list
    filtered_removal_list = list()
    for item in func_list:
        if item not in filtered_removal_list:
            filtered_removal_list.append(item)

    return filtered_removal_list


def slice_dict(current_dictionary, language, language_eng):
    # uses set known intervals of the length of words from the english dict and german dict
    # to save processor time
    # please make sure that length_of_secret_word is a set variable
    # (above start of who is in charge part)

    fun_dict = current_dictionary
    output_dict = dict

    if language == "english":
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
        elif length_of_secret_word <= 31:
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
                    print("mhhh, I do not know any words with 26 letters...")
                    print("I will try anyway, but I will take some more time, mortal.")
                    print("I hope you have some more left... muahahah\n")
                else:
                    print("Hmm, ich kenne keine Wörter mit 26 Buchstaben...")
                    print("Dennoch werde ich es versuchen, aber ich werde mir etwas mehr Zeit nehmen, Sterblicher.")
                    print("Ich hoffe, du hast noch etwas übrig... Muahahaha\n")
            elif length_of_secret_word == 27:
                output_dict = fun_dict[370097:370099]
            elif length_of_secret_word == 28:
                output_dict = fun_dict[370100:370101]
            elif length_of_secret_word == 29:
                output_dict = fun_dict[370102:370104]
            elif length_of_secret_word == 30:
                output_dict = fun_dict
                if language_eng:
                    print("mhhh, I do not know any words with 30 letters...")
                    print("I will try anyway, but I will take some more time, mortal.")
                    print("I hope you have some more left... muahahah\n")
                else:
                    print("Hmm, ich kenne keine Wörter mit 30 Buchstaben...")
                    print("Dennoch werde ich es versuchen, aber ich werde mir etwas mehr Zeit nehmen, Sterblicher.")
                    print("Ich hoffe, du hast noch etwas übrig... Muahahaha\n")
            elif length_of_secret_word == 31:
                output_dict = fun_dict[370105:370105]
        else:
            if language_eng:
                print("\nthat's a very long word... are you sure it exists?")
                print("\nI will try anyway, cheat.")
                print("\nIf you button-smashed, I will haunt your dreams for eternity and make sure that "
                      "in the after-life you won`t have the chance to dream.... just kidding... unless...")
            else:
                print("\nDas ist ein sehr langes Wort... bist du sicher, dass es existiert?")
                print("\nIch werde es trotzdem versuchen, Schummler.")
                print("\nWenn du wild auf den Tasten herumgehauen hast,\n"
                      "werde ich dich für die Ewigkeit heimsuchen und sicherstellen,\n"
                      "dass du im Jenseits nicht träumen wirst... nur ein Scherz... oder auch nicht...")
            output_dict = fun_dict

    elif language == "german":
        print("\nI have to admit... I haven't learned german yet... I just dont get the grammar.\n eh... los gehts")
        output_dict = fun_dict
        # TODO

    return output_dict


#          -------------------------------
def letter_frequency_structure_maker(sec_word_for_func: str, alph_in_func: list):
    # creates an array of keys of the length of secret word with the other axis being the alphabet
    # since initialising 806 possible combinations would be unnecessary.
    # all the values of the arrays are lists with the index values of the corresponding words
    # starts at a0

    sec_le = len(sec_word_for_func)
    alp_le = len(alph_in_func)
    solvstruct = {}

    for i in range(sec_le):
        for j in range(alp_le):
            solvstruct["{}{}".format(alph_in_func[j], str(i))] = []

    return solvstruct


# -----------------------------------------

def is_guess_in_secret_word(gues_letter, sec_word):
    # function that checks if letter is in secret word
    if gues_letter in sec_word:
        return True
    else:
        return False


# ----------------------------------------

# function used to put the secret_word string into a set, so we can remove duplicates and iterate easy
def get_unique_letters(word):
    return "".join(set(word))


# -----------------------------------------

def user_input_word(language_eng):
    # variables used for control while statement
    good_enough_points = False
    # as a little debug control, the user_word is originally named this
    user_word = "SomethingWentWrongInUserInputWordFunction"

    while not good_enough_points:
        # while-loop breaks when the challenge_word is good enough
        if language_eng:
            user_word = str(input("\n... so be it... write your human word on this card and do not tell me: "))
        else:
            user_word = str(input("\n... so sei es... schreib dein menschliches Wort hierdrauf und sag es mir nicht: "))
        # checking the challenge_word for anything bad
        # does it have numbers in it?
        # is challenge word actually multiple words with space inbetween
        if " " not in challenge_word and not are_there_numbers(challenge_word):
            good_enough_points = True
        else:
            if language_eng:
                print("\n Narrator: Numbers??? Multiple words??? Separators?! Not in this game! "
                      "Repeat, Repeat, Repeeeeat!")
            else:
                print("\n Narrator: Zahlen??? Mehrere Wörter??? Trennzeichen?! Nicht in diesem Spiel! "
                      "Wiederholen, Wiederholen, Wiederholen!")
    return user_word


# ----------------------------------------

def games_callout(who_won, language_eng):
    # function that gives out a statement according to who won - perspective player
    if who_won == "NPC":
        print(npc_art_win)
        print("")
        time.sleep(2)
        print("---------------------------------------")
        print(select_word(npc_wins))
        print("")
        if language_eng:
            print("Narrator: The Exorcist... or was it Executioner?... has won! pity you!\n")
        else:
            print("Narrator: Der Exorzist... oder war es der Henker?... hat gewonnen! Schade für dich!\n")
        print("---------------------------------------\n")
    if who_won == "Player":
        print("---------------------------------------\n")
        print(select_word(player_wins))
        print("")
        if language_eng:
            print("Narrator: Wow! You have actually managed to win! good job you!\n")
        else:
            print("Narrator: Wow! Du hast es tatsächlich geschafft zu gewinnen! Gut gemacht!\n")
        print("")
        print(player_art_win)
        print("")
        print("---------------------------------------\n")


# -----------------------------------------
# Hangman stages as a function corresponding to the remaining_attempts

def get_hangman_stage(attempt_number):
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


# Story/Game-Opening ----------------------------

# prints the hangman logo
print(hangman_art)

print("Willkommen zu Galgenmännchen!   Welcome to Hangman!\n")
print("Choose your language / Wähle deine Sprache:\n")
print(" --- 1. English/Englisch --- 2. German/Deutsch --- ")

# call just for this one function
is_english = True
lang_decide = language = give_me_a_value_inbetween(0, 2, is_english, True)

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

first_choice = give_me_a_value_inbetween(0, 2, is_english, False)

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

    second_choice = give_me_a_value_inbetween(0, 7, is_english, False)

    # nested if statements for choosing the right secret word
    if second_choice == 1:
        secret_word = select_word(animals)
    elif second_choice == 2:
        secret_word = select_word(cities)
    elif second_choice == 3:
        secret_word = select_word(food)
    elif second_choice == 4:
        secret_word = select_word(presidents)
    elif second_choice == 5:
        secret_word = select_word(cartoon_characters)
    elif second_choice == 6:
        secret_word = select_word(hard_words)
    elif second_choice == 7:
        secret_word = select_word(animals_german)
        print("\n-----------"
              "\nah.... deutsche Tiere... jaja, guten Tag Herr Osterhase."
              "\n----------")

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
              'Although I could crush you, I want to give you a chance... to play with my prey\n.'
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

strategy_value = give_me_a_value_inbetween(0, 2, is_english, False)

if strategy_value == 3:
    print("")
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

    lang_value = give_me_a_value_inbetween(0, 2, is_english, False)

    if lang_value == 2:
        hard_mode_lang = "german"
    else:
        hard_mode_lang = "english"

print("--------------------------------")
challenge_word = user_input_word(is_english)
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

# variable used in both player and npc
length_of_secret_word = int(len(get_unique_letters(secret_word)))

# The Player is in charge:

if who_plays == "Player":

    if is_english:
        print("The letter you wish to guess has {} letter´s... do with this Information what you like.\n".format(
            len(secret_word)))
    else:
        print("Der gesuchte Buchstabe hat {} Buchstaben... mache mit dieser Information, was du willst.\n".format(
            len(secret_word)))

    while remaining_attempts > 0 and len(guessed_letters) < length_of_secret_word:
        # the while-loop runs while the attempts haven't run out and the player hasn't won

        guess = guess_player_letter(is_english)  # player takes a guess

        guess_in_secret_word = is_guess_in_secret_word(guess, secret_word)
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
                print(select_word(point_player))
                guessed_letters += guess
        else:
            if is_english:
                print("\nNo! The letter {} is not part of the secret word\n".format(guess))
            else:
                print("\nNein! Der Buchstabe {} ist nicht Teil des geheimen Wortes\n".format(guess))

            print(select_word(point_computer))
            remaining_attempts -= 1

        print(get_hangman_stage(remaining_attempts))
        pri_secret_word(secret_word, guessed_letters)

        if is_english:
            print("\n You can make {} more mistakes... I would say be careful, but I hope you lose.\n"
                  .format(remaining_attempts))
        else:
            print("\nDu hast noch {} Fehler übrig... Ich würde sagen, sei vorsichtig, "
                  "aber ich hoffe, dass du verlierst.\n".format(remaining_attempts))

    if len(guessed_letters) == len(get_unique_letters(secret_word)):
        games_callout("Player", is_english)
    else:
        games_callout("NPC", is_english)

# The Computer is in charge of guessing: ---------------------------------------------------

if who_plays == "NPC":

    length_of_secret_word = int(len(get_unique_letters(secret_word)))

    if strategy_value == 3:
        # here the version for the high-strategy computer-way, seperated for better overview

        # implemented variable outside of loop, so it doesn't load each time
        dict_before_slice = open_dictionary(hard_mode_lang)
        sliced_dict = slice_dict(dict_before_slice, hard_mode_lang, is_english)
        remove_letters = []

        while remaining_attempts > 0 and len(guessed_letters) < length_of_secret_word:
            # the while-loop runs while the attempts haven't run out and the computer hasn't won

            empty_solv_dict = letter_frequency_structure_maker(secret_word, alphabet)

            # creates a dict where frequency of elements at letter positions
            # are measured for remaining words in sliced_dict
            solving_dict = iterate_dict_to_sol_dict(sliced_dict, empty_solv_dict)

            # computer takes a guess based on the highest amount of an element it found in solving_dict
            # if sliced_dict empty, meaning no known words fit parameters of secret word, use medium strategy
            if len(sliced_dict) == 0:
                guess = guess_computer_letters_strategy(is_english, guessed_letters)
            else:
                guess = high_strategy_dictionary(solving_dict, guessed_letters, remove_letters, is_english)

            # gives out a True or False value which we store in the variable and use in the following if statements
            guess_in_secret_word = is_guess_in_secret_word(guess, secret_word)

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
                    print(get_hangman_stage(remaining_attempts))
                    guessed_letters.append(guess)
                    pri_secret_word(secret_word, guessed_letters)

                else:  # meaning that the guess is in secret word, but hasn't been guessed yet
                    if is_english:
                        print("\nI have been right! The letter {} is part of your secret filthy word\n".format(guess))
                    else:
                        print("\nIch habe recht gehabt! Der Buchstabe {} ist "
                              "Teil deines geheimen Wortes.\n".format(guess))
                    print(select_word(point_computer))
                    print(get_hangman_stage(remaining_attempts))
                    guessed_letters.append(guess)
                    pri_secret_word(secret_word, guessed_letters)
                    # creates list that is used in understanding where a known element is in the secret word
                    half_hidden_word_list = format_the_hidden_word(secret_word, guessed_letters)
                    # the just created list and its opposite are used in eliminating
                    # the words that contradict known positional letters
                    sliced_dict = letter_sniper(solving_dict, sliced_dict, half_hidden_word_list)

            else:  # meaning that the letter is not part of the word.
                if is_english:
                    print("\n Nooooo.... The letter {} is not part of your word...\n".format(guess))
                else:
                    "\n Nein! Der Buchstabe {} ist nicht Teil deines Wortes ...\n".format(guess)
                print(select_word(point_player))
                remaining_attempts -= 1
                remove_letters.append(guess)
                sliced_dict = thinner_the_sliced_dict(sliced_dict, solving_dict, remove_letters)
                print(get_hangman_stage(remaining_attempts))
                pri_secret_word(secret_word, guessed_letters)

            # prevents duplicates in the guessed letters list,
            # in case smth goes wrong, as to not create more systematic bugs
            guessed_letters = remove_duplicates_in_list(guessed_letters)

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
                guess = guess_computer_letter(is_english)  # computer takes a guess
            else:
                guess = guess_computer_letters_strategy(is_english, guessed_letters)
                # computer takes a structured guess with a higher success chance

            guess_in_secret_word = is_guess_in_secret_word(guess, secret_word)
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
                    print(select_word(point_computer))
                    guessed_letters += guess
            else:
                if is_english:
                    print("\n Nooooo.... The letter {} is not part of your word...\n".format(guess))
                else:
                    "\n Nein! Der Buchstabe {} ist nicht Teil deines Wortes ...\n".format(guess)
                print(select_word(point_player))
                remaining_attempts -= 1

            print(get_hangman_stage(remaining_attempts))
            pri_secret_word(secret_word, guessed_letters)

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

    if len(guessed_letters) == len(get_unique_letters(secret_word)):
        # Function that celebrates the victory of whoever has won
        games_callout("NPC", is_english)
    else:
        games_callout("Player", is_english)

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

restart = give_me_a_value_inbetween(0, 2, is_english, False)

if restart == "1":
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
elif restart == "2":
    print("\nThe matrix will be closed...")
    sys.exit(0)
