
outputPath = "resources/outputs/"

def saveText(text):
    outputText = open(outputPath + "text.txt", "w")
    outputText.write(text)
    outputText.close()

def saveMorse(morseCode):
    outputMorse = open(outputPath + "morseCode.morse", "w")
    outputMorse.write(morseCode)
    outputMorse.close()

def saveBin(binaryCode):
    outputBinary = open(outputPath + "binaryCode.bin", "w")
    outputBinary.write(binaryCode)
    outputBinary.close()