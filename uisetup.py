from distutils.core import setup
import py2exe
import sys

sys.argv.append('py2exe')
INCLUDES = []

options = {
    "py2exe" :
        {
            "optimize" : 2,
            "bundle_files" : 3, # 所有文件打包成一个 exe 文件
            "includes" : INCLUDES,
            "dll_excludes" : ["MSVCR100.dll"]
        }
}

setup(
    options=options,
    description = "setup",
    zipfile=None,

    #console = [{"script":'Json2fbx.py'}])

    console = [{"script":'main.py',"icon_resources":[(1,"favicon.ico")]}])