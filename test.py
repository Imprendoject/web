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

#
# import pandas as pd
#
# df = pd.read_csv('Endit.csv', encoding='utf-8-sig')
# columns = df.columns
# column1 = df.Column1[0]
# column2 = df.Column2[0]
# column3 = df.Column3[0]
# column4 = df.Column4[0]
#
# for n in range(0,9):
#     cell = df.Column2[n]
#     print(cell)
#
#
import smtplib
from flask import request, render_template, redirect, url_for, send_from_directory

msg = "kgsd lzvkxl/zjshpabiskd"

my_email = 'jsrchetansharma@gmail.com'
password = 'vzay qxxh sryp eegp'
with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs='chetansharama@gmail.com',
                        msg=f'Subject:Portfolio mail\n\n{msg}')


# def download():
#     return send_from_directory('static', 'files/Chetan_Sharma_GT.pdf')
#
#
#
#
#
# my_email = 'jsrchetansharma@gmail.com'
# password = 'vzay qxxh sryp eegp'
# with smtplib.SMTP('smtp.gmail.com') as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs='chetansharama@gmail.com',
#                         msg=f'Subject:Portfolio mail\n\n{name_replace}')

