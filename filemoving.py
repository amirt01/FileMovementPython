from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from os.path import exists, splitext
from os import mkdir, listdir, rename
from time import sleep
from getpass import getuser

USER = getuser()

TRACK = "/Users/" + USER + "/Downloads"
DOCUMENTS = "/Users/" + USER + "/Downloads/Documents"
MUSIC = "/Users/" + USER + "/Downloads/Music"
PHOTOS = "/Users/" + USER + "/Downloads/Photos"
PROGRAMS = "/Users/" + USER + "/Downloads/Programs"
ZIPS = "/Users/" + USER + "/Downloads/zip"


def setup():
    # photos
    if not exists(PHOTOS):
        mkdir(PHOTOS)
    # documents
    if not exists(DOCUMENTS):
        mkdir(DOCUMENTS)
    # music
    if not exists(MUSIC):
        mkdir(MUSIC)
    # programs
    if not exists(PROGRAMS):
        mkdir(PROGRAMS)
    # zip
    if not exists(ZIPS):
        mkdir(ZIPS)

    move_files()


def download_wait():
    timeout = 30
    seconds = 0
    waiting = True

    while waiting and seconds < timeout:
        sleep(1)
        waiting = False

        for filename in listdir(TRACK):
            if filename.endswith('.crdownload'):
                wait = True
        seconds += 1


def move_files():
    for filename in listdir(TRACK):
        extension = splitext(filename)[-1].lower()
        newDestination = src = TRACK + "/" + filename

        # pictures
        if extension in {'.png', '.jpg', '.jpeg'}:
            newDestination = PHOTOS + "/" + filename
        # documents
        elif extension in {'.doc', '.xls', '.xlsx', '.pdf', 'txt', '.docx', '.csv'}:
            newDestination = DOCUMENTS + "/" + filename
        # music
        elif extension in {'.mp3', '.wav'}:
            newDestination = MUSIC + "/" + filename
        # programs
        elif extension in {".exe", '.msi'}:
            newDestination = PROGRAMS + "/" + filename
        # zips
        elif extension in {".zip"}:
            newDestination = ZIPS + "/" + filename

        rename(src, newDestination)


class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        download_wait()
        move_files()


setup()

eventHandler = MyHandler()
observer = Observer()
observer.schedule(eventHandler, TRACK, recursive=True)
observer.start()

try:
    while True:
        sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
