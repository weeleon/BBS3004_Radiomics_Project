# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 15:50:29 2019

@author: Leonard Wee
"""
import pandas as pd
import glob

#path = r'//smb.isilon01.ad.maastro.nl/research/Projects/_Knowledge Engineering/P0122 - Radiomics in glioblastoma/Results_Leonard/gbm_tilburg_pyradiomics_1.1.1' # use your path
path = r'C:/pyradiomics-master/O-RAW-master/RFstore/CSV_output/lung1_1mm' # use your path
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    print(filename)
    try :
        df = pd.read_csv(filename, index_col=None, header=0)
        li.append(df)
    except :
        print("This did not have the expected data!")

frame = pd.concat(li, axis=0, ignore_index=True)

frame.to_csv('C:/pyradiomics-master/O-RAW-master/RFstore/CSV_output/2019-10-20_lung1_1mm_radiomics_features.csv', index=False)


