#-*- coding:utf-8 -*-
import chardet
import codecs

def convert(content):
    source_encoding = chardet.detect(content)['encoding']
    content = content.decode(source_encoding)
    return content.encode('utf-8')


def convert_encoding(filename, target_encoding):
    content = codecs.open(filename, 'r').read()
    source_encoding = chardet.detect(content)['encoding']
    content = content.decode(source_encoding)
    
    if (source_encoding != target_encoding):
        filename = filename.decode(source_encoding).encoding(target_encoding)
        codecs.open(filename, 'w', encoding = target_encoding).write(content)


def convert_utf8(filename):
    convert_encoding(filename, 'utf-8')
