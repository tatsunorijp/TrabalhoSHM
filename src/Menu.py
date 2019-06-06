import Functions as f
import Save as save
import scipy.io.wavfile as wavfile
import Save as save

def main():
    inputFileName = input("Digite o nome do arquivo de entrada\n")
    extension = inputFileName.split('.')

    inputFileName = "resources/inputs/" + inputFileName

    if (extension[1] == "txt"):
        file = open(inputFileName, 'r')
        text = file.read()

        morseCode = f.textToMorse(text)
        binaryCode = f.morseToBinary(morseCode)
        f.binaryToWav(binaryCode)

        save.saveMorse(morseCode)
        save.saveBin(binaryCode)

        file.close()

    elif extension[1] == "morse":
        file = open(inputFileName, 'r')
        morseCode = file.read()

        text = f.morseToText(morseCode)
        binaryCode = f.morseToBinary(morseCode)
        f.binaryToWav(binaryCode)

        save.saveBin(binaryCode)
        save.saveText(text)

        file.close()

    elif extension[1] == "wav":
        freq, data = f.wavfile.read(inputFileName)

        binaryCode = f.wavToBinary(freq, data)
        morseCode = f.binaryToMorse(binaryCode)
        text = f.morseToText(morseCode)

        save.saveText(text)
        save.saveMorse(morseCode)
        save.saveBin(binaryCode)

    else:
        print("Erro de formato de arquivo ou Arquivo não encontrado\n")
    return

main()