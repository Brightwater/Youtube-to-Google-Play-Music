# Made by Jeremiah Spears
# Youtube to GPM
# v1.3
#
# Dependencies:
#	Chrome Developer extension (Youtube to GPM)
#	Youtube to GPM server

import time
import pathlib
import glob
import os
import sys
import youtube_dl
import subprocess
from gmusicapi import Musicmanager

# open config file
config = open("yt2gpmCONFIG.txt", "r")
x = 0
firstRun = None
ytDlString = ""
removeFile = True

# read config file
for line in config:
	if x is 0:
		firstRun = line.rsplit(':', 1)[1]
	if x is 1:
		ytDlString = line.rsplit(':', 1)[1:]
		ytDlString = ''.join(ytDlString)
		ytDlString = ytDlString.rstrip()
	if x is 2:
		removeFile = line.rsplit(':', 1)[1]
	x += 1

config.close()

# read file that holds link from chrome extension
file = open("link.txt", "r")
videoLink = ""
for line in file:
	videoLink = line

# get download path
downloadPath = pathlib.Path().absolute()

print("Downloading and converting video to mp3 file...")

# start youtube-dl as subprocess
subprocess.call("youtube-dl " + ytDlString + " " + videoLink)
# If running directly in windows shell change to this
# subprocess.call('.\youtube-dl -f bestaudio --no-playlist --audio-format mp3 -x "' + videoLink + '"')

print("\nFile downloaded.")

# find the mp3 file that was downloaded
files = glob.glob(f'{downloadPath}\*.mp3')
latestFile = max(files, key=os.path.getctime)

# connect to gmusicapi
mm = Musicmanager()
# check if firstRun
if "True" in firstRun:
	print("Since this is your first time using the app you will need to allow your google account to authenticate...")
	print("If you would like to change the app settings please modify the config file.")
	mm.perform_oauth()
	config = open("yt2gpmCONFIG.txt", "w")
	firstRun = False
	config.write(f"firstRun:{firstRun}\nYoutube-DL Args:{ytDlString}\nremoveDownloadedFile (saves storage space):{removeFile}")
	config.close()

print("Attempting to login to GPM.")
mm.login()
print(f"Successfuly logged into GPM, Uploading file: {latestFile}...")

c = mm.upload(latestFile)
mm.logout()

print("File upload complete! Finishing up.")

# remove mp3 file from directory (default)
# if you want to keep the file change config (removeFile to true)
if "True" in removeFile:
	os.remove(latestFile)
	print("Removed downloaded file. Goodbye.")
else:
	print("Goodbye.")
time.sleep(1)
