#! /usr/bin/env python3

from glob import glob
from pathlib import Path
import os.path
import tika


# TODO:
# def demo_pypdf4(files):
#     pass


# TODO:
# def demo_textract(files):
#     pass


def demo_tika(files):
    Path('txt/tika/').mkdir(parents=True, exist_ok=True)
    tika.initVM()
    from tika import parser
    for finp in files:
        fout = os.path.basename(finp)
        fout = os.path.splitext(fout)[0] + '.txt'
        fout = os.path.join('txt', 'tika', fout)
        parsed = parser.from_file(finp)
        with open(fout, 'w') as f:
            print(parsed["content"], file=f)


def main():
    files = glob('pdf/*.pdf')
    demo_tika(files)


if __name__ == '__main__':
    main()
