#! /usr/bin/env python3

from glob import glob
from pathlib import Path
import os.path
import tika
import textract


def get_fout(fname, module):
    """return the name of output file
    """
    res = os.path.basename(fname)
    res = os.path.splitext(res)[0] + '.txt'
    res = os.path.join('txt', module, res)
    return res



# TODO:
# def demo_pypdf4(files):
#     pass


def demo_textract(files):
    Path('txt/textract/').mkdir(parents=True, exist_ok=True)
    for finp in files:
        text = textract.process(finp, encoding='latin2')
        text = text.decode(encoding='latin2')
        with open(get_fout(finp, 'textract'), 'w') as f:
            print(text, file=f)


def demo_tika(files):
    Path('txt/tika/').mkdir(parents=True, exist_ok=True)
    tika.initVM()
    from tika import parser
    for finp in files:
        parsed = parser.from_file(finp)
        with open(get_fout(finp, 'tika'), 'w') as f:
            print(parsed["content"], file=f)


def main():
    files = glob('pdf/*.pdf')
    demo_tika(files)
    demo_textract(files)


if __name__ == '__main__':
    main()
