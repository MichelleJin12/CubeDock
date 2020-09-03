# -*- coding: utf-8 -*-

import sys
import subprocess
import shlex

from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit import print_formatted_text

def _CommandRun(command):
    line = FormattedText([
        ('', '['),
        ('#ff0000', 'Out'),
        ('', ']')
    ])

    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)

    while True:
        output = process.stdout.readline()

        if output == b'' and process.poll() is not None:
            break
        if output:
            print_formatted_text(line, end="")
            print(">> " + output.strip().decode('utf-8'))
    rc = process.poll()
    return rc

def _Eval_Container_Argument() :
    return True 
def _Evel_Machine_Argument() :
    return True

def _ConcatStr() :
    _TSysArgString = ""

    for _Arg in sys.argv:
        _TSysArgString += _Arg + ' '
    
    return _TSysArgString

def Cli_Parse(*args, **kwargs) :
    _TFirstArgv = sys.argv[1]
    
    sys.argv.pop(0)
    sys.argv.pop(0)
    _TMakedArgument = _ConcatStr()
    
    if _TFirstArgv == "machine" :
        if _Evel_Machine_Argument() is True:
            _CommandRun('docker-machine ' + _TMakedArgument)
            #subprocess.call('docker-machine ' + _TMakedArgument, shell=True)
        
    elif _TFirstArgv == "container" :
        if _Eval_Container_Argument() is True:
            _CommandRun('docker ' + _TMakedArgument)
            #subprocess.call('docker ' + _TMakedArgument, shell=True)
    
if __name__ == '__main__':
    sys.exit(Cli_Parse())