import subprocess
import glob

gpt = '/Applications/snap/bin/gpt'
cali_graph = 's1pp_Graph_mos.xml'
# prod_list= glob.glob('/Volumes/External_disk_1TB/S1/*dim')
# date = prod_list1[0].split('.')[0].split('/')[5]
# files_string = " ".join(prod_list)
# print(prod_list[0])

subprocess.call([
gpt, cali_graph,
# '-Pinput0={}'.format(prod_list[0]),
# '-Pinput1={}'.format(prod_list[1])
])
