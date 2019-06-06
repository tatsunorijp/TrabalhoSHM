import unittest
import Functions

text = "meu gato eh preto"
morse = "-- . ..-  --. .- - ---  . ....  .--. .-. . - ---"
binario = "1110111000100010101110000000111011101000101110001110001110111011100000001000101010100000001011101110100010111010001000111000111011101110"

class Tests(unittest.TestCase):


    def testTextToMorse(self):
        result = Functions.textToMorse(text)
        expected = morse
        self.assertEqual(expected, result)

    def testMorseToText(self):
        result = Functions.morseToText(morse)
        expected = text
        self.assertEqual(expected, result)

    def testMorseToBinario(self):
        result = Functions.morseToBinary(morse)
        expected = binario
        self.assertEqual(expected, result)

    def testBinaryToMorse(self):
        result = Functions.binaryToMorse(binario)
        expected = morse
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
