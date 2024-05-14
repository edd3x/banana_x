import subprocess
import glob

gpt = '/Applications/snap/bin/gpt'
cali_graph = 'myGraph_DB.xml'

date = ['20181107T234814',
        '20190211T234811',
        '20191009T234820']
for d in date:
    prod_list = glob.glob('/Volumes/External_disk_1TB/S1/tryS1/S1A*{}*dim'.format(date))
    # date = prod_list1[0].split('.')[0].split('/')[5]
    # files_string = " ".join(prod_list1)
    path = '/Volumes/External_disk_1TB/S1/tryS1/'
    for p in prod_list[:3]:
        name = p.split('.')[0].split('/')[5]
        subprocess.call([
        gpt,
        cali_graph,
        '-Pinput={}'.format(p),
        '-Poutput={}{}'.format(path, name),
        ])
