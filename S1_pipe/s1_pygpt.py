import subprocess
import glob

gpt = '/Applications/snap/bin/gpt' # Path to the GPT in the SNAP installation
xml_graph = 's1pp_Graph_all.xml' # Path to the Graph XML file
prod_list = glob.glob('/Volumes/External_disk_1TB/S1/s1update/S1A*zip') # Path to the list of S1 files

path = '/Volumes/External_disk_1TB/S1/s1update/' # Path output directory 

for p in prod_list:
    name = p.split('.')[0].split('/')[5]
    subprocess.call([
    gpt,
    xml_graph,
    '-Pinput={}'.format(p), # Input variable in the XML file
    '-Poutput1={}{}_VH'.format(path, name), # Output1 variable in the XML file
    '-Poutput2={}{}_VV'.format(path, name) # Output2 variable in the XML file
    ])
