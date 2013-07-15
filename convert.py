#-*- coding:utf-8 -*-
import chardet
import codecs
import sys


def convert_encoding(content, encoding):
    source_encoding = chardet.detect(content)['encoding']
    content = content.decode(source_encoding)
    return content.encode(encoding)


def convert_file(filename, target_encoding):
    content = codecs.open(filename, 'r').read()
    content = convert_encoding(content, target_encoding)
    filename = convert_encoding(filename, target_encoding)
    open(filename, 'w').write(content)


def convert_file_to_utf8(filename):
    convert_file(filename, 'utf-8')


def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        convert_file_to_utf8(filename)


if __name__ == '__main__':
    main()
