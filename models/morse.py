# INSTRUCTIONS

# Words are separated by '/' in morse code
# While actual Morse code signal does not include a space after '/', it's often added for clarity in written representations

import re


class Morse:
    """
    A class for encrypting text into Morse code and decrypting it
    """
    # make a collection of all letters and number and corresponding morse code
    morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', ' ': '/'
    }
    # Invert the dictionary
    inverted_morse_code = {
        value: key for key, value in morse_code.items()}

    @classmethod
    def encrypt(cls, text):
        """
        Encrypt the given text into Morse code.

        :param text: The text to be encrypted.
        :return: The encrypted Morse code.
        """
        # morse code is always uppercase
        words = text.upper().split(' ')

        morse_result = ""

        for i, word in enumerate(words):
            # use .get() to replace unknown symbol by a space
            morse_result += " ".join([cls.morse_code.get(char, '')
                                     for char in word])
            if i < len(words) - 1:
                morse_result += " / "

        return morse_result

    @classmethod
    def decrypt(cls, morse):
        """
        Decrypt the given Morse code into text.

        :param morse: The Morse code to be decrypted.
        :return: The decrypted text.
        """
        morse_sequences = [word.strip().split(' ')
                           for word in re.split('/\s*', morse)]

        # create sentence from individual morse sequences (or morse words)
        # catch any unknown morse symbols with '?'
        natural_language = ""
        for morse_word in morse_sequences:
            natural_language += "".join([cls.inverted_morse_code.get(
                morse_symbol, '?') for morse_symbol in morse_word])
            natural_language += ' '

        # remove the last space
        natural_language = natural_language[:-1]

        return natural_language
