# Wordle!
#
# Rules:
# // 1. The word that you have to guess is a 5 letter long word.
# // 2. You get 6 tries.
# // 3. For each guess, you are given a hint:
# //    - correct letter in wrong place gets a yellow background
# //    - correct letter in the right place gets a green background
# //    - wrong letter gets a grey background
# work of the days map r:0 e:1 a:2 d:3 y:4
from collections import defaultdict
def wordle(wordOfTheDay):
    guesses = ['rapid', 'ready']
#   r: (0, 4)
#   //
#   // ['rapid', 'store', 'cross', 'reach', 'peace', 'ready'];

#   // guess the inputs, for example:
#   //
#   // guess('rapid'); // this should print output the results, for example:
#   //   1st guess:
#   //     'r' - green
#   //     'a' - yellow
#   //     'p' - grey
#   //     'i' - grey
#   //     'd' - yellow
    word_day_map = defaultdict(list)

    # word_day_map(r:0, e:1, a:2, d:3, y:4)
    for guess in guesses: # rapid
        for i in range(5):
            word_day_map[wordOfTheDay[i]].append(i)
        guess_word_map = {}
        for index in range(5): # 0 r 1 e
            if guess[index] in word_day_map: # d 4
                indexes = word_day_map[guess[index]] #[3] d
                if indexes[0] == index: # 0 4
                    guess_word_map[guess[index]] = 'green' # r : green
                    indexes.pop(0)
                else:
                    guess_word_map[guess[index]] = 'yellow' # d: yellow
            else:
                guess_word_map[guess[index]] = 'grey'
        print(f"{guess} \n")
        for key, value in guess_word_map.items():
            print(f" {key} - {value}" )
# result

# rapid

#  r - green
#  a - yellow
#  p - grey
#  i - grey
#  d - yellow
# ready

#  r - green
#  e - green
#  a - green
#  d - green
#  y - green


# // run
wordle('ready')