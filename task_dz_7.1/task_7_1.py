import os

path = r'C:\Documents and Settings\HP\PycharmProjects\obychenie\venv\Zhelonkina_Alyona_dz_7\task_dz_7.1'
dir_name = 'my_project'
dir_name_folders = ['settings', 'mainapp', 'adminapp', 'authapp']

dir_name_my_project = os.path.join(path, dir_name)
if not os.path.exists(dir_name_my_project):
    os.mkdir(dir_name_my_project)

for folder in dir_name_folders:
    dir_name_folder = os.path.join(dir_name_my_project, folder)
    if not os.path.exists(dir_name_folder):
        os.makedirs(dir_name_folder)