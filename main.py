import youtube_dl
import art
import sys, os
from googlesearch import search

path = ""
value = ""
NAME = "NAME"
URL = "URL"
download_type = ''


def welcome_message():
    print(art.text2art("Youtube Downloader"))
    print("\n")


def usage():
    print("Usage: python youtube_download.py [OPTION] [VALUE]")
    print()
    print("Options:")
    print(" -n | --name   : To download video by searching name")
    print(" -u | --url    : To download video based on video URL")
    print()
    print("Example: python youtube_download.py -n")
    print("         python youtube_download.py -u")


def download_song(download_type):
    folder = input("Enter file download location: ")
    if download_type == NAME:
        name = input("Enter song name: ")
        query = name + " song youtube"
        url = ''
        for j in search(query, tld="co.in", num=10, stop=1, pause=2):
            url = j
        flag = 0
        os.chdir(folder)
        ydl_opts = {}
        print("Downloading song...please wait")
        with youtube_dl.YoutubeDL(ydl_opts) as ydl :
            flag = 1
            ydl.download([url])
    elif download_type == URL:
        url = input("Enter video url: ")
        os.chdir(folder)
        ydl_opts = {}
        print("Downloading song...please wait")
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            flag = 1
            ydl.download([url])


def main():
    global download_type
    global NAME
    # Checking command line parameters
    if not sys.argv[1]:
        usage()

    if sys.argv[1] == '-n' or sys.argv[1] == '--name':
        download_type = NAME
    elif sys.argv[1] == '-u' or sys.argv[1] == '--url':
        download_type = URL

    download_song(download_type)


if __name__ == '__main__':
    main()