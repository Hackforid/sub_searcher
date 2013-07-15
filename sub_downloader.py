# coding:utf-8
import os
import os.path
import zipfile
import urllib
from os.path import basename, splitext
from urlparse import urlsplit
from transcoding import convert


sub_zip_name = ''


def unrar_file(sub_zip_name):
    cmd = 'unrar e ' + sub_zip_name;
    os.system(cmd)

def unzip_file(sub_zip_name):
    zipFile = zipfile.ZipFile(sub_zip_name)
    for filename in zipFile.namelist():
        content = zipFile.read(filename)
        content = convert(content)
        open(filename, 'w').write(content)


def extract_file():
    global sub_zip_name
    extension = splitext(sub_zip_name)[1]
    print(extension)

    if extension == '.zip':
        unzip_file(sub_zip_name)
    elif extension == '.rar':
        unrar_file(sub_zip_name)


def download_tmp_sub(sub_url):
    global sub_zip_name
    sub_zip_name = basename(urlsplit(sub_url)[2])
    print("Downloading...")
    urllib.urlretrieve(sub_url, sub_zip_name)


def delete_tmp_sub():
    os.remove(sub_zip_name)


def download_sub(sub_url):
    download_tmp_sub(sub_url)
    extract_file()
    delete_tmp_sub()
