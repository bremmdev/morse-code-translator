# Morse Code Encryptor/Decryptor with Audio Generation

This Python module provides a simple Morse code encryption and decryption functionality, along with the capability to generate Morse code audio from given text. Additionally, it includes a command-line interface (CLI) for easy interaction.

## Features
- Morse Code Encryption: Convert text to Morse code
- Morse Code Decryption: Convert Morse code back to readable text
- Morse Code Audio Generation: Generate audio from Morse code
- CLI Interface: Perform operations through the command line 

## Usage

### Example Usage
```
from morse_code import Morse

# Encrypt text to Morse code
encrypted_text = Morse.encrypt("Hello World")
print(encrypted_text)

# Decrypt Morse code to text
decrypted_text = Morse.decrypt(".... . .-.. .-.. --- / .-- --- .-. .-.. -..")
print(decrypted_text)

# Generate Morse code audio
audio = Morse.generate_morse_code_audio("Hello World")
```

### CLI Usage

`python main.py <input> <mode> [--output OUTPUT]`

With the following options:
- `<input>`:  Input to be processed.
- `<mode>`:  Mode of operation. Choose from 'encrypt', 'decrypt', or 'generate_audio'.
- `--output, -o`:  Output file or location. Format must be .wav or .mp3.
