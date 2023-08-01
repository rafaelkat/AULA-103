import os
import time
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEvenHandler

origem = "C:/Users/Usuario/Downloads"
destino = "C:/Users/Usuario/OneDrive/Área de Trabalho/codigos/AULA-103"

dir_tree = {
    "image_files": [".jpg", ".jpeg", ".png", ".gif", ".jfif"],
    "video_files": [".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".mp4"],
    "document_files": [".ppt", ".xls", ".xlsx", ".csv", ".pdf", ".txt"],
    "setup_files": [".exe",".bin", ".cmd",".msi",".dmg"]
}

class FileMovimentHandler(FileSystemEvenHandler):
    def on_created(self, event):
        name, extencion = os.path.splitext(event.src_path)
        time.sleep(1)

        for key,value in dir_tree.items():
            time.sleep(1)
            
            if extencion in value:
                fileName = os.path.basename(event.src_path)
                print("Baixado " + fileName)
                
                path1 = origem + "/" + fileName
                path2 = destino + "/" + key
                path3 = destino + "/" + key + "/" + fileName

                if os.path.exists(path2):
                    print("Diretorio existe ")
                    print("Movendo " + fileName + "... ")
                    shutil.move(path1, path3)
                    time.sleep(1)
                else:
                    print("Criando diretorio")    
                    os.makedirs(path2)
                    print("Movendo " + fileName + "... ")
                    shutil.move(path1, path3)
                    time.sleep(1)

event_handler = FileMovimentHandler()

observer = Observer()

observer.schedule(event_handler, origem, recursive = True)
observer.start()

try: 
    while True:
        time.sleep(2)
        print("Execultando ... ")
except KeyboardInterrupt:
    print("Interrompido ")
    observer.stop()









