import subprocess

result = subprocess.check_output("arp -a", shell=True)

print(result.decode())