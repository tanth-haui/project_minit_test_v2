import PyInstaller.__main__
import PyInstaller.config
import os

print("path:", str(os.getcwd()))

distpath ="--distpath=" + r"C:\Training-Code\Python\Code_Folder\mini_test\App_build"
workpath = "--workpath=" + r"C:\Training-Code\Python\Code_Folder\mini_test\App_build\tempo"
PyInstaller.__main__.run([
    "--onedir",
    # "--onefile",
    r"C:\Training-Code\Python\Code_Folder\mini_test\Code_Vr1\main.py",
    "-nSignal_Processing",
    "--windowed",
    distpath,
    workpath,
    "--clean",
    "-y"
])
