import argparse
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
    files = list(file_path.glob("*.log"))
    error_list = []

    for filename in files:
        with open(filename) as file_read:
            reader = file_read.readlines()
            for page_number, line in enumerate(reader):
                words = line.split()
                if text in words:
                    index = words.index(text)
                    start = words[max(0, index - 5):index]
                    finish = words[index + 1:min(len(words), index + 6)]
                    context = ' '.join(start) + ' ' + text + ' ' + ' '.join(finish)
                    error_list.append(f"The '{context}' founded on line:{page_number+1} in ({filename})")
    return error_list


if __name__ == "__main__":
    errors = get_files_list()
    for error in errors:
        print(error)
