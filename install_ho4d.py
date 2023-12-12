import os
import time
import subprocess

time.sleep(7*60*60)

script_list = ['gdown https://drive.google.com/uc?id=1rQVoYsAilwmq66ilGj6d2Q2fUF7osrpn']

for each_script in script_list:
    each_script_list = each_script.split(' ')
    subprocess.call(each_script_list)





