import subprocess
import glob

files = glob.glob('/Volumes/External_disk_1TB/S2/tryS2/*MSIL1C*SAFE')

for prod in files:
    subprocess.call([
    '/Users/eddie/Desktop/banana_wd/Sen2Cor-02.08.00-Darwin64/bin/L2A_Process',
        prod
])
