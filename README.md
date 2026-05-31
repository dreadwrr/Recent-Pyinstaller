Pyinstaller resources for recentchanges <br>
Will post any updates or findings here regarding pyinstaller and also will look into nuitka instructions <br>
# Recent-Pyinstaller <br>
<br>
if you built a binary from the source code these .bat go with pyintaller <br>
they point to main <br><br>

The size of the app can be reduce with upx placed in the directory before build upx-5.1.1-win64.zip <br>
upx https://github.com/upx/upx <br><br>

also the following can be removed from build <br>
dist\main\_internal\PySide6\opengl32sw.dll <br>
dist\main\_internal\PySide6\Qt6Qmd.dll <br>
dist\main\_internal\PySide6\Qt6Network.dll <br>
dist\main\_internal\PySide6\Qt6OpenGl.dll <br><br>




main.py is not longer needed <br>
/src is no longer needed <br><br>
upx.exe win64 from github can be put in the folder to compress the executable <br><br>

![Alt text](https://i.imgur.com/ty6b3Th.png)
