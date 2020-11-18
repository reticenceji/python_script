import zipfile
import os

def unzip(path,zfile):
    file_path=path+os.sep+zfile
    desdir=path+os.sep+zfile[:zfile.index('.zip')]
    srcfile=zipfile.ZipFile(file_path)
    for filename in srcfile.namelist():
        srcfile.extract(filename,desdir)
        if filename.endswith('.zip'):
            # if zipfile.is_zipfile(filename):
            path=desdir
            zfile=filename
            unzip(path,zfile)

path=r'/home/reticence/Documents/Code/python/aaa/'
zfile=r'droste.zip'
unzip(path,zfile)