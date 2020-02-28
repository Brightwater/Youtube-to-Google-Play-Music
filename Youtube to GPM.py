# Made by Jeremiah Spears
# Youtube to GPM
# v1.1
#
# Dependencies:
#	Chrome Developer extension (Youtube to GPM)
#	Youtube to GPM server

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyautogui
import time
import pathlib
import glob
import os
import sys
import youtube_dl
import subprocess

# read file that holds link from chrome extension
file = open("link.txt", "r")
videoLink = ""
for line in file:
	videoLink = line

# get download path
downloadPath = pathlib.Path().absolute()

print("Converting video to mp3 file...")

# start youtube-dl as subprocess
subprocess.call("youtube-dl -f bestaudio --no-playlist --audio-format mp3 -x " + videoLink)

# If running directly in windows shell change to this
# subprocess.call('.\youtube-dl -f bestaudio --no-playlist --audio-format mp3 -x "' + videoLink + '"')

print("\nFile downloaded.")

print("Starting Chrome with Selenium")

# chromedriver configuration
chrome_options = Options()
chrome_options.add_argument("--window-size=1920x1080")

# you will need to find the user profile for your chromedriver and put it here
# (this is my path)
chrome_options.add_argument('user-data-dir=C:\\Users\Jeremiah\AppData\Local\Google\Chrome\\User Data\Profile 2')

# start chrome driver
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.minimize_window()

print("Loading Google Play Music...")

# open google play music
# this will require the browser to open and close the window just allow it
# or it won't work
done = False
while not done:
	try:
		driver.maximize_window()
		driver.get('https://play.google.com/music/listen#/home')
		driver.find_element_by_xpath('/html/body/paper-drawer-panel/iron-selector/div[1]/paper-header-panel/paper-toolbar/div[1]/div/div[2]/paper-icon-button').click()
		driver.find_element_by_xpath('/html/body/paper-drawer-panel/iron-selector/div[2]/paper-header-panel/div/div[1]/div/div[3]/a[1]').click()
		done = True
		driver.minimize_window()
	except:
		time.sleep(2)

# find the mp3 file that was downloaded
files = glob.glob(f'{downloadPath}\*.mp3')
latestFile = max(files, key=os.path.getctime)

print(f"\nUploading file: {latestFile}...")

# send file to google play music fileInput
fileInput = driver.find_element_by_xpath('/html/body/div[10]/div[2]/div/div[6]/div[2]/input')
fileInput.send_keys(latestFile)

# check if file is uploaded
try:
	time.sleep(1)

	driver.find_element_by_xpath('/html/body/div[10]/div[2]/div/div[7]/div[1]/paper-button').click

	time.sleep(1)
	print("File uploading to Google Play Music.")

	time.sleep(2)
	driver.find_element_by_xpath('/html/body/paper-drawer-panel/iron-selector/div[2]/paper-header-panel/paper-toolbar/div[1]/paper-icon-button/iron-icon').click()
except:
	print()

found = False

while True:
	status = ""
	try:
		driver.find_element_by_xpath('/html/body/paper-drawer-panel/iron-selector/div[1]/div[1]/button').click()
		status = driver.find_element_by_xpath('/html/body/paper-drawer-panel/iron-selector/div[1]/div[1]/button/paper-tooltip/div').text
		found = True
	except:
		if found is not True:
			time.sleep(3)
		else:
			break

print("File upload complete! Finishing up.")

# remove mp3 file from directory
# if you want to keep the file remove this line

driver.minimize_window()
time.sleep(10)
print("Goodbye.")
driver.quit()
os.remove(latestFile)
time.sleep(1)
