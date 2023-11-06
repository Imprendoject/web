class MorseCode:
    def __init__(self):
        self.MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


    def coded(self,sentence):
        morse_store = []
        for char in sentence:
            if char == ' ':
                char = '\n'
                morse_store += char
            elif char in self.MORSE_CODE_DICT:
                morse = self.MORSE_CODE_DICT[char]
                morse_store.append(morse)
            else:
                print(f'Character {char} is wrong input')
        return f'Your coded message:\n{morse_store}'


    def decode(self,codes):
        codes = codes.split(' ')
        decoded = ''
        for code in codes:
            if code in self.MORSE_CODE_DICT.values():
                for letter, morse_code in self.MORSE_CODE_DICT.items():
                    if morse_code == code:
                        decoded += letter

        return f'You decoded characters:\n{decoded}'






####################################################################################
# MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
#                    'C': '-.-.', 'D': '-..', 'E': '.',
#                    'F': '..-.', 'G': '--.', 'H': '....',
#                    'I': '..', 'J': '.---', 'K': '-.-',
#                    'L': '.-..', 'M': '--', 'N': '-.',
#                    'O': '---', 'P': '.--.', 'Q': '--.-',
#                    'R': '.-.', 'S': '...', 'T': '-',
#                    'U': '..-', 'V': '...-', 'W': '.--',
#                    'X': '-..-', 'Y': '-.--', 'Z': '--..',
#                    '1': '.----', '2': '..---', '3': '...--',
#                    '4': '....-', '5': '.....', '6': '-....',
#                    '7': '--...', '8': '---..', '9': '----.',
#                    '0': '-----', ', ': '--..--', '.': '.-.-.-',
#                    '?': '..--..', '/': '-..-.', '-': '-....-',
#                    '(': '-.--.', ')': '-.--.-'}
#
#
# def coded(sentence):
#     morse_store = []
#     for char in sentence:
#         if char == ' ':
#             char = '\n'
#             morse_store += char
#         elif char in MORSE_CODE_DICT:
#             morse = MORSE_CODE_DICT[char]
#             morse_store.append(morse)
#         else:
#             print(f'Character {char} is wrong input')
#     return f'Your coded message:\n{morse_store}'
#
#
# def decode(codes):
#     codes = codes.split(' ')
#     decoded = ''
#     for code in codes:
#         if code in MORSE_CODE_DICT.values():
#             for letter, morse_code in MORSE_CODE_DICT.items():
#                 if morse_code == code:
#                     decoded += letter
#
#     return f'You decoded characters:\n{decoded}'
#
#
# choice = input('You want to decode or code your message Options: "D" or "C":\n').upper()
#
# if choice == 'D':
#     sentence = input('Please enter message you want to decode with spaces: ')
#     result = decode(sentence)
#     print(result)
# elif choice == 'C':
#     sentence = input('Please enter message you want to decode: ').upper()
#     result = coded(sentence)
#     print(result)
# else:
#     print('Wrong choice please select from options')