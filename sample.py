# import numpy as np
#
# print(np.arange(0,9))
# import pandas as pd
#
# data = pd.read_csv('/Users/knight/Desktop/AA_Prac.csv',index_col= 0)
# print(data)
#
# import sys
# print('Python: {}'.format(sys.version))
#
# # import re
# #
# # vowelRegex = re.compile(r'[aeiou]')
# # print(vowelRegex.findall('Knight Samurai live by rules.Are waah'))


import os

# path_to_watch = '/Users/knight/Desktop'
# print(os.listdir(path_to_watch))
#
# before = dict([(f, None) for f in os.listdir (path_to_watch)])
# print(before)

# import os, time
# def run():
#     path_to_watch = "/Users/knight/Desktop/Read"
#     print("watching: " + path_to_watch)
#     before = dict ([(f, None) for f in os.listdir (path_to_watch)])
#     switch = True
#     while switch:
#         after = dict ([(f, None) for f in os.listdir (path_to_watch)])
#         added = [f for f in after if not f in before]
#         removed = [f for f in before if not f in after]
#         if added: print ("Added: ", ", ".join (added))
#         if removed: print ("Removed: ", ", ".join (removed))
#         before = after
#         switch = False
#         # time.sleep(10)
# if __name__ == "__main__":
#     print(run())

# import os
# import time
# import shutil
# from shutil import copyfile
#
# # def run():
# path_to_original = "/Users/knight/Desktop/Read/"
# path_to_backup = "/Users/knight/Desktop/backup"
# print("watching: " + path_to_original)
# original = dict([(f, None) for f in os.listdir(path_to_original)])
# #     switch = True
# #     while switch:
# backup = dict([(f, None) for f in os.listdir(path_to_backup)])
#         added = [f for f in original if not f in backup: copy2(f,path_to_backup)]

#         removed = [f for f in backup if not f in original]
#         if added: print ("Added: ", ", ".join (added)) #and copy2(path_to_original, path_to_backup)
#         if removed: print ("Removed: ", ", ".join (removed))
#         # backup = original
#         switch = False
#         # time.sleep(10)
# if __name__ == "__main__":
#     print(run())

# shutil.copy2('/Users/knight/Desktop/Read/',
#              '/Users/knight/Desktop/backup')

##########################
##########################
# original = dict([(f, None) for f in os.listdir(path_to_original)])
# backup = dict([(f, None) for f in os.listdir(path_to_backup)])
# print(original)
# for f in original:
#     if not f in backup:
#         # print('/Users/knight/Desktop/Read/" '+f+' "')
#         shutil.copy2('/Users/knight/Desktop/Read/'+f+'',
#                      '/Users/knight/Desktop/backup/'+f+'')

import subprocess

p1 = subprocess.run(['cat', '/Users/knight/Desktop/udemy.txt'], capture_output=True, text = True)
print(p1.stdout)
