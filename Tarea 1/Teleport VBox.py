import psutil
import time
import subprocess

def teleport_vm():

    while True:
        cpu_load = psutil.cpu_percent(interval=1)
        print("CPU : "+ str(cpu_load) +" %")
        if cpu_load > 40:
            subprocess.run('VBoxManage controlvm Ubu teleport --host localhost --port 6000', shell=True)
            print("Teleport VM successful")
            break

        time.sleep(5)
        
        
teleport_vm()