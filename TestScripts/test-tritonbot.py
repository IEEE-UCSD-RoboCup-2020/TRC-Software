import os
import time
import subprocess 

dir_path = os.path.dirname(os.path.realpath(__file__)) + "/.." 

tritonBot_dir = dir_path + "/TritonBot/build/"
tritonBot_cmd = "./TritonBot"
tritonBot_args = ["-vt", "-i", "0"]
tritonBot_port_base_base = 6500


AI_dir = dir_path + "/TritonSoccerAI"                                                            
AI_cmd = "java"
AI_tag = "-jar"
AI_file = "target/TritonSoccerAI-1.0-SNAPSHOT-jar-with-dependencies.jar"
AI_team = "BLUE"
AI_prog_mode = "TEST_TRITONBOT"
AI_Robots_IPaddr = "127.0.0.1"
AI_Robots_IPportBase = str(tritonBot_port_base_base)
AI_full_cmd = [AI_cmd, AI_tag, AI_file, AI_team, AI_prog_mode, AI_Robots_IPaddr, AI_Robots_IPportBase] 

def run_cmd_term(cmd, cwd, tab = True):
    if tab == True:
        print("opening new terminal with command: " + ' '.join(map(str, cmd)))
        subprocess.Popen(["gnome-terminal", "--tab", "--"] + cmd, cwd=cwd)                                                   
    else:
        print("running " + ' '.join(map(str, cmd))  + " as background process")
        subprocess.Popen(cmd, cwd=cwd, stdout=subprocess.PIPE)                                                   
                
def run_main_cmd(cmd, cwd):
    subprocess.Popen(cmd, cwd=cwd)

run_cmd_term(AI_full_cmd, AI_dir, True)


run_main_cmd([tritonBot_cmd, tritonBot_args[0], tritonBot_args[1], 
                tritonBot_args[2], str(tritonBot_port_base_base)], tritonBot_dir)   



while (True):
    time.sleep(100)