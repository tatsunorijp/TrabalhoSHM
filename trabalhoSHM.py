MorseDictionary = {
        'a': '.-',  'b': '-...',    'c': '-.-.',    'd': '-..',
        'e': '.',   'f': '..-.',    'g': '--.',     'h': '....',
        'i': '..',  'j': '.---',    'k': '-.-',     'l': '.-..',
        'm': '--',  'n': '-.',      'o': '---',     'p': '.--.',
        'q': '--.-','r': '.-.',     's': '...',     't': '-',
        'u': '..-', 'v': '...-',    'w': '.--',     'x': '-..-',
        'y': '-.--','z': '--..',

        '1': '.----',   '2': '..---',   '3': '...--',   '4': '....-',
        '5': '.....',   '6': '-....',   '7': '--...',   '8': '---..',
        '9': '----.',   '0': '-----',   ' ': ' '
    }

def textToMorse(text):
    morseCode = ''
    for char in text:
        if char != ' ':
            morseCode += MorseDictionary[char.lower()] + ' '
        else:
            morseCode += ' '

    return morseCode

def morseToCode(morseCode):
    morseCode += ' '
    text = ''
    codeLetter = ''
    for code in morseCode:
        if (code != ' '):
            i = 0
            codeLetter += code
        else:
            i += 1
            if i == 2:
                text += ' '
            else:
                text += list(MorseDictionary.keys())[list(MorseDictionary.values()).index(codeLetter)]
                codeLetter = ''

    return text

inputFileName = input("Digite o nome do arquivo de entrada\n")
extension = inputFileName.split('.')
text = ""

if (extension[1] == "txt"):
    print("arquivo txt\n")
    file = open(inputFileName, 'r')
    text = file.read()

    print(textToMorse(text))

    file.close()

elif extension[1] == "morse":
    print("arquivo morse\n")
    file = open(inputFileName, 'r')
    text = file.read()
    print(morseToCode(text))

elif extension[1] == "wav":
    print("arquivo wav")