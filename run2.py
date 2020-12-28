import os
import time
import subprocess                                               

dir_path = os.path.dirname(os.path.realpath(__file__))

vfirm_dir = dir_path + "/Virtual-Firmware-grSim"
vfirm_cmd = "./vfirm.exe"
vfirm_port = "8888"
vfirm_robot_id = "0"
vfirm_is_blue = "1"
vfirm_full_cmd = [vfirm_cmd, vfirm_port, vfirm_robot_id, vfirm_is_blue]

tritonBot_dir = dir_path + "/TritonBot/build/"
tritonBot_cmd = "./TritonBot.exe"
tritonBot_virtual = "-v"
tritonBot_port_base = "6000"
tritonBot_vfirm_port = vfirm_port
tritonBot_full_cmd = [tritonBot_cmd, tritonBot_virtual, tritonBot_port_base, tritonBot_vfirm_port]

rcCore_dir = dir_path + "/TritonSoccerAI"                                                            
rcCore_cmd = "mvn"
rcCore_package = "package"
rcCore_exec = "exec:java"
rcCore_full_cmd = [rcCore_cmd, rcCore_exec]                                
                                                                
def run_cmd(cmd, cwd):
    print("opening new terminal with command: " + ' '.join(map(str, cmd))  + " at " + cwd)
    subprocess.Popen(["gnome-terminal", "--"] + cmd, cwd=cwd)                                                   

os.system("fuser -k {port}/tcp".format(port = vfirm_port))
run_cmd(vfirm_full_cmd, vfirm_dir)
time.sleep(2)
run_cmd(tritonBot_full_cmd, tritonBot_dir)
time.sleep(2)
run_cmd(rcCore_full_cmd, rcCore_dir)
