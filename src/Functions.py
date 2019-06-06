import wave
import struct
import numpy as np
import scipy.io.wavfile as wavfile

unityTime = 0.25
frequency = 440
sampleWidth = 2
channels = 1

# SAMPLE RATE
rate = 48000.0

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
    #PARA TODOS OS CARACTERES DO TEXTO
    for char in text:

        # SE O CARACTER NÃO FOR UM ESPAÇO, ENTAO TRANSFORMA PRA MORSE
        if char != ' ':
            morseCode += MorseDictionary[char.lower()] + ' '

        # SE NÃO SÓ ADICIONA O ESPAÇO
        else:
            morseCode += ' '

    return morseCode[:-1]

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

def morseToBinary(morseCode):
    morseCode = morseCode.replace(".", "10")
    morseCode = morseCode.replace("-", "1110")
    morseCode = morseCode.replace("  ", "000000")
    morseCode = morseCode.replace(" ", "00")
    return morseCode

def binaryToMorse(binaryCode):
    binaryCode = binaryCode.replace("1110", "-")
    binaryCode = binaryCode.replace("10", ".")
    binaryCode = binaryCode.replace("000000", "  ")
    binaryCode = binaryCode.replace("00", " ")
    return binaryCode

def writeSignal(wavef, bit, volume):

    if (bit == '0'):
        volume = 0

    for x in range(int(unityTime * rate)):
        value = int(volume * np.sin(2 * np.pi * frequency * x / rate))
        data = struct.pack('<h', value)
        wavef.writeframesraw(data)

def binaryToWav(text):

    wav = wave.open('resources/outputs/output.wav', 'w')
    wav.setnchannels(channels)
    wav.setsampwidth(sampleWidth)
    wav.setframerate(rate)

    print("Gerando audio...")
    for char in text:
        writeSignal(wav, char, volume = 32767.0)
    wav.close()

def wavToBinary(freq, data):
    # n "TAMANHO DO BIP"
    n = int(freq * 0.25)

    matriz = np.split(data, range(n, len(data), n))

    binaryCode = ""

    # ELEMENTO 0 DA MATRIZ SEMPRE 0
    # SE FOR UMA MATRIZ SO DE ZEROS, SIGNIFICA QUE É VOLUME 0
    # SE NÃO, SIGNIFICA UM BIP (VOLUME == 32767.0)
    for vetor in matriz:
        if vetor[1] == 0:
            binaryCode += '0'
        else:
            binaryCode += '1'

    return binaryCode

