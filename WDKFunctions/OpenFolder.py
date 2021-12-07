import os
myFolders = {

        #type names without spaces

        'pythonprojects':'C:\\Users\\wdils\\Documents\\Python Projects',
        'pythonproject':'C:\\Users\\wdils\\Documents\\Python Projects',
        'firstsemester' : 'C:\\Users\\wdils\\Documents\\1st Sem',
        'first-semester' : 'C:\\Users\\wdils\\Documents\\1st Sem',
        'electronic': 'C:\\Users\\wdils\\Documents\\1st Sem\\Electronic',
        'electronics': 'C:\\Users\\wdils\\Documents\\1st Sem\\Electronic',
        'network':'C:\\Users\\wdils\\Documents\\1st Sem\\Fundamental of Computer Networks',
        'networks':'C:\\Users\\wdils\\Documents\\1st Sem\\Fundamental of Computer Networks',
        'mathematics':'C:\\Users\\wdils\\Documents\\1st Sem\\Mathematics',
        'mathematic':'C:\\Users\\wdils\\Documents\\1st Sem\\Mathematics',
        'webprogramming': 'C:\\Users\\wdils\\Documents\\1st Sem\\Web Programming',
        'structuredprogramming': 'C:\\Users\\wdils\\Documents\\1st Sem\\Structured Programing',
        'law': 'C:\\Users\\wdils\\Documents\\1st Sem\\Law',
        'computerscience':'C:\\Users\\wdils\\Documents\\1st Sem\\Computer Science',
        'ethics':'C:\\Users\\wdils\\Documents\\1st Sem\\Ethics',
        'english':'C:\\Users\\wdils\\Documents\\1st Sem\\English',

}



# def BIT_open():
#     os.startfile("C:\\Users\\wdils\\Documents\\BIT")
#
# def PythonProject():
#     os.startfile("C:\\Users\\wdils\\Documents\\Python Projects")
#
# #Fisrt Sem Folders
# def FirstSem():
#     os.startfile("C:\\Users\\wdils\\Documents\\1st Sem")
#
# def Electronics():
#     os.startfile("C:\\Users\\wdils\\Documents\\1st Sem\\Electronic")
#
# def Networks():
#     os.startfile("C:\\Users\\wdils\\Documents\\1st Sem\\Fundamental of Computer Networks")
#
# def Mathematics():
#     os.startfile("C:\\Users\\wdils\\Documents\\1st Sem\\Mathematics")
#
# def WebProgramming():
#     os.startfile("C:\\Users\\wdils\\Documents\\1st Sem\\Web Programming")
#
# def StrucProgramming():
#     os.startfile("C:\\Users\\wdils\\Documents\\1st Sem\\Structured Programing")
#
# def Law():
#     os.startfile("C:\\Users\\wdils\\Documents\\1st Sem\\Law")
#
# def ComputerScience():
#     os.startfile("C:\\Users\\wdils\\Documents\\1st Sem\\Computer Science")
#
# def Ethics():
#     os.startfile("C:\\Users\\wdils\\Documents\\1st Sem\\Ethics")
#
# def English():
#     os.startfile("C:\\Users\\wdils\\Documents\\1st Sem\\English")


#OpenFolder Function
# def OpenFolder(command):
#     switcher = {
#         'pythonprojects': PythonProject,
#         'first semester' : FirstSem,
#         'electronic': Electronics,
#         'network':Networks,
#         'mathematics':Mathematics,
#         'webprogramming': WebProgramming,
#         'structuredprogramming': StrucProgramming,
#         'law': Law,
#         'computerscience':ComputerScience,
#         'ethics':Ethics,
#         'english':English,
#
#     }
#     func=switcher.get(command, lambda : 'Invalid')
#     return func()

#OpenFolder Function
def OpenFolder(command):
    try:
        folder = myFolders[command]
        os.startfile(folder)
        return 'done'
    except:
        return 'Invalid'



