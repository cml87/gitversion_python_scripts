#!/usr/bin/python3.8

import sys
from random import sample
import subprocess
from sys import stdout

import json

## This script runs gitversion in dir1 and puts its output in dir2, in a file.
## The name of the file will be "gv_<sha5>_<postfix>"
## sha5 is the first 5 characters of the sha of the current commit.
## postfix is a word that can be appended to the name of the file. The script receives it
## as an argument. If omitted, nothing is appended.


if len(sys.argv)==2:
    posfix_str= "_"+str(sys.argv[1])
else:
    posfix_str=""


## dir of the git project to run gitversion
dir1="/home/camilo/work/gitversionTests/test1"

## dir where the output of gitversion will be placed
dir2="/home/camilo/work/gitversionTests/test1/gvCommits/"


subprocess1 = subprocess.Popen("gitversion", shell=True, stdout=subprocess.PIPE,cwd=dir1)
subprocess_return = subprocess1.stdout.read()
##print(subprocess_return)

subprocess_return_json_object = json.loads(subprocess_return)

##print(type(subprocess_return_json_object))
sha_str=str(subprocess_return_json_object["Sha"])
sha5_str=sha_str[:5]


outputFFN = dir2+"gv_"+sha5_str+posfix_str
if outputFFN[-1]=="_":
    outputFFN=outputFFN[:-1]

## gitversion -output file -outputfile '/home/camilo/t/ffggg'
cmd = "gitversion -output file -outputfile '"+outputFFN+"'"
subprocess2 = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,cwd=dir1)
subprocess_return = subprocess1.stdout.read()
print("outputFFN: "+outputFFN)
##print(subprocess_return)


##f = open(fileName, "w")
##f.write(gitversion_str.replace(",",",\n").replace("{","{\n ").replace("}","\n}"))
##f.close()





