import pyperclip

# this is the list of all symbols
symbols = [
            '«»', '§', 'ÄäÖöÜüß', '—', '•', '⁰¹²³⁴⁵⁶⁷⁸⁹', '√', '∞', '▲►▼◄', 'Ññ', 'ÁÉÓÚáéóú', '÷', '¡¿', '£¥€₽₿',
            '™', '‹›', '©®'
        ]

# width of the list of available characters (in characters)
stringlen = 24

# program
print('\n   Available symbols (' + str(len(symbols)) + ')')
# 'for in' generates a list of all available symbols and their id's
for i in range(len(symbols)):
    print ('   ' + str(i) + ' ' * (stringlen - (len(str(i)) + len(symbols[i]))) + symbols[i])
print('')
def getSym():
    pyperclip.copy(symbols[int(input('   Enter: '))])
    getSym()
getSym()