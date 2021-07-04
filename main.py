import art, os, requests
from colorama import Fore
import youtube_dl, platform
from googlesearch import search
import subprocess

YOUTUBE = "https://www.youtube.com/"
LIST = "list="
WATCH = "watch"

def welcome_message():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    print(art.text2art("Youtube-Downloader"))
    print(Fore.CYAN + "\nCreated By:" + Fore.RESET + " Vishesh Dvivedi [All About Python]\n")
    print(Fore.YELLOW + "GitHub: " + Fore.RESET + "   visheshdvivedi")
    print(Fore.YELLOW + "Youtube:" + Fore.RESET + "   All About Python")
    print(Fore.YELLOW + "Instagram:" + Fore.RESET + " @itsallaboutpython")
    print(Fore.YELLOW + "Blog Site:" + Fore.RESET + " itsallaboutpython.blogspot.com\n")
    print(Fore.RED + "DISCLAIMER:" + Fore.RESET + " Kindly use the downloaded videos from this tool only for personal use.")
    print('            The developer is not responsible for misuse of this script.\n\n')

def checkInternetConenctivity():
    response = requests.get(YOUTUBE)
    if response.status_code == 200:
        print("[INFO] Internet Connectivity...Found\n")
    else:
        print("[INFO] Internet Connectivity..Not Found")
        exit(0)

def download(url, path, isPlaylist = True):
    curr_path = os.getcwd()
    os.chdir(path)
    if not isPlaylist:
        subprocess.call("youtube-dl --no-playlist {0}".format(url))
    else:
        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    print("[INFO] Video saved at '{0}'".format(os.getcwd()))
    os.chdir(curr_path)  

def download_list(url_list, path):
    curr_path = os.getcwd()
    os.chdir(path)
    ydl_opts = {}
    for video in url_list:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url.strip()])
    print("[INFO] Videos saved at '{0}'".format(os.getcwd()))
    os.chdir(curr_path)

if __name__ == "__main__":
    welcome_message()
    checkInternetConenctivity()
    path = ''
    path = input("Enter path where you want to save video (press enter to save at default 'video' folder): ")
    if path == '':
        path = "video"
    if not os.path.exists(path):
        print('[ERROR] Invalid path {0}...try again'.format(path))
        exit(0)
    url = input('Enter URL (For multiple urls, separate them by commas): ')
    if YOUTUBE in url:
        if LIST in url and WATCH in url:
            choice = input("Do you want to download the whole playlist (y/n): ")
            if "y" in choice.lower():
                print("[INFO] Downloading playlist.")
                download(url, path)
            elif "n" in choice.lower():
                print("[INFO] Downloading video.")
                download(url, path, False)
            else:
                print("[ERROR] Invalid choice {0}".format(choice))
        elif "," in url:
            print("[INFO] Downloading all youtube videos.")
            download_list(url.split(","), path)
        else:
            print("[ERROR] This youtube URL does not seem to point to any video or playlist.")
            print("[ERROR] Please check the URL and try again.")
    else:
        print("[ERROR] Invalid URL format. Kindly enter a youtube video URL")
