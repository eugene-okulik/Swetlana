import argparse
import re
from pathlib import Path


def parameters():
    parser = argparse.ArgumentParser(description='Find the error in your logs')
    parser.add_argument('file_path', type=Path, help='Enter your files path')
    parser.add_argument('text', type=str, help='Enter the text which the script should find')
    args = parser.parse_args()

    file_path = args.file_path
    text = args.text
    return file_path, text


def get_files_list():
    file_path, text = parameters()
    files = list(file_path.glob('*.log'))
    error_list = []
    pattern = re.compile(r'(\w+\W+){0,3}' + re.escape(text) + r'(\W+\w+){0,3}')

    for filename in files:
        with open(filename) as file_read:
            reader = file_read.read().split('\n')
            for i, line in enumerate(reader):
                if text in line:
                    match = pattern.search(line)
                    substr = match.group(0)
                    error_list.append(f'The "{substr}" founded on line:{i+1} in ({filename})')
    return error_list


if __name__ == "__main__":
    errors = get_files_list()
    for error in errors:
        print(error)
