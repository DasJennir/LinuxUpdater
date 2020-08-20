#! /usr/bin/python
import sys
import subprocess
import time

user = input('Start Update ? (y/n) ')

def upgrader():

    if user == "y":
        subprocess.run(f'sudo apt-get update >> Update_Logs.txt  && sudo apt-get upgrade -y >> Update_Logs.txt && sudo apt autoremove >> Update_Logs.txt ' , shell=True)
        subprocess.run(f'sudo apt autoremove', shell=True)
        
        try:
            with open('Update_Logs.txt', 'r') as f:
                contents = f.read()
                if "kernel" in contents:
                    kernel = input('It seems like the Kernel has been updated, would you like to reboot now ? (y/n) ')
                    if kernel == "y":
                        print("System rebooting in 5 seconds ...")
                        time.sleep(5)
                        subprocess.run('sudo reboot', shell=True)
                    else:
                        print('Update_Logs File not Found')
        except:
            pass

        
    else:
        exit()

        
upgrader()
keep = input('Keep update logs file ? (y/n) ')
if keep == "y":
    pass
else:
     subprocess.run('rm Update_Logs.txt', shell=True)

print('Updater has finished everthing, have a good day !!!')