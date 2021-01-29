import os
import sys
import datetime
import time
import subprocess                                               

home = os.path.dirname(os.path.realpath(__file__)) + "/.." 

# Configure Logger
logdir = home + "/log/"
if not os.path.exists(logdir):
    os.mkdir(logdir)
timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
logdir = logdir + timestamp + '/'
if not os.path.exists(logdir):
    os.mkdir(logdir)

vfirm_dir = home + "/Virtual-Firmware-grSim"
vfirm_cmd = "./vfirm.exe"
vfirm_port = "8888"
vfirm_robot_id = "0"
vfirm_is_blue = "1"
vfirm_logfn = logdir + "vfirm.txt"
vfirm_full_cmd = [vfirm_cmd, vfirm_port, vfirm_robot_id, vfirm_is_blue]

tritonBot_dir = home + "/TritonBot/build/"
tritonBot_cmd = "./TritonBot.exe"
tritonBot_virtual = "-v"
tritonBot_port_base = "6000"
tritonBot_vfirm_port = vfirm_port
tritonBot_logfn = logdir + "tritonBot.txt"
tritonBot_full_cmd = [tritonBot_cmd, tritonBot_virtual, tritonBot_port_base, tritonBot_vfirm_port]

AI_dir = home + "/TritonSoccerAI"                                                            
AI_cmd = "java"
AI_tag = "-jar"
AI_file = "target/TritonSoccerAI-1.0-SNAPSHOT-jar-with-dependencies.jar"
AI_logfn = logdir + "AI.txt"
AI_full_cmd = [AI_cmd, AI_tag, AI_file]                 

def run_cmd(cmd, cwd, logfn):
    with open(logfn, 'w') as logfile:
        return subprocess.Popen(cmd, cwd=cwd, stdout=logfile, stderr=logfile)

os.system("fuser -k {port}/tcp".format(port = vfirm_port))
vfirm = run_cmd(vfirm_full_cmd, vfirm_dir, vfirm_logfn)
time.sleep(2)
tritonBot = run_cmd(tritonBot_full_cmd, tritonBot_dir, tritonBot_logfn)
time.sleep(2)
AI = run_cmd(AI_full_cmd, AI_dir, AI_logfn)

tail_full_cmd = ["multitail",]
for tag in sys.argv[1:]:
    if "j" in tag: 
        tail_full_cmd.append(AI_logfn)
    if "c" in tag:
        tail_full_cmd.append(tritonBot_logfn)
    if "v" in tag:
        tail_full_cmd.append(vfirm_logfn)

tail = subprocess.Popen(tail_full_cmd)
tail.wait()