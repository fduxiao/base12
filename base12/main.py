import argparse
from .base12 import b12encode, b12decode
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--decode', action="count", default=0)
    parser.add_argument('input', default=None, nargs='?')
    parser.add_argument('-o', '--output', default=None)
    processor = b12encode

    args = parser.parse_args()
    if args.decode:

        def _processor(x):
            x = x.replace(b'\n', b'')
            x = x.replace(b' ', b'')
            x = x.replace(b'\t', b'')
            x = x.replace(b'\r', b'')
            return b12decode(x)
        processor = _processor

    input_file = sys.stdin.buffer
    if args.input is not None:
        input_file = open(args.input, 'rb')

    output_file = sys.stdout.buffer
    if args.output is not None:
        output_file = open(args.output, 'wb')

    data = input_file.read()
    data = processor(data)
    output_file.write(data)


if __name__ == '__main__':
    main()
