# GoodRiddance: Inline Media (WEBM, OGV, OGG)


## About:
Converts any WEBM, OGV, or OGG file in a `[sound:...]` tag into an inline `<video>` element.

Note: MP4 is not supported.


# Codec Test:
In order to ensure that your system supports the webm codec, please use this shared deck for testing. It will make sure that we are on the same page and isolate any problems before filing a bug report.  
https://www.dropbox.com/s/siuyw8lr0962j7s/embedded_video.apkg?dl=0


## Screenshot:

<img src="https://github.com/lovac42/GoodRiddance/blob/master/screenshots/embedded_video.png?raw=true" />  


## MPlayer:
If mplayer pops up, remember to disable autoplay. This addon patches Anki after autoplay is triggered.


## Autoplay:
Chromium does not allow embeded videos to autoplay. So in order to activate it, I used an AHK script to trigger a mouse click on the reviewer. The mouse must be inside the reviewer window. It is very hacky.  
https://github.com/lovac42/GoodRiddance/blob/master/helpers/anki_autoplay.ahk

