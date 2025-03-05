#!/usr/bin/env python
# _*_coding:utf-8_*_

import re, sys, os

pPath = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(pPath)
import readFasta
import checkFasta

USAGE = """
USAGE:
	python CKSAAP.py input.fasta <k_space> <output>

	input.fasta:      the input protein sequence file in fasta format.
	k_space:          the gap of two amino acids, integer, defaule: 5
	output:           the encoding file, default: 'encodings.tsv'
"""


def CKSAAP(fastas, gap=3, **kw):
    if gap < 0:
        print('Error: the gap should be equal or greater than zero' + '\n\n')
        return 0

    if checkFasta.minSequenceLength(fastas) < gap + 2:
        print('Error: all the sequence length should be larger than the (gap value) + 2 = ' + str(gap + 2) + '\n\n')
        return 0

    AA = kw['order'] if kw['order'] != None else 'ACDEFGHIKLMNPQRSTVWY'
    encodings = []
    aaPairs = []
    for aa1 in AA:#生成所有可能的氨基酸对
        for aa2 in AA:
            aaPairs.append(aa1 + aa2)
    header = ['#']
    for g in range(gap + 1):
        for aa in aaPairs:
            header.append(aa + '.gap' + str(g))#生成特征名称
    encodings.append(header)
    for i in fastas:
        name, sequence = i[0], i[1]
        code = [name]
        for g in range(gap + 1):
            myDict = {}
            for pair in aaPairs:
                myDict[pair] = 0
            sum = 0
            for index1 in range(len(sequence)):
                index2 = index1 + g + 1
                if index1 < len(sequence) and index2 < len(sequence) and sequence[index1] in AA and sequence[
                    index2] in AA:
                    myDict[sequence[index1] + sequence[index2]] = myDict[sequence[index1] + sequence[index2]] + 1 # 统计该氨基酸对的出现次数
                    sum = sum + 1# 统计有效对的总数
            for pair in aaPairs:
                code.append(myDict[pair] / sum)#归一化
        encodings.append(code)
    return encodings


