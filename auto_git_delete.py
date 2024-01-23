import os
import subprocess

# print(os.getcwd())
# os.chdir('01_python/')
# print(os.getcwd())

current_folder = os.getcwd()
for foldername, subfolders, filenames in os.walk(current_folder):
    # print(foldername, 'fn')
    # print(subfolders, 'sf')
    # print(filenames, 'fn')
    if '.git' in subfolders:
        # print(foldername)
        if foldername == current_folder:
            continue
        git_folder_path = os.path.join(foldername, '.git')
        subprocess.run(['rm', '-rf', git_folder_path])
        print(f'{git_folder_path} 폴더가 삭제되었습니다.')