#!/usr/bin/env python
# coding: utf-8

# In[2]:


import argparse
import sys

import pandas as pd
import numpy as np
import readFasta
from features_code import *

# this file is used to generate features file.
filePath = "dataset"


# In[3]:


def todataframe(encoding):
    index_list = []
    new_list = []
    for i in encoding[1:]:
        new_list.append(i[1:])
        index_list.append(i[0])
    return new_list, index_list #返回特征向量以及序列名称列表



def catBoost_inputGenterator(fasta, **kw):
    features = ["AAC", "CKSAAP", "CTDC", "CTDT", "CTDD", "CTriad", "DPC","GAAC","GDPC"]#通过不同的方法将蛋白质序列转换为数值特征
    feature_dict = {}
    feature_list = []
    for i in features: #对于每一个特征生成特征向量
        cmd = i + '.' + i + '(fasta, **kw)' #动态生成调用命令，例如 "AAC.AAC(fasta, **kw)
        encoding = eval(cmd) #动态调用函数
        content, index = todataframe(encoding)
        feature_dict[i] = pd.DataFrame(content, columns=encoding[0][1:])
        feature_list.append(pd.DataFrame(content, columns=encoding[0][1:]))
        
            
    df = pd.concat(feature_list, axis=1)
    return df



# In[7]:


def generator(fasta_file=None, output_name=None):  #读取输入文件并生成特征文件进行输出
    if not fasta_file:
        print("Missing input files")
        print("Start prediction on independent test set samples")
        fasta_N = readFasta.readfasta("dataset/indep_test_N.fasta")
        fasta_P = readFasta.readfasta("dataset/indep_test_P.fasta")
        fasta = fasta_N + fasta_P
    else:
        fasta = readFasta.readfasta(fasta_file)
        
    kw = {'order': 'ACDEFGHIKLMNPQRSTVWY'}
    df_catBoost = catBoost_inputGenterator(fasta, **kw)
    print(df_catBoost)
    if not output_name:
        df_catBoost.to_csv("features/test.csv", index=True, header=True)
    else:
        df_catBoost.to_csv("features/%s.csv" % output_name, index=True, header=True)
if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description='generate feature')
    # parser.add_argument("--type", required=True,
    #                     choices=["benchmark", "predict"],
    #                     help="the encoding type")
    # parser.add_argument('--fasta_file', required=True, type=str, help='input fasta file')
    # parser.add_argument('--output_name', type=str, help='output file name')
    # args = parser.parse_args()
    # # print(args.type)
    # generator(args.fasta_file, args.output_path)
    generator()        


# In[ ]:




