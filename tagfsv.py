#!/usr/bin/python3.8


import sys
import subprocess
from sys import stdout

import json

## This script goes to the directory 'dir', runs "git version" and then creates a tag for the 
## current commit (extracted from gitversion) with the FulSemVer (also extracted from gitversion)

dir="/home/camilo/work/gitversionTests/test1"

subprocess1 = subprocess.Popen("gitversion", shell=True, stdout=subprocess.PIPE,cwd=dir)
subprocess_return = subprocess1.stdout.read()

subprocess_return_json_object = json.loads(subprocess_return)

sha_str=str(subprocess_return_json_object["Sha"])

fullsemver_str=str(subprocess_return_json_object["FullSemVer"])
fullsemver_str_tag = "__"+fullsemver_str

print(fullsemver_str_tag)


cmd = "git tag \""+fullsemver_str_tag + "\" "+sha_str 

subprocess2 = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,cwd=dir)
subprocess_return = subprocess2.stdout.read()