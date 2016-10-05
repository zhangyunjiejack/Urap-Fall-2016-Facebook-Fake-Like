#include <AutoItConstants.au3>
#include <MsgBoxConstants.au3>

_open()
_choose_task("about")
_restore_before_start()
_save()


Func _save()
;   $finish = PixelSearch(844, 440, 858, 453, 0x97d593, 30)
;   If Not @error Then
;	  MsgBox(0, "t", "t")
;   Else
;	  MsgBox(0, "f", "f")
;   EndIf


   Do
	  Sleep(30000)
	  $finish = PixelSearch(844, 440, 858, 453, 0x97d593, 30)
   Until Not @error
   MouseClick($MOUSE_CLICK_LEFT, 870, 445, 1)
   Sleep(5000)
   MouseClick($MOUSE_CLICK_LEFT, 965, 727, 1)
   Sleep(5000)
   MouseClick($MOUSE_CLICK_LEFT, 976, 694, 1)
   Sleep(5000)
   MouseClick($MOUSE_CLICK_LEFT, 692, 476, 1)
   Sleep(10000)
   MouseClick($MOUSE_CLICK_LEFT, 862, 399, 1)
   Sleep(7000)
   MouseClick($MOUSE_CLICK_LEFT, 1167, 10, 1)
   Sleep(5000)
   MouseClick($MOUSE_CLICK_LEFT, 645, 410, 1)
   Sleep(5000)
EndFunc

Func _restore_before_start() ;To check whether to restore data from last task
;   MsgBox(0, "t", "t")
   sleep(20000)
   Local $request_restore = PixelSearch(595, 362, 612, 375, 0xb9bbc4, 30)
   If Not @error Then
;	  MsgBox(0, "t", "t")
	  MouseClick($MOUSE_CLICK_LEFT, 726, 409, 1)
	  Sleep(3000)
	  MouseClick($MOUSE_CLICK_LEFT, 645, 412, 1)
	  Local $test_fail = PixelSearch(616, 326, 620, 329, 10)
	  If Not @error Then
		 MsgBox(0, "Test Initialization Failed", "Automatic search halts")
		 Break
	  EndIf
   Else
	  MouseMove(400, 500, 10)
   EndIf
   Sleep(1000)
   MouseClick($MOUSE_CLICK_LEFT, 756, 438, 1)
   Sleep(5000)
   ;MsgBox(0, "Task Initialized", "Initialization finished, working. Miao~")
   ;Sleep(3000)
   ;MouseClick($MOUSE_CLICK_LEFT, 758, 441, 1)
EndFunc

Func _choose_task($work) ;Choose one task menu and starts working on it
   ;sleep(18000)
   Do
	  sleep(5000)
	  Local $tasks = PixelSearch(26, 213, 31, 146, 0xd5ae62, 30); check color
   Until Not @error
   ;MsgBox(0, "t", "t")
   sleep(5000)
   MouseClick($MOUSE_CLICK_LEFT, 15, 215, 1) ;Choosing the right task folder
   Sleep(3000)
   IF $work == "friends" Then
	  MouseClick($MOUSE_CLICK_LEFT, 154, 281, 1) ;Clicking on the task
	  Sleep(3000)
	  MouseClick($MOUSE_CLICK_LEFT, 233, 507, 1)
   Else
	  If $work == "friends_html" Then
		 MouseClick($MOUSE_CLICK_LEFT, 154, 306, 1)
		 Sleep(3000)
		 MouseClick($MOUSE_CLICK_LEFT, 235, 525, 1)
	  Else
		 MouseClick($MOUSE_CLICK_LEFT, 154, 238, 1)
		 Sleep(3000)
		 MouseClick($MOUSE_CLICK_LEFT, 243, 466, 1)

	  EndIf
   EndIf
;   MsgBox(0, "Task Menu Shown", "Task to be started.")
EndFunc

Func _open() ;Open bazhuayu.exe from task bar
   MouseClick($MOUSE_CLICK_LEFT, 291, 751, 1) ;Clicking on bazhuayu icon
   Sleep(19000)
   Local $color_login = PixelSearch(625, 381, 633, 383, 0x000000) ; Check color
   If Not @error Then
	  MouseClick($MOUSE_CLICK_LEFT, 698, 494, 1) ;login
   Else
	  Sleep(5000)
	  MouseClick($MOUSE_CLICK_LEFT, 698, 494, 1) ;login
   EndIf
   sleep(18000)
   MouseMove(200, 500, 10)
EndFunc
