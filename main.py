from models.morse import Morse
import argparse
import sys
import os


def validate_output_file(file_name):
    try:
        output_file_name, output_format = file_name.split(
            '.')
    except ValueError:
        print(f"Invalid output file: {file_name}")
        sys.exit(1)

    output_file = f"{output_file_name}.{output_format}"

    # check if format is valid
    if output_format not in ['wav', 'mp3']:
        print(f"Invalid output format: {output_format}")
        sys.exit(1)

    # check if export location is valid
    if not os.path.exists(os.path.dirname(output_file)):
        print(f"Invalid output location: {output_file}")
        sys.exit(1)

    return output_file_name, output_format


def main():
    parser = argparse.ArgumentParser(description='Morse Code Translator')
    parser.add_argument('input', help='Input to be processed')
    parser.add_argument('mode', choices=[
                        'encrypt', 'decrypt', 'generate_audio'], help='Mode of operation')
    parser.add_argument(
        '--output', '-o', help='Output file or location, format must be .wav or .mp3')

    args = parser.parse_args()

    if args.mode == 'encrypt':
        result = Morse.encrypt(args.input)
        print(f"Morse code is: {result}")

    elif args.mode == 'decrypt':
        result = Morse.decrypt(args.input)
        print(f"Text is: {result}")

    elif args.mode == 'generate_audio':
        result = Morse.generate_morse_code_audio(args.input)

        # default output file name and format
        if not args.output:
            output_file_name, output_format = 'output', 'wav'
        else:
            output_file_name, output_format = validate_output_file(args.output)

        output_file = f"{output_file_name}.{output_format}"
        result.export(output_file, format=output_format)
        print(f"Audio file generated: {output_file}")


if __name__ == '__main__':
    main()
