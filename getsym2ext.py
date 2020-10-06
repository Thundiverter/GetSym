import pyperclip

stringlen = 24

# this is a list of all symbols
copy = [
            '«»', '§', 'ÄäÖöÜüß', '—', '•', '⁰¹²³⁴⁵⁶⁷⁸⁹', '√', '∞', '▲►▼◄', 'Ññ', 'ÁÉÓÚáéóú', '÷', '¡¿', '£¥€₽₿',
            '™', '‹›', '©®',
            '≤≥', '∈∉', '≈≠', '〈〉', '≡', '⋮', '∫', '∝',
            '⇒⇔', '→↦', '⊃⊇⊋⊂⊆⊊', '∧∨', '¬', '∀∃', '∅', '∪⋂',
            'ℕℤℚℝℂ', '∑∏'
    ]

print('\n   Made by Thundiverter | Extended version\n   https://github.com/Thundiverter/GetSym\n')
print('   Available symbols (' + str(len(copy)) + ')')
# 'for in' generates a list of all available symbols and their id's
for i in range(len(copy)):
    spaces = ' ' * (stringlen - (len(str(i)) + len(copy[i])))
    print ('   ' + str(i) + spaces + copy[i])
print('')

def getSym():
    pyperclip.copy(copy[int(input('   Enter: '))])
    getSym()
getSym()
