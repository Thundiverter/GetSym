import pyperclip

print('The most useful symbols')
print('0 - «»\n1 - §\n2 - ÄäÖöÜüß\n3 - —\n4 - •')

def gen():
    number = input()
    if number == '0':
        pyperclip.copy('«»')
    elif number == '1':
        pyperclip.copy('§')
    elif number == '2':
        pyperclip.copy('ÄäÖöÜüß')
    elif number == '3':
        pyperclip.copy('—')
    elif number == '4':
        pyperclip.copy('•')
    else:
        print('Not found')
    
    gen()

gen()

