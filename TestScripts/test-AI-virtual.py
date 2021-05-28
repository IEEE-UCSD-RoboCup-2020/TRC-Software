import os
import time
import subprocess 
import atexit      
import argparse
import configparser

dir_path = os.path.dirname(os.path.realpath(__file__)) + "/.."    
cfg_path = dir_path + "/Config/development/virtual/"
                      
                
def run_cmd(cmd, path, mode=None):
    if mode == None:
        print("### running " + ' '.join(map(str, cmd)) + " in current terminal")
        subprocess.Popen(cmd, cwd=path)
    if mode == "background":
        print("### running " + ' '.join(map(str, cmd))  + " as background process")
        subprocess.Popen(cmd, cwd=path, stdout=subprocess.PIPE) 
    if mode == "tab":
        print("### running" + ' '.join(map(str, cmd)) + " in a new terminal tab")
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



tritonbot_path = dir_path + "/TritonBot/build/"
for i in range(0, num_robots):
    tb_port_base = str(port_base + i * id_offset)
    run_cmd([(tritonbot_path + "./TritonBot"), 
            "-v", "-c", (cfg_path + "tritonbot-grsim.ini"), str(tb_port_base)], 
              dir_path, "tab")  


#AI_path =
#AI_cmd = 


while (True):
    time.sleep(1)
