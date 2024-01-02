
from models.morse import Morse

def main():
    # print(Morse.decrypt('.... . .-.. .-.. --- / - --- / -.-- --- ..- / .-- --- .-. .-.. -..'))
    print(Morse.encrypt('HELLO TO YOU, WORLD'))

if __name__ == '__main__':
    main()
