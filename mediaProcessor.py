import json
import os
import sys
from ftplib import FTP
import mysql.connector


tag = 1

output = open("output.txt", "w")


def main(configFile):
    # {
    # composer: 'Anton Bruckner',
    # targetComposerFolderName: "bruckner",
    # workTitle: "Symphony No. 6 in Allegro major,
    # genre: "Symphony",
    # workingFolder: ""
    # }
    inputJsonFile = json.loads(configFile)

    # ftp = FTP('classicalmusic-notes.com')
    # ftp.login()
    # ftp.cwd('public_html/wp-content/md/' + inputJsonFile['targetComposerFolderName'])
    print(inputJsonFile)
    if not inputJsonFile["workingFolder"] == "":
        os.chdir(inputJsonFile["workingFolder"])
    path = os.getcwd()
    print("Path: " + path)
    print(os.listdir())
    for subfolder in os.listdir():  # read all movement folders (subfolders)
        readFolder(path+"\\" + subfolder, subfolder)
    output.close()


def readFolder(fullpath, subfolder):
    fileList = os.listdir(fullpath)
    if not fileList[0].endswith(".png"):  # is audio file
        output.write("[MyClip xfile=\"" + fileList[0] + "\" xfield=\"" + subfolder + "\"]\n")
    for mediaFile in range(1, len(fileList)):  # read all files under movement folders (subfolders)
        if not fileList[mediaFile].endswith(".png"):
            global tag
            output.write("[audio4 tag=\"" + str(tag) + "\" src=\"" + fileList[mediaFile] + "\"]\n")
            tag += 1


file = open(sys.argv[1], "r")
main(file.read())
# make own modules/imports
# mySQL import