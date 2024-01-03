from models.morse import Morse


def main():
    result = Morse.generate_morse_code_audio('TEST ME')
    print(result)


if __name__ == '__main__':
    main()
