# coding:utf-8
import os
import os.path
import zipfile
import urllib
from os.path import basename, splitext
from urlparse import urlsplit
from transcoding import convert


sub_zip_name = '';

def convert_sub(filename):
    convert_utf8(filename)


def unzip_file(zipfilename, unziptodir):
    if not os.path.exists(unziptodir): os.mkdir(unziptodir, 0777)
    zfobj = zipfile.ZipFile(zipfilename)
    for name in zfobj.namelist():
        name = name.replace('\\', '/')
        if name.endswith('/'):
            os.mkdir(os.path.join(unziptodir, name))
        else: 
            ext_filename = os.path.join(unziptodir, name)
            ext_dir= os.path.dirname(ext_filename)
            if not os.path.exists(ext_dir) : os.mkdir(ext_dir,0777)
            outfile = open(ext_filename, 'wb')
            outfile.write(zfobj.read(name))
            outfile.close()
            convert_utf8(ext_filename)


def unrar_file(sub_zip_name):
    pass 

def unzip_file(sub_zip_name):
    zipFile = zipfile.ZipFile(sub_zip_name)
    for filename in zipFile.namelist():
        content = zipFile.read(filename)
        content = convert(content)
        open(filename, 'w').write(content)

def extract_file():
    global sub_zip_name
    extension = splitext(sub_zip_name)


def download_tmp_sub(sub_url):
    global sub_zip_name
    sub_zip_name = basename(urlsplit(sub_url)[2])
    urllib.urlretrieve(sub_url, sub_zip_name)
    

def delete_tmp_sub():
    os.remove(sub_zip_name)


def download_sub(sub_url):
    download_tmp_sub(sub_url)
    unzip_file(sub_zip_name, './')
    delete_tmp_sub()
