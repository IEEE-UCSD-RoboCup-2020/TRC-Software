import os
import time
import subprocess 
import atexit      
import argparse
import configparser


robot_config = "robot-2021.ini"

dir_path = os.path.dirname(os.path.realpath(__file__)) + "/../.."    
cfg_path = dir_path + "/Config/development/virtual/"
tritonbot_path = dir_path + "/TritonBot/build/"
tritonsoccerAI_path = dir_path + "/TritonSoccerAI/target/"
                      
                
def run_cmd(cmd, path, mode=None):
    # annoying lengthy path is removed from the print out
    prt_cmd_str = ((' '.join(map(str, cmd))).replace(cfg_path,"")).replace(tritonbot_path,"")
    if mode == None:
        print(">>> running " + prt_cmd_str + " in current terminal")
        subprocess.Popen(cmd, cwd=path)
    if mode == "background":
        print(">>> running " + prt_cmd_str + " as background process")
        subprocess.Popen(cmd, cwd=path, stdout=subprocess.PIPE) 
    if mode == "tab":
        print(">>> running " + prt_cmd_str + " in a new terminal tab")
        subprocess.Popen(["gnome-terminal", "--tab", "--"] + cmd, cwd=path)


#available simulators: "grsim", "erforcesim"
parser = argparse.ArgumentParser()
parser.add_argument("-y", "--yellow", help="set yellow team to be tested", action="store_true")
parser.add_argument("-b", "--blue", help="set blue team to be tested", action="store_true")
parser.add_argument("-s", "--setup",  help="select a mainsetup-xxx.ini file in" + cfg_path)


args = parser.parse_args()
team_color = "-b" #default is blue team
mainsetup = "mainsetup-grsim-6v6.ini" #default setup

if args.blue:
    team_color = "-b"
    print("Team color: blue")
if args.yellow:
    team_color = "-y"
    print("Team color: yellow")
if args.setup != None:
    mainsetup = args.setup

config = configparser.ConfigParser()
config.read(cfg_path + mainsetup)
#print(config.sections())
#print(config.get('robot-connections', 'robot-port-base'))

env = config.get('basic-info', 'environment')
num_robots = int(config.get('robot-connections', 'num-robots'))
port_base = int(config.get('robot-connections', 'robot-port-base'))
id_offset = int(config.get('robot-connections', 'id-base-offset'))
#print(port_base)
#print(id_offset)
#print(env)
tritonbot_config = "tritonbot-grsim.ini" #default
simulator = "grsim" #default
if env == "grsim":
    tritonbot_config = "tritonbot-grsim.ini"  
    simulator = "grsim"
if env == "erforcesim":
    print("...")
    exit(-1)

print("Simulator: " + simulator)


print(">>> Enter TritonBot Module Name to Monitor (CamelCase, E.g.: McuClientModule)")
module_to_monitor = input()



#run TritonSoccerAI (java)
run_cmd(["java", "-jar", (tritonsoccerAI_path + "TritonSoccerAI-1.0-SNAPSHOT-jar-with-dependencies.jar"),
            team_color, "-vm", "test-tb", 
            (cfg_path + mainsetup)
            (cfg_path + robot_config)
            ], dir_path)

time.sleep(2) # sleep is needed or it might crash for unknown reason (in background mode, tab mode won't crash, which is wierd)

#run TritonBots (cpp x num_robots)
tb_port_base = str(port_base + 0 * id_offset)
run_in = "background"
run_in = "tab"
run_cmd([(tritonbot_path + "TritonBot"), 
        "-v", "-l", module_to_monitor, "-c", (cfg_path + tritonbot_config), str(tb_port_base)], 
            dir_path, run_in)  




while (True):
    time.sleep(1000)
