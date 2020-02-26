# Youtube-to-Google-Play-Music

![Icon](https://raw.githubusercontent.com/Brightwater/Youtube-to-Google-Play-Music/master/YouTube_to_GPM%20Chrome%20Extension/YouTube%20to%20GPM/icon.png)

This was a personal project and is not meant to download any Youtube videos or songs that you do not own. Use at your own risk!

This tool enables you to upload a video (audio only) from youtube to your google play library. This lets you upload your own songs to listen to that you have available on Youtube but not google play. This project was made to be used with Windows but can be adapted on your own.

To upload a song you simple click the upload button from the Chrome extension, and the program will do the rest!

This project requires a little bit of configuration and some other dependencies not included in the project! Use at your own risk. It is also designed to be used with the pyinstaller package if you plan on using all the components together seemlessly.

For the Chrome Extension:
  Simply download the folder and enable developer mode in chrome. Then just upload the extension.
  
For the server:
  - For the tool to always work, the server must be running in the background on your computer. To accomplish this I reccommend using the     pyinstaller tool https://www.pyinstaller.org/.
  - Once pyinstaller is installed in the python console run the command $ pyinstaller --noconsole --onefile "Youtube to GPM Server.py"
    This will allow the server to run in the background without having the console open at all times.
  - To have the server run on startup you can place it in the startup folder of windows (C:\ProgramData\Microsoft\Windows\Start         Menu\Programs\Startup).
  
For the engine (Youtube to GPM.py):
  - This file requires the most configuration and has some helpful notes in the python file
  - For the program to actually upload the file you will need to download the Google Chrome webdriver to be used with Selenium. https://chromedriver.chromium.org/downloads Once downloaded make sure it is either in your windows path or in the same directory as the main python files.
  - You will then need to run the program once so you can configure a new Chrome Profile for the webdriver to use (If you configure it to   use your existing chrome profile it will not work while you have your normal Google Chrome open.
  - Next you will need to find the chromedriver user profile located in C:/users/your name/AppData/Local/Google/Chrome/User Data/(profile) It should be in a separate folder than your normal Chrome. Place this path in the python file where it says to.
  - While the webdriver is running and your profile is logged in to chrome you will need to visit the google play site and login with     your account. You will then also need to download the Google Play Music extension for chrome to be able to upload songs.
  - You will also need to download the youtube-dl.exe for windows. https://ytdl-org.github.io/youtube-dl/download.html along with ffmpeg. https://www.ffmpeg.org/
  - Once downloaded make sure they are either in your windows path or in the same directory as the main python files.
  - You will probably also want to use pyinstaller for the main file. To do this put this command in the python console $ pyinstaller --onefile "Youtube to GPM.py"
  - Once everything is configured double check the pyinstaller .exes are together along with the chromedriver, ffmpeg, and youtube-dl in the same directory. Then it should be fully configured and ready to use!
