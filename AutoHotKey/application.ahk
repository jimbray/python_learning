#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


#c::
{
  IfWinNotExist ahk_class Chrome_WidgetWin_1
  {
    Run "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    WinActivate
  }
  Else IfWinNotActive ahk_class Chrome_WidgetWin_1
  {
    WinActivate
  }
  Else
  {
    WinMinimize
    }
    Return
}
