# -*- coding: utf-8 -*-
# Copyright: (C) 2019 Lovac42
# Support: https://github.com/lovac42/GoodRiddance
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
# Version: 0.0.1; Prototype


import re
from anki.hooks import addHook


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
},1000);
window.setTimeout(function(){
    document.querySelector('.autoplay').play();
},3000);
</script>"""

# Use autohotkey to simulate a physical click
# on showQ in order to trigger autoplay.
# Use title addon to signal AHK

addHook("mungeQA", inline_media)
