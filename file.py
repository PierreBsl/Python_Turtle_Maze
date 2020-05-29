import os

class File:
    @staticmethod
    def getFile(file_path):
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                return file.read().splitlines()
        else:
            exit("Fichier introuvable")
