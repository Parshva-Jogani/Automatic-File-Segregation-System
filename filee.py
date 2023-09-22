import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/parsh/Downloads"
to_dir = "E:/folder for project"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.pv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg'],
    "Folder_Files": ['.zip']
}

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        name,extension = os.path.splitext(event.src_path)
        for key,value in dir_tree.items():
            if extension in value:
                filename=os.path.basename(event.src_path)
                path1=from_dir + "/" + filename
                path2 = to_dir +"/" + key
                path3 = to_dir +"/" + key + "/" + filename
                time.sleep(2)
                if os.path.exists(path2):
                    print("moving file")
                    shutil.move(path1,path3)

                else:
                    print("creating folder")
                    os.makedirs(path2)
                    print("moving file")
                    shutil.move(path1,path3)

event_handler = FileMovementHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()

while True:
    time.sleep(2)
    print("running...")