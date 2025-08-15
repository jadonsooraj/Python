#! python3
# pw.py- a passwork locker program to store passwords for various sites

passwords={'gmail': 'Sooraj@10082000',
           'linkedin': 'Sooraj@10082000'}


import sys,pyperclip
if len(sys.argv)<2:
    print('Usage: python pw.py[account]- copy account password')
    sys.exit()

account=sys.argv[1] #first command line arg is the account name
