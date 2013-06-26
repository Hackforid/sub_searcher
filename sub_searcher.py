# coding:utf-8
import sys
from shooter import Shooter
import sub_downloader
movie_name = ""
def main():
    if len(sys.argv) == 2:
        movie_name = sys.argv[1]
        sub_searcher = Shooter()
        sub_url = sub_searcher.get_sub_url(movie_name)
        sub_downloader.download_sub(sub_url)
        
if __name__ == "__main__":
    main()
