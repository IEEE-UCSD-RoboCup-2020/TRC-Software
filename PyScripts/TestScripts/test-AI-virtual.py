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
parser.add_argument("-d", "--debug", help="enable debug mode which will run Tritonbot in tab terminals", action="store_true")
parser.add_argument("--lmtbm", help="log monitored tritonbot module, give it a module name as argument")

args = parser.parse_args()
team_color = "-b" #default is blue team
mainsetup = "mainsetup-grsim-6v6.ini" #default setup
if args.setup != None:
    mainsetup = args.setup
    
lmtbm = "None"

if args.blue:
    team_color = "-b"
    print("Team color: blue")
if args.yellow:
    team_color = "-y"
    print("Team color: yellow")

if args.lmtbm != None:
    lmtbm = args.lmtbm


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
    #tritonbot_config = "tritonbot-erforcesim.ini" 
    tritonbot_config = "tritonbot-grsim.ini"   
    simulator = "erforcesim"

print("Simulator: " + simulator)

##########################################
def clear_ports():
    for i in range(0, num_robots):
        firstport = port_base + i * id_offset 
        os.system("fuser -k {port}/tcp".format(port = str(firstport)))
        os.system("fuser -k {port}/udp".format(port = str(firstport + 1)))
        os.system("fuser -k {port}/tcp".format(port = str(firstport + 2)))
        os.system("fuser -k {port}/udp".format(port = str(firstport + 3)))
        os.system("fuser -k {port}/udp".format(port = str(firstport + 4)))

atexit.register(clear_ports)
clear_ports()
##########################################






#run TritonSoccerAI (java)
run_cmd(["java", "-Xms16384M", "-jar", (tritonsoccerAI_path + "TritonSoccerAI-1.0-SNAPSHOT-jar-with-dependencies.jar"),
            team_color, "-vm", "test", "-s", simulator,
            (cfg_path + mainsetup),
            (cfg_path + robot_config)
            ], dir_path)

time.sleep(2) # sleep is needed or it might crash for unknown reason (in background mode, tab mode won't crash, which is wierd)

#run TritonBots (cpp x num_robots)
for i in range(0, num_robots):
    tb_port_base = str(port_base + i * id_offset)
    run_in = "background"
    if args.debug:
        run_in = "tab"
    if lmtbm != "None":  
        run_cmd([(tritonbot_path + "TritonBot"), 
            "-v", "-l", lmtbm, "-c", (cfg_path + tritonbot_config), str(tb_port_base)], 
              dir_path, run_in)
    else:
        run_cmd([(tritonbot_path + "TritonBot"), 
            "-v", "-c", (cfg_path + tritonbot_config), str(tb_port_base)], 
              dir_path, run_in)  
    time.sleep(1)




while (True):
    time.sleep(1000)
