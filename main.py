import random
initial_clues_dict = {
    'ester': '_s_e_',
    'pavement': 'p_v__e_t',
    'john erinjery': 'jo_n __i_j__y',
    'jeffin jose thalakkottoor': 'j_f_in __s_ th_l___ot_o__'
}
number_per_letter = {}
for i in initial_clues_dict.keys():
    sum = 0
    number_per_letter[i] = {}
    for j in i:
        sum = i.count(j)
        number_per_letter[i][j] = sum
clue_key = random.randint(1, len(initial_clues_dict.keys()))
word = list(initial_clues_dict.keys())[clue_key - 1]
clue = initial_clues_dict[word]
current_user_guess = clue

while True:
    if current_user_guess == word:
        print(word.title())
        print('VICTORY!')
        print('Thanks for Playling!')
        break
    print(f'\n{current_user_guess}')
    guess = input('Guess : ').lower()
    num_guessed_in_current_user_guess = 0
    for i in current_user_guess:
        if i == guess:
            num_guessed_in_current_user_guess += 1
    if guess in word:
        if num_guessed_in_current_user_guess < number_per_letter[word][guess]:
            print('good guess!')
            index_list = []
            start = 0
            index = 0
            for i in word:
                if i == guess:
                    index = word.index(i, start)
                    start = index + 1
                    index_list.append(index)
            start = 0
            index = 0
            for i in current_user_guess:
                if i == '_':
                    if (c := current_user_guess.index(i, start)) in index_list:
                        current_user_guess = current_user_guess[:c] + \
                            guess + current_user_guess[c+1:]
                        break
                    else:
                        start = c + 1
        else:
            print('wrong guess!')
    else:
        print('wrong guess!')
