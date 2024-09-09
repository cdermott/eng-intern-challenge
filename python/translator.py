import sys

# Braille alphabet map
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......'
}

# Braille number maps
braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Braille special characters map
capital_follows = '.....O'
number_follows = '.O.OOO'

# Braille back to English Map
reverse_braille_alphabet = {v: k for k, v in braille_alphabet.items()}
reverse_braille_numbers = {v: k for k, v in braille_numbers.items()}

def is_braille(s):
    return all(c in 'O.' for c in s)

def translate_to_braille(text):
    braille_output = []
    number_mode = False
    for char in text:
        if char.isdigit():
            if not number_mode:
                braille_output.append(number_follows)
                number_mode = True
            braille_output.append(braille_numbers[char])
        else:
            if number_mode:
                number_mode = False
            if char.isalpha():
                if char.isupper():
                    braille_output.append(capital_follows)
                    braille_output.append(braille_alphabet[char.lower()])
                else:
                    braille_output.append(braille_alphabet[char])
            elif char == ' ':
                braille_output.append(braille_alphabet[' '])
    return ''.join(braille_output)

def translate_to_english(braille):
    english_output = []
    number_mode = False
    i = 0
    while i < len(braille):
        current_symbol = braille[i:i+6]
        if current_symbol == number_follows:
            number_mode = True
            i += 6
            continue
        elif current_symbol == capital_follows:
            i += 6
            current_symbol = braille[i:i+6]
            english_output.append(reverse_braille_alphabet[current_symbol].upper())
        elif number_mode:
            english_output.append(reverse_braille_numbers[current_symbol])
        else:
            english_output.append(reverse_braille_alphabet[current_symbol])
        i += 6
    return ''.join(english_output)

def braille_translator(input_texts):
    concatenated_input = ' '.join(input_texts) 
    return translate_to_braille(concatenated_input)

if __name__ == "__main__":
    input_texts = sys.argv[1:]
    print(braille_translator(input_texts))
