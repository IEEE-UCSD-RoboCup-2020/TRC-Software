import os
import time
import subprocess 

dir_path = os.path.dirname(os.path.realpath(__file__)) + "/.." 

tritonBot_dir = dir_path + "/TritonBot/build/"
tritonBot_cmd = "./TritonBot"
tritonBot_args = "-vt"
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
                                                
            

subprocess.Popen([tritonBot_cmd, tritonBot_args, str(tritonBot_port_base_base)], cwd=tritonBot_dir)

time.sleep(1)

print("opening new terminal with command: " + ' '.join(map(str, AI_full_cmd)))
subprocess.Popen(["gnome-terminal", "--"] + AI_full_cmd, cwd=AI_dir)



while (True):
    time.sleep(100)