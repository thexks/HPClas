import re, os, sys


def readfasta(file):
    if not os.path.exists(file):
        print('Error: "' + file + '" does not exist.')
        sys.exit(1)

    with open(file) as f:
        records = f.read()

    if re.search('>', records) is None:# 判断是否是fasta格式
        print('The input file seems not in fasta format.')
        sys.exit(1)

    records = records.split('>')[1:] # 去掉头
    myFasta = []
    for fasta in records:
        array = fasta.split('\n') # 去掉尾
        name, sequence = array[0].split()[0], re.sub('[^ARNDCQEGHILKMFPSTWYV-]', '-', ''.join(array[1:]).upper())#其中`pattern`是正则表达式模式只允许匹配括号内的字符，`repl`是替换后的字符串，`string`是要处理的原始字符串
        myFasta.append([name, sequence])
    return myFasta
