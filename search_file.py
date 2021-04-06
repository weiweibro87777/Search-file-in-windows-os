import os
import time
import tkinter as tk
from tkinter.filedialog import askdirectory
tk.Tk().withdraw() # Close the root window
folder_to_read = askdirectory()
if folder_to_read == "":
    print("Exiting program")
    quit()
if folder_to_read[-1] != '/':
    folder_to_read += '/'
folder_path = os.path.dirname(folder_to_read)
path,folder_name = os.path.split(folder_path)
if folder_name is "":
    folder_name = folder_to_read
    if folder_name[-2:] == ':/':
        folder_name = folder_name[:-2]
search_string = ""
while search_string is "":
    search_string = input("請輸入想搜尋的檔名:\n").lower()
search_results_found = 0
print("搜尋中...")
start_time = time.time()
with open(folder_name + " 檔案搜尋結果.txt", "w", encoding="utf-8") as a:
    a.write("Searches found for " + search_string + ":\n")
    for search_path, subdirs, files in os.walk(os.path.normpath(folder_to_read)):
        for filename in files:
            f = os.path.join(search_path, filename)
            if search_string in f.lower():
                search_results_found += 1
                a.write( f + os.linesep)
seconds = time.time() - start_time
m, s = divmod(seconds, 60)
h, m = divmod(m, 60)
print("{:.0f} minutes and {:.1f} seconds used for searching folder contents for {}".format( m, s, search_string ))
print("Found {} search results for {}".format(search_results_found, search_string))