import os

path = r'C:\Documents and Settings\HP\PycharmProjects\obychenie\venv\Zhelonkina_Alyona_dz_7\task_dz_7.3'
dir_name = 'my_project_2'
dir_name_folders = ['settings', 'mainapp', 'authapp']

dir_name_my_project = os.path.join(path, dir_name)
if not os.path.exists(dir_name_my_project):
    os.mkdir(dir_name_my_project)

for folder in dir_name_folders:
    dir_name_folder = os.path.join(dir_name_my_project, folder)
    if not os.path.exists(dir_name_folder):
        os.makedirs(dir_name_folder)

file_1 = open('my_project_2\settings\dev.py', 'w', encoding='utf-8')
file_1.close()
file_1 = open('my_project_2\settings\prod.py', 'w', encoding='utf-8')
file_1.close()

# остальные директории и файлы создам в "ручном режиме"
import shutil
import os
from shutil import copytree
from os.path import join

my_dir = r'C:\Documents and Settings\HP\PycharmProjects\obychenie\venv\Zhelonkina_Alyona_dz_7\task_dz_7.3\my_project_2\templates'
if not os.path.exists(my_dir):
    os.mkdir(my_dir)
folder = r'my_project_2'
files = []
for r, d, f in os.walk(folder):
    for file in f:
        if '.html' in file:
	        files.append(os.path.join(r, file))
for path in files:
    folder_new = os.path.join(my_dir, os.path.basename(os.path.dirname(path)))
    if not os.path.exists(folder_new):
        os.mkdir(folder_new)
    save_path = os.path.join(folder_new, os.path.basename(path))
    shutil.copy(path, save_path)

# возможные исключения
dir_1 = r"my_project_2\authapp\templates"
new_1 = r"my_project_2"
path_src = join(dir_1)
path_dist = os.path.join(new_1, "templates")
try:
    copytree(path_src, path_dist)
except FileExistsError:
      print(None, 'попытке создать уже существующий файл или каталог')
