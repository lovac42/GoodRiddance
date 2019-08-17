; Copyright: (C) 2019 Lovac42
; Support: https://github.com/lovac42/GoodRiddance
; License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html

; Helper used to trigger page activity in order
; to activate autoplay. Mouse pointer must
; be with the Anki reviewer window.



#Persistent
    SetTimer, Autoplay, 250
return

Autoplay:
    IfWinActive, Anki - autoplay ahk_class Qt5QWindowIcon
    {
        MouseClick, left
    }
    return
