# coding:utf-8
from pyquery import PyQuery as pq
import urllib2
import re
class Shooter():
    """
    Download subtitle from shooter.cn by name
    """
    shooter_base_url = "http://www.shooter.cn" 

    def file_hash(self, a):
   
        def b(j):
            g = ""
            for f in xrange(len(j)):
                h = ord(j[f])
                g += chr(ord(' ') + (h + 47) % 126) if h + 47 >= 126 else chr(h + 47)
            return g
    
        def d(g):
            return g[::-1]
   
        def c(j, h, g, f):
            return j[len(j) - f + g - h: len(j) - f + g ] + j[len(j) - f:len(j) - f+ g - h] + j[len(j) - f + g:] + j[:len(j) - f]
  
        if len(a) > 32:
            t = a[0]
            if t == "o":
                return b((c(a[1:], 8, 17, 27)))
            elif t == 'n':
                return b(d(c(a[1:], 6, 15, 17)))
            elif t == 'm':
                return d(c(a[1:], 6, 11, 17))
            elif t == "l":
                return d(b(c(a[1:], 6, 12, 17)))
            elif t ==  "k":
                return c(a[1:], 14, 17, 24)
            elif t ==  "j":
                return c(b(d(a[1:])), 11, 17, 27)
            elif t ==  "i":
                return c(d(b(a[1:])), 5, 7, 24)
            elif t == "h":
                return c(b(a[1:]), 12, 22, 30)
            elif t == "g":
                return c(d(a[1:]), 11, 15, 21)
            elif t == "f":
                return c(a[1:], 14, 17, 24)
            elif t== "e":
                return c(a[1:], 4, 7, 22)
            elif t == "d":
                return d(b(a[1:]))
            elif t == "c":
                return b(d(a[1:]))
            elif t == "b":
                return d(a[1:])
            elif t == "a":
                return b(a[1:])
        else:
            return a 


    def get_hash(self):
        url = 'http://www.shooter.cn/a/loadmain.js'
        resp = urllib2.urlopen(url).read()
        h = re.findall('shtg_filehash="([a-z0-9]*?)"', resp)
        res = re.findall('shtg_filehash\+="([a-z0-9]*?)"', resp)
        return ''.join(h) + ''.join(res)


    def get_field(self, url):
        resp = urllib2.urlopen(url).read()
        res = re.findall('return local_downfile\(this,([0-9]+?)\)', resp)
        return res[0]
    
    def get_download_url(self, url):
        field = self.get_field(url)
        hash_value = self.get_hash()
        url = 'http://www.shooter.cn/files/file3.php?hash=%s&fileid=%s' % (hash_value, field)
        resp = urllib2.urlopen(url).read()
        return 'http://file1.shooter.cn' + self.file_hash(resp)


    def check_item(self, result_item):
        sub_attr = result_item.find('#sublist_ul li') 
        sub_lanuage = sub_attr\
        .filter(lambda i: pq(this).html().find(u'语言') != -1)
        if sub_lanuage.find(u"简") != -1:
            sub_page_url = self.shooter_base_url\
            + result_item.find('a.introtitle').attr('href')
            return sub_page_url
        else:
            return None

    def get_result(self, movie_name):
        search_url = self.shooter_base_url + "/search/" + movie_name
        result_html = pq(url = search_url)
        return result_html('div.subitem')

    def get_sub_url(self, movie_name):
        sub_items = self.get_result(movie_name)
        item = sub_items.eq(0)
        sub_page_url = self.check_item(item)
        if sub_page_url != None:
            return self.get_download_url(sub_page_url)
        else:
            return None


#main
if __name__ == "__main__":
    shooter = Shooter()
    print shooter.get_sub_url('死人的复仇')
