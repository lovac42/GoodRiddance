# -*- coding: utf-8 -*-
# Copyright: (C) 2019 Lovac42
# Support: https://github.com/lovac42/GoodRiddance
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
# Version: 0.0.2


import re
from anki.hooks import addHook
from aqt import mw


# Supported formats
TYPE={
    'webm': "video/webm",
    'ogv': "video/ogg",
    'ogg': "audio/ogg",
}

def inline_media(html, *args, **kwargs):
    def subVideoTag(sound):
        type=TYPE.get(sound.group(2))
        return u"""
<video class="autoplay" playsinline controls>
<source src="%s" type="%s">
</video>
"""%(sound.group(1),type)
    html=re.sub(r"\[sound:(.*?\.(webm|ogv|ogg))\]", subVideoTag, html)
    return html + """
<script>
window.setTimeout(function(){
    document.querySelector('.autoplay').play();
},500);
</script>"""

addHook("mungeQA", inline_media)



# Use autohotkey to simulate a physical click
# on showQ in order to trigger autoplay.
# Use title addon to signal AHK
# Mouse pointer must be within the reviewer window.

def onShowQ():
    title=mw.windowTitle()
    mw.setWindowTitle("Anki - autoplay")
    mw.progress.timer(300,
                lambda: mw.setWindowTitle(title),
                False, requiresCollection=False)

addHook("showQuestion", onShowQ)
