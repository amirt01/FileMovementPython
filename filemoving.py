from watchdog.observer import observer
from watchdog.events import FileSystemEventHandler
#need to install these packages pip install watchdog

import json 
import os
import time

class MyHandler(FileSystemEventHandler):
	def on_modified(self, event):
		for filename in os.listdir(folder_to_track):
			src = folder_to_track + "/" filename
			newDestination = folderDestination + "/" filename
			os.rename(src, newDestination)
folder_to_track = "/fileFolder initial destination"
folderDestination = "/fileFolder where the file is going"
eventHandler = MyHandler()
observer = Observer()
observer.schedule(evenHandler, folder_to_track, recursive=True)
observer.start()
try: 
	while True:
		time.sleep(10)
except KeyBoardInerrupt:
	observer.stop()
observer.join()