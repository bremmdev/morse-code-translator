# INSTRUCTIONS

# Words are separated by '/' in morse code
# While actual Morse code signal does not include a space after '/', it's often added for clarity in written representations

import re
from pydub import AudioSegment
from pydub.generators import Sine

class InvalidMorseCodeError(Exception):
    def __init__(self, message):
        super().__init__(message)

class Morse:
    """
    A class for encrypting text into Morse code and decrypting it
    """

    DOT_DURATION = 100  # Duration for a dot in milliseconds
    DASH_DURATION = 300  # Duration for a dash in milliseconds
    SPACE_BETWEEN_LETTERS_DURATION = 100  # Duration between letters in the same word in milliseconds
    SPACE_BETWEEN_WORDS_DURATION = 700  # Duration between different words in milliseconds
    
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

        if text == '':
            raise ValueError('Input is empty')

        invalid_chars = re.sub('[A-Z0-9 \-\.]', '', text.upper())
        if invalid_chars:
            raise ValueError(f'Invalid characters found: {invalid_chars}')

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

        if '?' in natural_language:
            raise InvalidMorseCodeError('Invalid Morse code')

        # remove the last space
        natural_language = natural_language[:-1]

        return natural_language

    @classmethod
    def generate_morse_code_audio(cls, text):
        """
        Generate Morse code audio from the given text.

        :param text: The text to be converted to Morse code audio.
        :return: The Morse code audio.
        """
        # a dot lasts for one unit
        # a dash last for three units
        # the space between dots and dashes that are part of the same letter is one unit
        # the space between different letters is three units
        # the space between different words is seven units

        morse_code = cls.encrypt(text).replace(' / ', '/')
        print(morse_code)

        # create morse code audio
        morse_audio = AudioSegment.empty()    

        # iterate over all characters in the text
        for i, char in enumerate(morse_code):
            if char == '.' or char == '-':
                # if it's a dot or a dash, add the morse code beep
                morse_audio += cls.generate_morse_code_beep(char)
                if i < len(morse_code) - 1 and morse_code[i + 1] != ' ' and morse_code[i + 1] != '/':
                    # if the next character is not a space, add a 1 unit space
                    morse_audio += AudioSegment.silent(duration=cls.SPACE_BETWEEN_LETTERS_DURATION)
            # space between letters in the same word is 1 unit
            elif char == ' ' or char == '/':
                duration = cls.DASH_DURATION if char == ' ' else cls.SPACE_BETWEEN_WORDS_DURATION
                morse_audio += AudioSegment.silent(duration=duration)

        # add 100 ms of silence at the end
        morse_audio += AudioSegment.silent(duration=cls.DOT_DURATION)
        morse_audio.export("morse_code.wav", format="wav")
        return morse_audio

    @classmethod
    def generate_morse_code_beep(cls, char):
        """
        Generate a beep for the given Morse code character.

        :param char: The Morse code character ('.' for dot, '-' for dash).
        :return: The audio segment representing the Morse code beep.
        """
        duration = cls.DOT_DURATION if char == '.' else cls.DASH_DURATION
        return Sine(1000).to_audio_segment(duration=duration)
