#! /usr/bin/python
import os 
import sys
import subprocess
import time

user = input('Start Update ? (y/n) ')

def upgrader():

    subprocess.run(f'sudo apt-get update && sudo apt-get upgrade -y > Update_Logs.txt', shell=True)
    subprocess.run(f'sudo apt autoremove', shell=True)

    try:
        contents = Update_Logs.read()

        if "kernel" in contents:
            kernel = input('It seems like the Kernel has been updated, would you like to reboot now ? (y/n)')
            if kernel == "y":
                print("System rebooting in 5 seconds ...")
                time.sleep(5)
                subprocess.run('sudo reboot', shell=True)
            else:
                pass
    except:
        pass

upgrader()
keep = input('Keep update logs file ? (y/n)')
if keep == "y":
    pass
else:
     subprocess.run('rm Update_Logs.txt', shell=True)

print('Updater has finished everthing, have a good day !!!')