import sys, os
import subprocess, shlex
import json
import shutil
from FilterUtils import *

def getLocationsFile():
	return os.path.join(os.path.expanduser('~'), "Documents/locations.json")

def getDefaultStorageLocation():
	return os.path.join(os.path.expanduser('~'), "Downloads/")

def zipDir( dirLocation : str, outputLocation : str ):
    shutil.make_archive(outputLocation, 'zip', dirLocation)
    print(f" files saved to {outputLocation}")


def createStickerFiles( name, b, c, s, hasTex, t, oDir ) -> str:
    # create new folder to zip
    # add index, sticker, png files
    os.system(f"mkdir {name}")
    os.system(f'cp "{t}"  {name}/lookup.png')
    os.system(f'echo "{getFilterData(name, b, c, s, hasTex)}" > {name}/{name}.mat')
    os.system(f'echo "{getIndexFileData(name)}" > {name}/index.yaml')
    return os.path.join(os.getcwd(), name)

def deleteFiles( location : str ):
    os.system(f"rm -rf {location}")


def transformAndSave(name, b, c, s, hasTex, t, oDir) -> str:
    
    s = createStickerFiles( name, b, c, s, hasTex, t, oDir )
    zipDir( s, f"{oDir}/{name}" )
    deleteFiles( s )


    