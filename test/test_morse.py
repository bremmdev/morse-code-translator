from models.morse import Morse, InvalidMorseCodeError
import pytest

# TEST DATA

encrypt_valid_input = [
    ('HELLO WORLD', '.... . .-.. .-.. --- / .-- --- .-. .-.. -..'),
    ('THIS IS A TEST SENTENCE',
     '- .... .. ... / .. ... / .- / - . ... - / ... . -. - . -. -.-. .'),
    ('MORSE', '-- --- .-. ... .')
]

decrypt_valid_input = [
    ('.... . .-.. .-.. --- / .-- --- .-. .-.. -..', 'HELLO WORLD'),
    ('- .... .. ... /  .. ... / .- / - . ... - / ... . -. - . -. -.-. .',
     'THIS IS A TEST SENTENCE'),
    ('-- --- .-. ... .', 'MORSE')
]

decrypt_invalid_input = [
    '-- --- .-. ....... .',
    '-- --- .-. .... . 23',
    '!!- --- .-. .... .', '-- --- .-. ? .'
]

encrypt_invalid_input = [
    ('HELLO WORLD !', '!'),
    ('HELLO, WORLD', ','),
    ('HELLO WORLD!!?', '!!?'),
    ('/HELLO WORLD', '/'),
    ('HELLO @#%()WORLD', '@#%()'),
]


# ENCRYPT TESTS

@pytest.mark.parametrize("text_input, expected_output", encrypt_valid_input)
def test_encrypt_valid_input(text_input, expected_output):
    assert Morse.encrypt(text_input) == expected_output


@pytest.mark.parametrize("invalid_text_input, expected_output", encrypt_invalid_input)
def test_encrypt_invalid_input(invalid_text_input, expected_output):
    with pytest.raises(ValueError, match=f'Invalid characters found: {expected_output}'):
        Morse.encrypt(invalid_text_input)


def test_encrypt_no_input():
    with pytest.raises(ValueError):
        assert Morse.encrypt('')

# DECRYPT TESTS


@pytest.mark.parametrize("morse_input, expected_output", decrypt_valid_input)
def test_decrypt_valid_morse_input(morse_input, expected_output):
    assert Morse.decrypt(morse_input) == expected_output


@pytest.mark.parametrize("invalid_morse_input", decrypt_invalid_input)
def test_decrypt_invalid_input(invalid_morse_input):
    with pytest.raises(InvalidMorseCodeError):
        Morse.decrypt(invalid_morse_input)


def test_decrypt_no_input():
    with pytest.raises(InvalidMorseCodeError):
        assert Morse.decrypt('')
