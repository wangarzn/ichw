#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.
引用了三个模块，从第一个模块中获取标点符号，通过第二个模块与本地进行交互，通过第三个模块解析命令行给的URL获取文本。

__author__ = "Qichao Wang"
__pkuid__  = "1800011837"
__email__  = "180001837@pku.edu.cn"
"""


import string
import sys
from urllib.request import urlopen


def wcount(lines, topn):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line.
    变量 lines：读取的文件
    变量 topn ：打印的单词数目
    变量 strlines ：字符串形式的文本（所有的单词均转化成了小写）
    变量 ls1  ：把字符串格式的文本切成列表
    变量 ls2  ：把ls1中每个元素转化为元组，元组第二项为该字符的数目，然后进行去重
    """
    strlines = lines.decode()  # 将字节流转化为字符串
    for c in string.punctuation:
        if c != "'":
            strlines = strlines.replace(c, " ")  # 把所有的标点替换为空格,单引号不变，排除所有格和缩写
    strlines = strlines.lower()
    ls1 = strlines.split()  # 把字符串转化为列表
    ls2 = list(set([(i, ls1.count(i)) for i in ls1]))
    # ls2中包含互不重复的元组，元祖第一项为单词名称，第二项为单词在整个文本中出现的次数
    ls2.sort(key=lambda x: x[1], reverse=True)
    length = len(ls2)
    if topn > length:
        for i in ls2:
            print(i[0], "   ", i[1])   
    else:
        for i in ls2[:topn]:
            print(i[0], "   ", i[1])


if __name__ == '__main__':
    """ sys.argv 通过命令提示行得到的列表，一定存在第一项，为文件名。
    """
    if len(sys.argv) == 1:
        # 命令行仅给了一个参数，则无法找到网页，无法计数
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    text = urlopen(sys.argv[1])
    text0 = text.read()
    text.close()

    if len(sys.argv) == 2:
        # 命令行给了2个参数，给出仅给出十个结果
        wcount(text0, 10)
    if len(sys.argv) == 3:
        # 命令行给了3个参数，        
        wcount(text0, int(sys.argv[2]))
    if len(sys.argv) > 3:
        print("输入的参数多于应该输入的参数")
