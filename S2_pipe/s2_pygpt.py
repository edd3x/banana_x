import subprocess
import glob

gpt = '/Applications/snap/bin/gpt'
mos_graph = 'graphMultiSizeMosaicOp.xml'

dates = [
    '20190620T160519',
    '20191008T160509',
    '20181008T160511',
    '20181227T160501']


for d in dates:
    prod_list = glob.glob('/Volumes/External_disk_1TB/S2/tryS2/L2A/*{}*SAFE'.format(d))
    bands= ['B4', 'B8','quality_scene_classification']
    for b in bands:
        subprocess.call([
        gpt,
        mos_graph,
        '-PinputList0={}'.format(prod_list[0]),
        '-PinputList1={}'.format(prod_list[1]),
        '-PinputList2={}'.format(prod_list[2]),
        '-PinputList3={}'.format(prod_list[3]),
        '-PBandName1={}'.format(b),
        # '_P$var1BandExpression=B04',
        '-Pout1={}'.format('/Volumes/External_disk_1TB/S2L2/S2B_mos_{}_{}'.format(b, d))
        ])
