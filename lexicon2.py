lexicon = {
    'north': 'direction',
    'south': 'direction',
    'east': 'direction',
    'west': 'direction',
    'down':'direction',
    'up':'direction',
    'left':'direction',
    'right':'direction',
    'go': 'verb',
    'kill': 'verb',
    'eat': 'verb',
    'the': 'stop',
    'in': 'stop',
    'of': 'stop',
    'door':'noun',
    'bear': 'noun',
    'princess': 'noun',
    'dollar': 'money',
    'pound': 'money',
    'kronor': 'money',
    'miles': 'distance',
    'km': 'distance',
    'meter': 'distance',
}

def scan(sentence):
    sentence = sentence.split()
    result = []
    for word in sentence:
        wordtype = lexicon.get(word, 'error')
        pair = (wordtype, word)

        if word in lexicon:
            result.append(pair)

        elif word not in lexicon:
            number = convert_number(word)
            if number:
                pair = ('number', number)

            elif word not in lexicon and not number:
                pair = (wordtype, word)

            result.append(pair)

    print result  # printing this to see the output
    return result

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

if __name__ == '__main__':
    sentence = raw_input('write something:> ')
    sentence = sentence.lower()

    scan(sentence)

