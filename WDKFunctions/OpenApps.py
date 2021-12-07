import os
import wmi

from WDKFunctions import OpenFolder
def terminate(nameF):
    try:
        ti = 0
        name = nameF
        f = wmi.WMI()
        for process in f.Win32_Process():
            if process.name == name:
                process.Terminate()
                ti += 1
        if ti == 0:
            print("Process not found!!!")
    except:
        print('process done')

def listOfprocess():
    # Initializing the wmi constructor
    f = wmi.WMI()

    # Printing the header for the later columns
    print("pid   Process name")

    # Iterating through all the running processes
    for process in f.Win32_Process():
        # Displaying the P_ID and P_Name of the process
        print(f"{process.ProcessId:<10} {process.Name}")



myAppsOpen = {
    'notepad': 'C:\\Windows\\system32\\notepad.exe',
    'whatsapp':'C:\\Users\\wdils\\AppData\\Local\\WhatsApp\\WhatsApp.exe',
    'chrome':'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    'snippingtool':'C:\\Windows\\system32\\SnippingTool.exe',

}

myAppsClose = {
    'notepad': 'notepad.exe',
    'chrome': 'chrome.exe',
    'zoom': 'Zoom.exe',
    'whatsapp': 'WhatsApp.exe',
    'allfolders':'explorer.exe',
    'snippingtool':'SnippingTool.exe',


}
def OpenApp(command):
    try:
        if command == 'whats':
            command = 'whatsapp'
        app = myAppsOpen[command]
        os.startfile(app)
        return 'done'
    except:
        return 'Invalid'

def CloseApp(command):
    try:
        if command == 'whats' or 'whatsapp':
            command = 'whatsapp'
        app = myAppsClose[command]
        terminate(app)
        return 'done'
    except:
        return 'Invalid'




