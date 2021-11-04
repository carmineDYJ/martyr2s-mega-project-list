while True:
    word_input = input('Try to enter a word, the program will output the pig latin form of that word\n>>> ')
    vowel = 'aeiou'
    if word_input[0] in vowel:
        word_input += 'ay'
    else:
        for index, w in enumerate(word_input):
            if w in vowel:
                word_input = word_input[index:] + word_input[:index] + 'ay'
                break
        else:
            word_input += 'ay'
    print('The pig latin form of that word is ' + word_input)