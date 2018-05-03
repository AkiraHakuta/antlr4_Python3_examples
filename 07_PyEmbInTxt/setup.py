# python.exe setup.py 
import cx_Freeze
import sys

sys.argv.append('build')
# python.exe setup.py build

base = None
includes = []
include_files = ["gen"]
excludes = []
packages = ['antlr4']
executables = [cx_Freeze.Executable(script="pyEmbInTxt.py",targetName="pyEmbInTxt.exe", base = base),]

cx_Freeze.setup(
    name = "PyEmbInTxt",
    options = {"build_exe": 
        {"build_exe":"pyText/","includes":includes, "include_files": include_files, "excludes": excludes,"packages": packages}},
    version = "1.0",
    description = "PyEmbInTxt runs Python in text file",
    executables = executables)
