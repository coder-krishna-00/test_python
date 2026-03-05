#!/usr/bin/env python3

import subprocess

svc = input("Enter the Service you want to check: ")
check_cmd = ["ps", "-C", svc]
service_check = subprocess.call(check_cmd)
if service_check == 0:
    print("Service is running")
else:
    print("Service is NOT running. \n Starting it...")
    subprocess.call(["sudo", "systemctl", "start", svc])
    subprocess.call(check_cmd)
