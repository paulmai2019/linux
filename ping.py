import subprocess

host = input('Enter a host ping:')

p1 = subprocess.run(['ping', '-c 1', host])
