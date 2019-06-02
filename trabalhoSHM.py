unityTime = 0.25
frequency = 440
sampleRate = 48000
sampleWidth = 16000

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

BinaryDictionary = {
    '-': '111',
    '.': '1'
}

def textToMorse(text):
    morseCode = ''
    #PARA TODOS OS CARACTERES DO TEXTO
    for char in text:

        #SE O CARACTER NÃO FOR UM ESPAÇO, ENTAO TRANSFORMA PRA BINARIO
        if char != ' ':
            morseCode += MorseDictionary[char.lower()] + ' '

        #SE NÃO SÓ ADICIONA O ESPAÇO
        else:
            morseCode += ' '

    return morseCode

def morseToText(morseCode) :
    # ADICIONA UM ESPAÇO PARA A ÚLTIMA ITERAÇÃO
    i = 0
    morseCode += ' '
    text = ''
    codeLetter = ''

    # PARA CADA CARACTER MORSE DO TEXTO MORSE
    for code in morseCode:

        # SE FOR DIFERENTE DE ESPAÇO, ENTÃO CONCATENA PARA FORMAR A LETRA
        if (code != ' '):
            i = 0
            codeLetter += code

        # SE FOR UM ESPAÇO, SIGNIFICA FIM DE LETRA EX: (.- . .-.)
        else:
            i += 1

            # SE ACHAR DOIS ESPAÇO SEGUIDO, SIGNIFICA FIM DE PALAVRA
            if i == 2:
                text += ' '
            else:
                # TRANSFORMA A LETRA MORSE EM LETRA NORMAL
                text += list(MorseDictionary.keys())[list(MorseDictionary.values()).index(codeLetter)]

                # ESVAZIA PARA COMECAR A PROXIMA LETRA
                codeLetter = ''

    return text

def morseToBinaryMorse(morseCode):

    binaryText = ''
    #MESMA LÓGICA DE TextToMorse
    for unit in morseCode:
        if unit != ' ':
            binaryText += BinaryDictionary[unit] + '0'
        else:
            binaryText += '0'
    return binaryText

def binaryMorseToMorse(binaryText):
    i = 0
    binaryText += '0'
    morseText = ''
    unityLetter = ''
    for code in binaryText:
        if (code != '0'):
            i = 0
            unityLetter += code
        else:
            i += 1
            if i == 2:
                morseText += ' '
            elif i == 3:
                morseText += ' '
            else:
                morseText += list(BinaryDictionary.keys())[list(BinaryDictionary.values()).index(unityLetter)]
                unityLetter = ''
    #NA ULTIMA ITERACAO ACABA SENDO ADICIONADO DOIS ESPAÇOS, ENTAO, ESSES DOIS ESPAÇOS SAO REMOVIDOS

    return morseText[:-2]

def main():
    inputFileName = input("Digite o nome do arquivo de entrada\n")
    extension = inputFileName.split('.')
    text = ""

    if (extension[1] == "txt"):
        print("arquivo txt\n")
        file = open(inputFileName, 'r')
        text = file.read()
        morseCode = textToMorse(text)
        print(morseCode)
        binaryMorse = morseToBinaryMorse(morseCode)
        print(binaryMorse)

        file.close()

    elif extension[1] == "morse":
        print("arquivo morse\n")
        file = open(inputFileName, 'r')
        binaryMorse = file.read()
        morseText = binaryMorseToMorse(binaryMorse)
        print(morseText)
        text = morseToText(morseText)
        print(text)

    elif extension[1] == "wav":
        print("arquivo wav")

    else:
        print("Erro de formato de arquivo ou Arquivo não encontrado\n")
    return

main()