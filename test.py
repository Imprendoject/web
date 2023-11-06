# from morse import MorseCode
#
# morse_code = MorseCode()
# choice = input('You want to decode or code your message Options: "D" or "C":\n').upper()
#
# if choice == 'D':
#     sentence = input('Please enter message you want to decode with spaces: ')
#     result = morse_code.decode(sentence)
#     print(result)
# elif choice == 'C':
#     sentence = input('Please enter message you want to decode: ').upper()
#     result = morse_code.coded(sentence)
#     print(result)
# else:
#     print('Wrong choice please select from options')


import pandas as pd

df = pd.read_csv('Endit.csv', encoding='utf-8-sig')
columns = df.columns
column1 = df.Column1[0]
column2 = df.Column2[0]
column3 = df.Column3[0]
column4 = df.Column4[0]

for n in range(0,9):
    cell = df.Column2[n]
    print(cell)



