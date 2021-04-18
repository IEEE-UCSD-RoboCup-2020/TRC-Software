import os
import time
import subprocess 
import atexit                                              

dir_path = os.path.dirname(os.path.realpath(__file__)) + "/.."     


def run_cmd_term(cmd, cwd, tab = True):
    if tab == True:
        print("opening new terminal with command: " + ' '.join(map(str, cmd)))
        subprocess.Popen(["gnome-terminal", "--tab", "--"] + cmd, cwd=cwd)                                                   
    else:
        print("running " + ' '.join(map(str, cmd))  + " as background process")
        subprocess.Popen(cmd, cwd=cwd, stdout=subprocess.PIPE)                                                   
                
def run_cmd(cmd, cwd):
    subprocess.Popen(cmd, cwd=cwd)
    
    
run_cmd_term(["make", "run-blue"], dir_path, True)
run_cmd_term(["make", "run-yellow"], dir_path, True)
time.sleep(12)
# run_cmd(["make", "gc"], dir_path)
# kickOff

while (True):
    time.sleep(1)