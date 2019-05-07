#! /usr/bin/env python3

from glob import glob
from pathlib import Path
import os.path
import tika
# import textract

tika.initVM()
from tika import parser



def write_output(output, module, ext, fname):
    mydir = f'output/{module}/'
    Path(mydir).mkdir(parents=True, exist_ok=True)
    path = os.path.basename(fname)
    path = os.path.splitext(path)[0] + f'.{ext}'
    path = os.path.join(mydir, path)
    with open(path, 'w') as f:
        print(output, file=f)


# def demo_textract(files):
#     Path('output/textract/').mkdir(parents=True, exist_ok=True)
#     for finp in files:
#         text = textract.process(finp, encoding='latin2')
#         text = text.decode(encoding='latin2')
#         with open(get_fout(finp, 'textract'), 'w') as f:
#             print(text, file=f)


def demo_tika_html(inp):
    parsed = parser.from_file(inp, xmlContent=True)
    return parsed['content']


def demo_tika_txt(inp):
    parsed = parser.from_file(inp)
    return parsed['content']


def main():
    files = glob('pdf/*.pdf')
    for inp in files:
        txt = demo_tika_txt(inp)
        html = demo_tika_html(inp)
        write_output(txt, 'tika-txt', 'txt', inp)
        write_output(html, 'tika-html', 'html', inp)


if __name__ == '__main__':
    main()
