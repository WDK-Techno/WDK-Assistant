import os
import csv
# myFolders = {
#         #type names without spaces
#
#         'pythonprojects':'C:\\Users\\wdils\\Documents\\Python Projects',
#         'pythonproject':'C:\\Users\\wdils\\Documents\\Python Projects',
#         'firstsemester' : 'C:\\Users\\wdils\\Documents\\1st Sem',
#         'first-semester' : 'C:\\Users\\wdils\\Documents\\1st Sem',
#         'electronic': 'C:\\Users\\wdils\\Documents\\1st Sem\\Electronic',
#         'electronics': 'C:\\Users\\wdils\\Documents\\1st Sem\\Electronic',
#         'network':'C:\\Users\\wdils\\Documents\\1st Sem\\Fundamental of Computer Networks',
#         'networks':'C:\\Users\\wdils\\Documents\\1st Sem\\Fundamental of Computer Networks',
#         'mathematics':'C:\\Users\\wdils\\Documents\\1st Sem\\Mathematics',
#         'mathematic':'C:\\Users\\wdils\\Documents\\1st Sem\\Mathematics',
#         'webprogramming': 'C:\\Users\\wdils\\Documents\\1st Sem\\Web Programming',
#         'structuredprogramming': 'C:\\Users\\wdils\\Documents\\1st Sem\\Structured Programing',
#         'law': 'C:\\Users\\wdils\\Documents\\1st Sem\\Law',
#         'computerscience':'C:\\Users\\wdils\\Documents\\1st Sem\\Computer Science',
#         'ethics':'C:\\Users\\wdils\\Documents\\1st Sem\\Ethics',
#         'english':'C:\\Users\\wdils\\Documents\\1st Sem\\English',
#
# }
FoldersOpen = {}
with open('WDKFunctions/WDKDataBase/FoldersOpening.csv', 'r') as csv1_file:
    csv1_reader= csv.reader(csv1_file)
    for line in csv1_reader:
        FoldersOpen[line[0]] = line[1]




#OpenFolder Function
def OpenFolderF(command):
    try:
        folder = FoldersOpen[command]
        os.startfile(folder)
        return 'done'
    except:
        return 'Invalid'