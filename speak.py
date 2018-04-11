import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
speak.Speak("The detected object is toothbrush")
speak.Speak("The detected object is bottle")
speak.Speak("The detected object is scissor")
